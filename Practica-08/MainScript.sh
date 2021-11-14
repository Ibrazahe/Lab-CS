# Practica-03 Ibrahim Zavala Hernandez
clear
echo '[+] ENVIO DE CORREOS'
echo '[+] Informacion del Emisor'
echo 'Introduce el Correo Electronico: '
read -p 'Email: ' transmitter
echo ''
echo 'Introduce la Contraseña del Correo: '
read -p 'Contraseña: ' password
echo ''
echo '--- Informacion del Mensaje ---'
echo 'Asunto: '
read -p 'Asunto: ' subject
echo ''
echo 'Mensaje: '
read -p 'Mensaje: ' message

while IFS= read -r line
do
    echo ''
    echo $line
    python Envio_Correos.py --transmitter "$transmitter" --password "$password" --receiver "$line" --subject "$subject" --message "$message"
done < correos.txt