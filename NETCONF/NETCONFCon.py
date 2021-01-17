from ncclient import manager
import xml.dom.minidom


if __name__ == '__main__':
    m= manager.connect(host="172.16.98.132",
                      port=830,
                      username='cisco',
                      password="cisco123!",
                      hostkey_verify=False)
##for csr1_capability in m.server_capabilities:
##        print(csr1_capability)

netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>CSR1kv</hostname>
  </native>
</config>
"""
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>Sage IT Mi loopback</description>
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
netconf_newloop = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>2</name>
    <description>My second NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.2.3</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""



### Imprimir sin filtro
#netconf_reply = m.get_config("running")
#print(netconf_reply)
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

### Imprimir con filtros
#netconf_reply = m.get_config(source="running", filter=netconf_filter)
#print(netconf_reply)
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#Editar configuracion usando edit_config y cambiar el hostname
#netconf_reply = m.edit_config(target="running", config=netconf_hostname)
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#Editar configuracion y agregar loopback1
#netconf_reply = m.edit_config(target="running", config=netconf_loopback)
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#Editar configuracion y agregar loopback1 con misma IP que Loopback1
#netconf_reply = m.edit_config(target="running", config=netconf_newloop)
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


