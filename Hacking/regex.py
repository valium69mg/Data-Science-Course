#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:34:22 2023

Este codigo explica como  extraer un texto con herramientas regex 
usando la libreria re

@author: carlostr
"""


import re

message = "eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500 ether \
        12:22:33:44:55:66  txqueuelen 1000  (Ethernet) \
        RX packets 0  bytes 0 (0.0 B) RX errors 0  dropped 0 \
        overruns 0  frame 0 TX packets 0  bytes 0 (0.0 B)\
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\
        device interrupt 16  memory 0xdff00000-dff20000"
  
mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", message)

print(mac_address_search)
