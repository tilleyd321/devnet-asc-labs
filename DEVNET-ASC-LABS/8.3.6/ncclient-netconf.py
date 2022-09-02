from ncclient import manager
import xml.dom.minidom

router = {"host": "192.168.56.103",
          "port": "830", "username":"cisco",
          "password":"cisco123"}


if __name__ == '__main__':
    with manager.connect(host=router["host"],
                         port=router["port"],
                         username=router["username"],
                         password=router["password"],
                         hostkey_verify=False) as m:

        netconf_filter = """
<filter>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
        netconf_hostname = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<hostname>NEWHOSTNAME</hostname>
</native>
</config>
"""
        netconf_loopback = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface>
<Loopback>
<name>1</name>
<description>My first NETCONF loopback</description>
<ip>
<address>
<primary>
<address>10.1.1.1</address>
<mask>255.255.255.0</mask>
</primary>
</address>
</ip>
</Loopback>
</interface>
</native>
</config>
"""
        netconf_loopback2 = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface>
<Loopback>
<name>2</name>
<description>My first NETCONF loopback</description>
<ip>
<address>
<primary>
<address>10.1.1.1</address>
<mask>255.255.255.0</mask>
</primary>
</address>
</ip>
</Loopback>
</interface>
</native>
</config>
"""
        # Get Configuration and State Info for Interface
        print("Connected")
        netconf_reply = m.get_config(source='running', filter=netconf_filter)
        #print (netconf_reply)

        with open ("running-config.xml", "w") as f:
            f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

        netconf_reply = m.edit_config(target="running", config=netconf_hostname)
        if (netconf_reply.ok == True):
         print ("Success: Edit hostname")
        #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
        netconf_reply = m.edit_config(target="running", config=netconf_loopback)
        if (netconf_reply.ok == True):
         print ("Success: Edit loopback")
        else:
         print ("Fail: Edit loopback")
        #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
        #netconf_reply = m.edit_config(target="running", config=netconf_loopback2)
        #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
