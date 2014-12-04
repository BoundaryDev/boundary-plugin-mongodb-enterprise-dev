# PySNMP SMI module. Autogenerated from smidump -f python MONGOD-MIB
# by libsmi2pysnmp-0.1.3 at Wed Dec  3 19:26:37 2014,
# Python version (2, 6, 6, 'final', 0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("RFC1213-MIB", "DisplayString")
( Bits, Counter32, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "enterprises")
( DateAndTime, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime")

# Objects

mongodbInc = MibIdentifier((1, 3, 6, 1, 4, 1, 34601))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1))
mongodb = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1))
mongod = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1))
mongodMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 1)).setRevisions(("2014-01-31 00:00",))
if mibBuilder.loadTexts: mongodMIB.setOrganization("MongoDB Inc")
if mibBuilder.loadTexts: mongodMIB.setContactInfo("http://www.mongodb.com/contact")
if mibBuilder.loadTexts: mongodMIB.setDescription("mib for the MongoDB mongod process")
serverTable = MibTable((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2))
if mibBuilder.loadTexts: serverTable.setDescription("This table gives information and statistics for each server.")
serverTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1)).setIndexNames((0, "MONGOD-MIB", "serverName"))
if mibBuilder.loadTexts: serverTableEntry.setDescription("This defines a server.")
serverName = MibTableColumn((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverName.setDescription("The port of the virtual server is the name.")
system = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 2))
port = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: port.setDescription("port for this process")
sysUpTime = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 2, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUpTime.setDescription("uptime (in hundredths of a second)")
version = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setDescription("MongoDB version")
pid = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pid.setDescription("process ID")
opcounts = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3))
globalOpcounts = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 1))
globalOpInsert = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalOpInsert.setDescription("global insert count")
globalOpQuery = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalOpQuery.setDescription("global query count")
globalOpUpdate = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalOpUpdate.setDescription("global update count")
globalOpDelete = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalOpDelete.setDescription("global delete count")
globalOpGetMore = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalOpGetMore.setDescription("global getmore count")
globalOpCommand = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalOpCommand.setDescription("global command count")
replOpcounts = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 2))
replOpInsert = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOpInsert.setDescription("repl insert count")
replOpQuery = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOpQuery.setDescription("repl query count")
replOpUpdate = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOpUpdate.setDescription("repl update count")
replOpDelete = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOpDelete.setDescription("repl delete count")
replOpGetMore = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOpGetMore.setDescription("repl getmore count")
replOpCommand = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 3, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOpCommand.setDescription("repl command count")
memory = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 4))
memoryResident = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 4, 1), Integer32()).setMaxAccess("readonly").setUnits("MB")
if mibBuilder.loadTexts: memoryResident.setDescription("resident memory used by mongod")
memoryVirtual = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 4, 2), Integer32()).setMaxAccess("readonly").setUnits("MB")
if mibBuilder.loadTexts: memoryVirtual.setDescription("virtual memory used by mongod")
memoryMapped = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 4, 3), Integer32()).setMaxAccess("readonly").setUnits("MB")
if mibBuilder.loadTexts: memoryMapped.setDescription("provides the amount of mapped memory, in megabytes (MB), by the database")
memoryMappedWithJournal = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 4, 4), Integer32()).setMaxAccess("readonly").setUnits("MB")
if mibBuilder.loadTexts: memoryMappedWithJournal.setDescription("provides the amount of mapped memory, in megabytes (MB), including the memory used for journaling")
connections = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 5))
connectionsCurrent = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsCurrent.setDescription("current # of open connections")
connectionsAvailable = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsAvailable.setDescription("# of available connections")
connectionsTotalCreated = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionsTotalCreated.setDescription("count of all connections created to mongod, including those now closed")
asserts = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 6))
assertRegular = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 6, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assertRegular.setDescription("number of regular assertions")
assertWarning = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 6, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assertWarning.setDescription("number of warnings raised")
assertMsg = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 6, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assertMsg.setDescription("number of message assertions")
assertUser = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 6, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assertUser.setDescription("number of user assertions")
assertRollovers = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assertRollovers.setDescription("number of assertion counter rollovers")
backgroundFlushing = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 7))
flushCount = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 7, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flushCount.setDescription("number of flush operations")
flushTotalMs = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 7, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flushTotalMs.setDescription("total cumulative flush time (ms)")
flushAverageMs = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 7, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flushAverageMs.setDescription("average flush time (ms)")
flushLastMs = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 7, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flushLastMs.setDescription("time spent for last flush (ms)")
flushLastDateTime = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 7, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flushLastDateTime.setDescription("date and time of last flush (UTC)")
cursors = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 8))
cursorTotalOpen = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cursorTotalOpen.setDescription("total # of open cursors")
cursorClientSize = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cursorClientSize.setDescription("# of cursors open by clients")
cursorTimedOut = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 8, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cursorTimedOut.setDescription("# of cursors that have timed out")
dur = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9))
durCommits = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durCommits.setDescription("# of journal commits")
durJournaledMb = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: durJournaledMb.setDescription("data in megabytes (MB) written to journal during the last journal group commit interval")
durWritesToDataFilesMb = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: durWritesToDataFilesMb.setDescription("data in megabytes (MB) written from journal to the data files during the last journal group commit interval")
durCompression = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: durCompression.setDescription("the compression ratio of the data written to the journal")
durCommitsInWriteLock = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durCommitsInWriteLock.setDescription("count of the commits that occurred while a write lock was held")
durEarlyCommits = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durEarlyCommits.setDescription("the number of times MongoDB requested a commit before the scheduled journal group commit interval")
durTimeMs = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 7))
durTimeMsDt = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durTimeMsDt.setDescription("the amount of time (in milliseconds) over which MongoDB collected the timeMS data")
durTimeMsPrepLogBuffer = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durTimeMsPrepLogBuffer.setDescription("the amount of time (in milliseconds) spent preparing to write to the journal")
durTimeMsWriteToJournal = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 7, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durTimeMsWriteToJournal.setDescription("the amount of time (in milliseconds) spent actually writing to the journal")
durTimeMsWriteToDataFiles = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 7, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durTimeMsWriteToDataFiles.setDescription("the amount of time (in milliseconds) spent writing to data files after journaling")
durTimeMsRemapPrivateView = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 9, 7, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: durTimeMsRemapPrivateView.setDescription("the amount of time (in milliseconds) spent remapping copy-on-write memory mapped views")
extraInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 10))
extraInfoNote = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extraInfoNote.setDescription("reports that the data in this structure depend on the underlying platform")
extraInfoHeapUsageBytes = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 10, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extraInfoHeapUsageBytes.setDescription("total size in bytes of heap space used by the database process (Linux Only)")
extraInfoPageFaults = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extraInfoPageFaults.setDescription("total number of page faults that require disk operations")
indexCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 11))
indexCounterAccesses = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 11, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: indexCounterAccesses.setDescription("number of times that operations have accessed indexes")
indexCounterHits = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 11, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: indexCounterHits.setDescription("number of times that an index has been accessed and mongod is able to return the index from memory")
indexCounterMisses = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 11, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: indexCounterMisses.setDescription("number of times that an operation attempted to access an index that was not in memory")
indexCounterResets = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 11, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: indexCounterResets.setDescription("number of times that the index counters have been reset since the database last restarted")
indexCounterMissRatio = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 11, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: indexCounterMissRatio.setDescription("ratio of hits to misses")
network = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 12))
networkBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 12, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkBytesIn.setDescription("amount of network traffic, in bytes, received by this database")
networkBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 12, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkBytesOut.setDescription("amount of network traffic, in bytes, sent by this database")
networkNumRequests = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 12, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkNumRequests.setDescription("total number of distinct requests that the server has received")
writeBacksQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: writeBacksQueued.setDescription("number of writebacks currently queued (mongos only)")
globalLock = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14))
globalLockTotalTime = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockTotalTime.setDescription("time, in microseconds, since the database last started and created the globalLock (roughly server uptime)")
globalLockLockTime = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockLockTime.setDescription("time, in microseconds, since the database last started, that the globalLock has been held")
globalLockCurrentQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 3))
globalLockCurrentQueueTotal = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockCurrentQueueTotal.setDescription("combined total of operations queued waiting for the lock")
globalLockCurrentQueueReaders = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockCurrentQueueReaders.setDescription("number of operations that are currently queued and waiting for the read lock")
globalLockCurrentQueueWriters = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockCurrentQueueWriters.setDescription("number of operations that are currently queued and waiting for the write lock")
globalLockActiveClients = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 4))
globalLockActiveClientsTotal = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockActiveClientsTotal.setDescription("total number of active client connections to the database")
globalLockActiveClientsReaders = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockActiveClientsReaders.setDescription("count of the active client connections performing read operations")
globalLockActiveClientsWriters = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 14, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalLockActiveClientsWriters.setDescription("count of the active client connections performing write operations")
metrics = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15))
metricsDocument = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 1))
metricsDocumentDeleted = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsDocumentDeleted.setDescription("total number of documents deleted")
metricsDocumentInserted = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsDocumentInserted.setDescription("total number of documents inserted")
metricsDocumentReturned = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsDocumentReturned.setDescription("total number of documents returned")
metricsDocumentUpdated = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsDocumentUpdated.setDescription("total number of documents updated")
metricsGetLastError = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 2))
metricsGetLastErrorWtime = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 2, 1))
metricsGetLastErrorWtimeNum = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsGetLastErrorWtimeNum.setDescription("total number of getLastError operations with write concern (i.e. w) greater than 1")
metricsGetLastErrorWtimeTotalMillis = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsGetLastErrorWtimeTotalMillis.setDescription("amount of time in milliseconds that the mongod has spent performing getLastError operations with write concern (i.e. w) greater than 1")
metricsGetLastErrorWtimeouts = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsGetLastErrorWtimeouts.setDescription("number of times that write concern operations have timed out as a result of the wtimeout threshold to getLastError")
metricsOperation = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 3))
metricsOperationFastmod = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsOperationFastmod.setDescription("number of update operations that neither cause documents to grow nor require updates to the index")
metricsOperationIdhack = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsOperationIdhack.setDescription("number of queries that contain the _id field")
metricsOperationScanAndOrder = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsOperationScanAndOrder.setDescription("total number of queries that return sorted numbers that cannot perform the sort operation using an index")
metricsQueryExecutor = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 4))
metricsQueryExecutorScanned = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsQueryExecutorScanned.setDescription("total number of index items scanned during queries and query-plan evaluation")
metricsRecord = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 5))
metricsRecordMoves = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsRecordMoves.setDescription("total number of times documents move within the on-disk representation of the MongoDB data set")
metricsRepl = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6))
metricsReplApply = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 1))
metricsReplApplyBatches = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 1, 1))
metricsReplApplyBatchesNum = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplApplyBatchesNum.setDescription("total number of batches applied across all databases")
metricsReplApplyBatchesTotalMillis = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplApplyBatchesTotalMillis.setDescription("total amount of time the mongod has spent applying operations from the oplog")
metricsReplApplyOps = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplApplyOps.setDescription("total number of oplog operations applied")
metricsReplBuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 2))
metricsReplBufferCount = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplBufferCount.setDescription("current number of operations in the oplog buffer")
metricsReplBufferMaxSizeBytes = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplBufferMaxSizeBytes.setDescription("maximum size of the buffer")
metricsReplBufferSizeBytes = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplBufferSizeBytes.setDescription("current size in bytes of the oplog buffer contents")
metricsReplNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 3))
metricsReplNetworkBytes = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplNetworkBytes.setDescription("total amount of data in bytes read from the replication sync source")
metricsReplNetworkGetmores = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 3, 2))
metricsReplNetworkGetmoresNum = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 3, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplNetworkGetmoresNum.setDescription("total number of getmore operations, which are operations that request an additional set of operations from the replication sync source")
metricsReplNetworkGetmoresTotalMillis = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 3, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplNetworkGetmoresTotalMillis.setDescription("total amount of time required to collect data from getmore operations")
metricsReplNetworkOps = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplNetworkOps.setDescription("total number of operations read from the replication source")
metricsReplNetworkReadersCreated = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplNetworkReadersCreated.setDescription("total number of oplog query processes created")
metricsReplPreload = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 4))
metricsReplPreloadDocs = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 4, 1))
metricsReplPreloadDocsNum = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplPreloadDocsNum.setDescription("total number of documents loaded during the pre-fetch stage of replication")
metricsReplPreloadDocsTotalMillis = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplPreloadDocsTotalMillis.setDescription("total amount of time spent loading documents as part of the pre-fetch stage of replication")
metricsReplPreloadIndexes = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 4, 2))
metricsReplPreloadIndexesNum = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 4, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplPreloadIndexesNum.setDescription("total number of index entries loaded by members before updating documents as part of the pre-fetch stage of replication")
metricsReplPreloadIndexesTotalMillis = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 6, 4, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsReplPreloadIndexesTotalMillis.setDescription("total amount of time spent loading documents as part of the pre-fetch stage of replication")
metricsTtl = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 7))
metricsTtlDeletedDocuments = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 7, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsTtlDeletedDocuments.setDescription("total number of documents deleted from collections with a ttl index")
metricsTtlPasses = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 15, 7, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: metricsTtlPasses.setDescription("number of times the background process removes documents from collections with a ttl index")
repl = MibIdentifier((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 16))
replSetName = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 16, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSetName.setDescription("replica set name")
replSetVersion = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 16, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSetVersion.setDescription("version # of the current replica set configuration")
replIsMaster = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 16, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replIsMaster.setDescription("reflects whether the current node is the master or primary node in the replica set")
replIsSecondary = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 16, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replIsSecondary.setDescription("reflects whether the current node is a secondary node in the replica set")
replPrimary = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 16, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPrimary.setDescription("current primary in the form of hostname:port")
replMe = MibScalar((1, 3, 6, 1, 4, 1, 34601, 1, 1, 1, 2, 1, 16, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: replMe.setDescription("my hostname and port in the form of hostname:port")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("MONGOD-MIB", PYSNMP_MODULE_ID=mongodMIB)

# Objects
mibBuilder.exportSymbols("MONGOD-MIB", mongodbInc=mongodbInc, software=software, mongodb=mongodb, mongod=mongod, mongodMIB=mongodMIB, serverTable=serverTable, serverTableEntry=serverTableEntry, serverName=serverName, system=system, port=port, sysUpTime=sysUpTime, version=version, pid=pid, opcounts=opcounts, globalOpcounts=globalOpcounts, globalOpInsert=globalOpInsert, globalOpQuery=globalOpQuery, globalOpUpdate=globalOpUpdate, globalOpDelete=globalOpDelete, globalOpGetMore=globalOpGetMore, globalOpCommand=globalOpCommand, replOpcounts=replOpcounts, replOpInsert=replOpInsert, replOpQuery=replOpQuery, replOpUpdate=replOpUpdate, replOpDelete=replOpDelete, replOpGetMore=replOpGetMore, replOpCommand=replOpCommand, memory=memory, memoryResident=memoryResident, memoryVirtual=memoryVirtual, memoryMapped=memoryMapped, memoryMappedWithJournal=memoryMappedWithJournal, connections=connections, connectionsCurrent=connectionsCurrent, connectionsAvailable=connectionsAvailable, connectionsTotalCreated=connectionsTotalCreated, asserts=asserts, assertRegular=assertRegular, assertWarning=assertWarning, assertMsg=assertMsg, assertUser=assertUser, assertRollovers=assertRollovers, backgroundFlushing=backgroundFlushing, flushCount=flushCount, flushTotalMs=flushTotalMs, flushAverageMs=flushAverageMs, flushLastMs=flushLastMs, flushLastDateTime=flushLastDateTime, cursors=cursors, cursorTotalOpen=cursorTotalOpen, cursorClientSize=cursorClientSize, cursorTimedOut=cursorTimedOut, dur=dur, durCommits=durCommits, durJournaledMb=durJournaledMb, durWritesToDataFilesMb=durWritesToDataFilesMb, durCompression=durCompression, durCommitsInWriteLock=durCommitsInWriteLock, durEarlyCommits=durEarlyCommits, durTimeMs=durTimeMs, durTimeMsDt=durTimeMsDt, durTimeMsPrepLogBuffer=durTimeMsPrepLogBuffer, durTimeMsWriteToJournal=durTimeMsWriteToJournal, durTimeMsWriteToDataFiles=durTimeMsWriteToDataFiles, durTimeMsRemapPrivateView=durTimeMsRemapPrivateView, extraInfo=extraInfo, extraInfoNote=extraInfoNote, extraInfoHeapUsageBytes=extraInfoHeapUsageBytes, extraInfoPageFaults=extraInfoPageFaults, indexCounters=indexCounters, indexCounterAccesses=indexCounterAccesses, indexCounterHits=indexCounterHits, indexCounterMisses=indexCounterMisses, indexCounterResets=indexCounterResets, indexCounterMissRatio=indexCounterMissRatio, network=network, networkBytesIn=networkBytesIn, networkBytesOut=networkBytesOut, networkNumRequests=networkNumRequests, writeBacksQueued=writeBacksQueued, globalLock=globalLock, globalLockTotalTime=globalLockTotalTime, globalLockLockTime=globalLockLockTime, globalLockCurrentQueue=globalLockCurrentQueue, globalLockCurrentQueueTotal=globalLockCurrentQueueTotal, globalLockCurrentQueueReaders=globalLockCurrentQueueReaders, globalLockCurrentQueueWriters=globalLockCurrentQueueWriters, globalLockActiveClients=globalLockActiveClients, globalLockActiveClientsTotal=globalLockActiveClientsTotal, globalLockActiveClientsReaders=globalLockActiveClientsReaders, globalLockActiveClientsWriters=globalLockActiveClientsWriters, metrics=metrics, metricsDocument=metricsDocument, metricsDocumentDeleted=metricsDocumentDeleted, metricsDocumentInserted=metricsDocumentInserted, metricsDocumentReturned=metricsDocumentReturned, metricsDocumentUpdated=metricsDocumentUpdated, metricsGetLastError=metricsGetLastError, metricsGetLastErrorWtime=metricsGetLastErrorWtime, metricsGetLastErrorWtimeNum=metricsGetLastErrorWtimeNum, metricsGetLastErrorWtimeTotalMillis=metricsGetLastErrorWtimeTotalMillis, metricsGetLastErrorWtimeouts=metricsGetLastErrorWtimeouts, metricsOperation=metricsOperation, metricsOperationFastmod=metricsOperationFastmod, metricsOperationIdhack=metricsOperationIdhack, metricsOperationScanAndOrder=metricsOperationScanAndOrder, metricsQueryExecutor=metricsQueryExecutor, metricsQueryExecutorScanned=metricsQueryExecutorScanned, metricsRecord=metricsRecord, metricsRecordMoves=metricsRecordMoves, metricsRepl=metricsRepl, metricsReplApply=metricsReplApply, metricsReplApplyBatches=metricsReplApplyBatches, metricsReplApplyBatchesNum=metricsReplApplyBatchesNum, metricsReplApplyBatchesTotalMillis=metricsReplApplyBatchesTotalMillis, metricsReplApplyOps=metricsReplApplyOps, metricsReplBuffer=metricsReplBuffer, metricsReplBufferCount=metricsReplBufferCount, metricsReplBufferMaxSizeBytes=metricsReplBufferMaxSizeBytes, metricsReplBufferSizeBytes=metricsReplBufferSizeBytes, metricsReplNetwork=metricsReplNetwork, metricsReplNetworkBytes=metricsReplNetworkBytes, metricsReplNetworkGetmores=metricsReplNetworkGetmores, metricsReplNetworkGetmoresNum=metricsReplNetworkGetmoresNum, metricsReplNetworkGetmoresTotalMillis=metricsReplNetworkGetmoresTotalMillis)
mibBuilder.exportSymbols("MONGOD-MIB", metricsReplNetworkOps=metricsReplNetworkOps, metricsReplNetworkReadersCreated=metricsReplNetworkReadersCreated, metricsReplPreload=metricsReplPreload, metricsReplPreloadDocs=metricsReplPreloadDocs, metricsReplPreloadDocsNum=metricsReplPreloadDocsNum, metricsReplPreloadDocsTotalMillis=metricsReplPreloadDocsTotalMillis, metricsReplPreloadIndexes=metricsReplPreloadIndexes, metricsReplPreloadIndexesNum=metricsReplPreloadIndexesNum, metricsReplPreloadIndexesTotalMillis=metricsReplPreloadIndexesTotalMillis, metricsTtl=metricsTtl, metricsTtlDeletedDocuments=metricsTtlDeletedDocuments, metricsTtlPasses=metricsTtlPasses, repl=repl, replSetName=replSetName, replSetVersion=replSetVersion, replIsMaster=replIsMaster, replIsSecondary=replIsSecondary, replPrimary=replPrimary, replMe=replMe)

