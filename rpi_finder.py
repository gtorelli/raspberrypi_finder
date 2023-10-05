# Script para localizar uma placa Raspberry Pi na rede local
# Funciona com uma lista de endereços MAC do Raspberry Pi
# Autor: Gabriel Torelli
# Data 04/10/2023

# Requisitos para rodar em Windows
# 1) Instalar o python-nmap
# pip3 install python-nmap

# 2) Instalar o pacote npcap (nmap)
# https://npcap.org

# 3) Instalar o gawk, grep utilizando o Scoop (https://scoop.sh/)
# scoop install gawk grep

# Como executar? python rpi_finder.py 192.168.1.1/24

import subprocess
import sys

rpi_list = []

def find_devices_with_mac_prefixes(ip_range, mac_prefixes):
    for mac in mac_prefixes:
        cmd = f'''nmap -sn {ip_range} | grep -B 2 {mac} | grep "Nmap scan report" '''
        cmd_run = subprocess.getoutput(cmd)
        rpi_list.append(cmd_run)
        filtered_list = [item for item in rpi_list if item != '']
        result_string = '\n'.join(map(str, filtered_list))
    return result_string


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rpi_finder.py <IP range>. Example: python rpi_finder.py 192.168.1.1/24")
        sys.exit(1)

ip_range = sys.argv[1]
raspberry_mac_prefixes = ["28:CD:C1", "B8:27:EB", "D8:3A:DD", "DC:A6:32", "E4:5F:01"]

devices = find_devices_with_mac_prefixes(ip_range, raspberry_mac_prefixes)
print(devices)



