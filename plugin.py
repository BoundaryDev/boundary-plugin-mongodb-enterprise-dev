from __future__ import (absolute_import, division, print_function, unicode_literals)
import logging
import time
import sys
from pysnmp.entity.rfc3413.oneliner import cmdgen

import boundary_plugin
import boundary_accumulator

"""
If getting statistics fails, we will retry up to this number of times before
giving up and aborting the plugin.  Use 0 for unlimited retries.
"""
PLUGIN_RETRY_COUNT = 0
"""
If getting statistics fails, we will wait this long (in seconds) before retrying.
"""
PLUGIN_RETRY_DELAY = 5


class MongoDBPlugin(object):
    def __init__(self, boundary_metric_prefix):
        self.boundary_metric_prefix = boundary_metric_prefix
        self.settings = boundary_plugin.parse_params()
        self.accumulator = boundary_accumulator
        self.cmdGen = cmdgen.CommandGenerator()

    def snmp_get_first_row_value(self, instance, oid):
        error_indication, error_status, error_index, var_bind_table = self.cmdGen.nextCmd(
            cmdgen.CommunityData(instance['community']),
            cmdgen.UdpTransportTarget((instance['hostname'], instance['port'])),
            oid, maxRows=1,
            ignoreNonIncreasingOid=True)

        if error_indication:
            raise Exception(error_indication)

        if error_status:
            raise Exception('%s at %s' % (
                error_status.prettyPrint(),
                error_index and var_bind_table[-1][int(error_index) - 1] or '?'
                ))

        return var_bind_table[0][0][1]

    def report_stats(self, instance):
        for metric_item in self.get_metric_list():
            boundary_name, oid, accumulate = metric_item[:3]
            value = self.snmp_get_first_row_value(instance, oid)

            if accumulate:
                value = self.accumulator.accumulate(boundary_name, value)
            boundary_plugin.boundary_report_metric(self.boundary_metric_prefix + boundary_name,
                                                   value, source=instance['source_name'])

    def report_stats_with_retries(self, *args, **kwargs):
        """
        Calls the get_stats function, taking into account retry configuration.
        """
        retry_range = xrange(PLUGIN_RETRY_COUNT) if PLUGIN_RETRY_COUNT > 0 else iter(int, 1)
        for _ in retry_range:
            try:
                return self.report_stats(*args, **kwargs)
            except Exception as e:
                logging.error("Error retrieving data: %s" % e)
                time.sleep(PLUGIN_RETRY_DELAY)

        logging.fatal("Max retries exceeded retrieving data")
        raise Exception("Max retries exceeded retrieving data")

    def get_source_name(self, instance):
        return self.snmp_get_first_row_value(instance, cmdgen.MibVariable('MONGOD-MIB', 'serverName'))

    @staticmethod
    def get_metric_list():
        return (
            ('MONGODB_GLOBAL_OP_INSERT', cmdgen.MibVariable('MONGOD-MIB', 'globalOpInsert'), True),
            ('MONGODB_GLOBAL_OP_QUERY', cmdgen.MibVariable('MONGOD-MIB', 'globalOpQuery'), True),
            ('MONGODB_GLOBAL_OP_UPDATE', cmdgen.MibVariable('MONGOD-MIB', 'globalOpUpdate'), True),
            ('MONGODB_GLOBAL_OP_DELETE', cmdgen.MibVariable('MONGOD-MIB', 'globalOpDelete'), True),
            ('MONGODB_GLOBAL_OP_GETMORE', cmdgen.MibVariable('MONGOD-MIB', 'globalOpGetMore'), True),
            ('MONGODB_GLOBAL_OP_COMMAND', cmdgen.MibVariable('MONGOD-MIB', 'globalOpCommand'), True),
            ('MONGODB_REPL_OP_INSERT', cmdgen.MibVariable('MONGOD-MIB', 'replOpInsert'), True),
            ('MONGODB_REPL_OP_QUERY', cmdgen.MibVariable('MONGOD-MIB', 'replOpQuery'), True),
            ('MONGODB_REPL_OP_UPDATE', cmdgen.MibVariable('MONGOD-MIB', 'replOpUpdate'), True),
            ('MONGODB_REPL_OP_DELETE', cmdgen.MibVariable('MONGOD-MIB', 'replOpDelete'), True),
            ('MONGODB_REPL_OP_GETMORE', cmdgen.MibVariable('MONGOD-MIB', 'replOpGetMore'), True),
            ('MONGODB_REPL_OP_COMMAND', cmdgen.MibVariable('MONGOD-MIB', 'replOpCommand'), True),
            ('MONGODB_MEMORY_RESIDENT', cmdgen.MibVariable('MONGOD-MIB', 'memoryResident'), False),
            ('MONGODB_MEMORY_VIRTUAL', cmdgen.MibVariable('MONGOD-MIB', 'memoryVirtual'), False),
            ('MONGODB_CONNECTIONS_CURRENT', cmdgen.MibVariable('MONGOD-MIB', 'connectionsCurrent'), False),
            ('MONGODB_CURSOR_TOTAL_OPEN', cmdgen.MibVariable('MONGOD-MIB', 'cursorTotalOpen'), False),
            ('MONGODB_CURSOR_CLIENT_SIZE', cmdgen.MibVariable('MONGOD-MIB', 'cursorClientSize'), False),
            ('MONGODB_INDEX_ACCESSES', cmdgen.MibVariable('MONGOD-MIB', 'indexCounterAccesses'), True),
            ('MONGODB_INDEX_HITS', cmdgen.MibVariable('MONGOD-MIB', 'indexCounterHits'), True),
            ('MONGODB_INDEX_MISSES', cmdgen.MibVariable('MONGOD-MIB', 'indexCounterMisses'), True),
            ('MONGODB_NETWORK_IN', cmdgen.MibVariable('MONGOD-MIB', 'networkBytesIn'), True),
            ('MONGODB_NETWORK_OUT', cmdgen.MibVariable('MONGOD-MIB', 'networkBytesOut'), True),
            ('MONGODB_NETWORK_REQUESTS', cmdgen.MibVariable('MONGOD-MIB', 'networkNumRequests'), True),
            ('MONGODB_METRICS_DOCUMENT_DELETED', cmdgen.MibVariable('MONGOD-MIB', 'metricsDocumentDeleted'), True),
            ('MONGODB_METRICS_DOCUMENT_INSERTED', cmdgen.MibVariable('MONGOD-MIB', 'metricsDocumentInserted'), True),
            ('MONGODB_METRICS_DOCUMENT_RETURNED', cmdgen.MibVariable('MONGOD-MIB', 'metricsDocumentReturned'), True),
            ('MONGODB_METRICS_DOCUMENT_UPDATED', cmdgen.MibVariable('MONGOD-MIB', 'metricsDocumentUpdated'), True)
        )

    def main(self):
        logging.basicConfig(level=logging.ERROR, filename=self.settings.get('log_file', None))
        reports_log = self.settings.get('report_log_file', None)
        if reports_log:
            boundary_plugin.log_metrics_to_file(reports_log)
        boundary_plugin.start_keepalive_subprocess()

        instances = self.settings['items']
        while True:
            for instance in instances:
                instance['source_name'] = self.get_source_name(instance)
                self.report_stats_with_retries(instance)
            boundary_plugin.sleep_interval()


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        logging.basicConfig(level=logging.INFO)

    plugin = MongoDBPlugin('')
    plugin.main()
