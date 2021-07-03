import ipaddress

ip = "192.168.0.1"

endereco = ipaddress.ip_address(ip)

ip2 = "192.168.0.0/32"
rede = ipaddress.ip_network(ip2, strict=False)

for ip in rede:
    print(ip)
