Boundary MongoDB Enterprise Plugin
==================================

The Boundary MongoDB Enterprise plugin collects information on MongoDB.
**Only [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise) is supported.**

The plugin requires MongoDB to have SNMP monitoring enabled, and an SNMP agent listening on a UDP socket accessible
to the plugin.  See [this article](http://docs.mongodb.org/manual/tutorial/monitor-with-snmp/) for instructions
on how to set up SNMP monitoring of MongoDB. 

The plugin requires Python 2.6 or later.

## Metrics

The information collected is a subset of the MongoDB MIB, which is contained in `MONGOD-MIB.txt` in the MongoDB
Enterprise package.

## Adding the MongoDB Plugin to Premium Boundary

1. Login into Boundary Premium
2. Display the settings dialog by clicking on the _settings icon_: ![](src/main/resources/settings_icon.png)
3. Click on the _Plugins_ in the settings dialog.
4. Locate the _mongodb_ plugin item and click on the _Install_ button.
5. A confirmation dialog is displayed indicating the plugin was installed successfully, along with the metrics and the dashboards.
6. Click on the _OK_ button to dismiss the dialog.

## Removing the MongoDB Plugin from Premium Boundary

1. Login into Boundary Premium
2. Display the settings dialog by clicking on the _settings icon_: ![](src/main/resources/settings_icon.png)
3. Click on the _Plugins_ in the settings dialog which lists the installed plugins.
4. Locate the _mongodb_ plugin and click on the item, which then displays the uninstall dialog.
5. Click on the _Uninstall_ button which displays a confirmation dialog along with the details on what metrics and dashboards will be removed.
6. Click on the _Uninstall_ button to perfom the actual uninstall and then click on the _Close_ button to dismiss the dialog.

## Configuration

Before the plugin will collect data, you must configure the details of an SNMP agent to query on the Relays
tab.

General operations for plugins are described in [this article](http://premium-support.boundary.com/customer/portal/articles/1635550-plugins---how-to).
