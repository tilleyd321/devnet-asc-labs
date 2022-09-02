from ncclient import manager
import xml.dom.minidom
import router_config
import xmltodict

router = {"host": "192.168.56.103",
          "port": "830", "username":"cisco",
          "password":"cisco123"}


if __name__ == '__main__':
    with manager.connect(host=router["host"],
                         port=router["port"],
                         username=router["username"],
                         password=router["password"],
                         hostkey_verify=False) as m:

        # Get Configuration and State Info for Interface
        print("Connected")

#       this adds to the router config

        netconf_reply = m.edit_config(target="running", config=router_config.router_config)
        if (netconf_reply.ok):
            print("Success: Added OSPF config")

        netconf_reply = m.get_config(source='running')

        if (netconf_reply.ok):
            print("Succcess: Read Config")
        with open ("running-config.xml", "w") as f:
            f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

        run_config = xmltodict.parse(netconf_reply.xml)
        run_data   = run_config['rpc-reply']['data']['native']

        routing_info = run_data['router']['ospf']
        #print (routing_info.keys())
        
        ospf_id = run_data['router']['ospf']['id']
        ospf_network = run_data['router']['ospf']['network']
        ospf_router_id = run_data['router']['ospf']['router-id']
   
        print("*********{}**************".format("OSPF Router Config"))
   
        print("ospf_id is:{} ospf_router-id is: {}".format(ospf_id,
                                                           ospf_router_id))
        for i in ospf_network:
            print('ip {} mask {} area {}'.format(i['ip'], i['mask'], i['area']))

        print("*********{}**************".format("END"))
       #print("ospf_network is: {}".format(ospf_network))


        netconf_reply = m.edit_config(target="running", config=router_config.remove_router_ospf)

        if (netconf_reply.ok):
            print("Success: OSPF is removed")