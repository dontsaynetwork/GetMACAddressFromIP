from scapy.all import *

print("")
print("SENDING PACKET TO GET MAC ADDRESS")


target_ip = input('Please enter the IP to get the MAC address') # The script will pause and wait for the user to enter the target IP for which s/he wants to get the MAC address for

arprequest = ARP(pdst=target_ip) #Creating an ARP request to be sent with the target_ip as argument
broadcast = Ether(dst='ff:ff:ff:ff:ff:ff') #The ff:ff:ff:ff:ff:ff is the broadcast address which will send the ARP request to every connected device

final_packet = broadcast / arprequest #Finalising the construction of the packet to be sent

response = srp(final_packet, timeout=2, verbose=True)[0] #Sending the packet and storing the response in the response variable

print("")
print(f'THE MAC ADDRESS OF {target_ip}')
print (response[0][1].hwsrc) #Printing the response by using the hwrsc
