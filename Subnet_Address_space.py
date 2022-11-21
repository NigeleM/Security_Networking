
# Code for address 
stIp = ipaddress.IPv6Address(startIp)
edIp = ipaddress.IPv6Address(endIp)
ip = [ipaddr for ipaddr in ipaddress.summarize_address_range(stIp, edIp)]

# Code for IP generator
start_ip = ipaddress.IPv4Address(ipcontent[2])
end_ip = ipaddress.IPv4Address(ipcontent[3])
for ip_int in range(int(start_ip), int(end_ip)):
      print(ipaddress.IPv4Address(ip_int))
      
print(ipaddress.IPv4Address(end_ip))
                    
