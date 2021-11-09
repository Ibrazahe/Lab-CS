### Práctica 6 Nmap ###
# Ibrahim Zavala Hernandez 

echo "nmap a IP pública"
nmap 189.153.0.220

echo "IP de segmento de red"
nmap -sP 172.17.88.196 

echo "nmap a segmento de red"
nmap 172.17.88.196