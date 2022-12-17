
import ipaddress
# Code for address 
startIp = int("Enter starting IP: ")
endIp = int("Enter ending IP: ")
stIp = ipaddress.IPv6Address(startIp)
edIp = ipaddress.IPv6Address(endIp)
ip = [ipaddr for ipaddr in ipaddress.summarize_address_range(stIp, edIp)]

# Code for IP generator
startIp = int("Enter starting IP: ")
endIp = int("Enter ending IP: ")
# can also put logic in a loop for files
start_ip = ipaddress.IPv4Address(startIp)
end_ip = ipaddress.IPv4Address(endIp)
for ip_int in range(int(start_ip), int(end_ip)):
      print(ipaddress.IPv4Address(ip_int))
      
print(ipaddress.IPv4Address(end_ip))
                    
