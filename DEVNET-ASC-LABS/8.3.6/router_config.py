router_config = """
            <config>
			<native xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-native'>
			<router>
				<ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
					<id>1</id>
					<router-id>1.1.1.1</router-id>
					<network>
						<ip>10.1.1.1</ip>
						<mask>0.0.0.0</mask>
						<area>0</area>
                    </network>
					<network>
						<ip>10.1.2.1</ip>
						<mask>0.0.0.0</mask>
						<area>0</area>
                    </network>
					<network>
						<ip>10.1.3.1</ip>
						<mask>0.0.0.0</mask>
						<area>0</area>
                    </network>
				</ospf>
			</router>
            </native>
            </config>

"""
remove_router_ospf = """
			<config>
				<native xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-native'>
                    <router operation="delete">
					   <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
          				<id>1</id>
					    <router-id>1.1.1.1</router-id>
					    <network>
						 <ip>10.1.1.1</ip>
						 <mask>0.0.0.0</mask>
						 <area>0</area>
                        </network>
					   </ospf>	  					  
					</router>
				</native>
			</config>

"""


