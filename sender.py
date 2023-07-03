from scapy.all import *

print("")
print("SENDING PACKET TO GET MAC ADDRESS")


target_ip = input('Please enter the IP to get the MAC address')

arprequest = ARP(pdst=target_ip)
broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')

final_packet = broadcast / arprequest

response = srp(final_packet, timeout=2, verbose=True)[0]

print("")
print(f'THE MAC ADDRESS OF {target_ip}')
print (response[0][1].hwsrc)
