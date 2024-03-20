#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:49:27 2023

Este programa en un MAC CHANGER, se ejecuta desde la terminal pidiendo 
dos argumentos, la interfaz y la nueva direccion MAC

@author: carlostr
"""
import subprocess
import optparse
import re


#Esta funcion sirve para que el usuario desde la terminal pueda ejecutar el 
#programa y pueda usar las opciones -i, -m y -h

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interfaz para cambiar de direccion MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="Nueva direccion MAC")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor indicar una interfaz, usa -h para mas info")
        
    elif not options.new_mac:
        parser.error("[-] Por favor indicar una direccion MAC, usa -h para mas info")
    return options 
  
 #Esta funcion se encarga de cambiar la direccion mac
def change_mac(interface,new_mac):
    print("[+] Cambiando de Direccion MAC para " + str(interface) + " a " + str(new_mac))
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig", interface,"hw", "ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def mac_address_actual(interface):
    ifconfig_results = subprocess.check_output(["ifconfig", interface], text=True)
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)
    if mac_address_search:
        print("La direccion MAC actual es: {}".format(mac_address_search.group(0)))
    else:
        print("[-] No pudimos leer la direccion MAC")

#Guardamos las opciones que nos dio el usuario como variables
options = get_arguments() 
interface = options.interface
new_mac = options.new_mac
#Cambiamos la mac actual por la proporcionada por el usuario
change_mac(interface,new_mac)
#Le mostramos al usuario el MAC actual 
mac_address_actual(interface)





