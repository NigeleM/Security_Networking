
import ipaddress
def ipParser(iplist):
    iplist = sorted(iplist)
    newStr = ''
    head = ''
    nextip = ''
    ipNewset = []
    for ip in iplist:
        if head == '':
            head = ipaddress.ip_address(ip)
        elif head != '':
            nextip = ipaddress.ip_address(ip) - 1
            if head == nextip:
                ipNewset.append(head)
                ipNewset.append(nextip+1)
                head = nextip + 1
            else:
                if len(ipNewset) == 0:
                    newStr += f'{head},'
                    head = nextip + 1
                elif len(ipNewset) == 1:
                    newStr += f'{head},'
                    head = nextip + 1
                elif len(ipNewset) > 1:
                    newStr += f'{ipNewset[0]}-{ipNewset[len(ipNewset)-1]},'
                    ipNewset.clear()
                    head = nextip + 1
    if len(ipNewset) == 0:
        newStr += f'{head},'
    elif len(ipNewset) == 1:
        newStr += f'{ipNewset[0]},'
    elif len(ipNewset) > 1:
        newStr += f'{ipNewset[0]}-{ipNewset[len(ipNewset)-1]},'
        ipNewset.clear()
    return newStr

iplist = ['1.1.1.1','1.1.1.3','1.1.1.5','1.1.1.7','1.1.1.9']
print(ipParser(iplist))
    
        
                    
            
