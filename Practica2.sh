# !/bin/bash
# Ibrahim Zavala Hernandez
# Script de la practica 2 de LPCS
# Script que hace la suma desde 1 hasta el numero dado'

#GAUSS
function Gauss
{
	gauss1=` expr $n + 1 `
	gauss2=` expr $gauss1 \* $n `
	gauss=` expr $gauss2 / 2 `
	echo $gauss
}

read -p "Ingresa un numero: " n

while [ $n -le 0 ];
do
read -p "El número con que desea trabajar no es válido, dé uno nuevo: " n
done
Gauss

read -p "Desea agregar otro número [1] SI [2] NO: " opc
if [ $opc -eq 1 ];
then
	read -p "Ingresa el otro número: " n
while [ $n -le 0 ];
do
	read -p "No es un número válido, dé uno nuevo: " n
done
Gauss
else
	echo "FIN"
fi




