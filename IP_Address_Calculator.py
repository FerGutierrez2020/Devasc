import ipaddress

##Programa en Python para ejemplificar el uso de Condicionales, loops
##Input, Output y el uso de librerias/paquetes existentes.

dir_ip=input('Introduzca la direccion IP y prefijo con formato x.x.x.0/x: ')
ip=ipaddress.IPv4Network(dir_ip)
print('La mascara de subred es: ',ip.netmask)
print('La mascara wilcard es: ',ip.hostmask)
print('La primer ip usable es: ',ip.network_address+1)
print('La ultima ip usable es: ',ip.network_address-1)
print('Es una direccion IP privada: ',ip.is_private)
print('Total de IPs usables: ',ip.num_addresses-2)
pregunta=input('Quieres conocer cuales son las IP validas?: ')
if pregunta=='si' or pregunta=='SI' or pregunta=='Si':
    for h in ip.hosts():
        print(h)
elif pregunta=='no' or pregunta=='NO' or pregunta=='No':
 print('Buen dia, bye\nAtte:SAGE IT')