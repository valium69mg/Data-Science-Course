#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:48:16 2023

Este programa es un scanner de redes 

@author: carlostr
"""

import scapy.all as scapy

def scan(ip):
    #scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    print("IP\t\t\t MAC address\n------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print("-------------------------------------------------------------")
    
scan("192.168.0.1/24")
# Video pausado en:
# 01:24:19
