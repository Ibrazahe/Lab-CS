# Ibrahim Zavala Hernandez 
# Script de practica 2
# Algebra lineal, vectores de manera sencilla 

# Variables
$n= read-Host -prompt "¿Cuántos vectores son? " 
$m= read-Host -prompt "¿A que está elevado R? " 
#ciclo
while ($n -le 0)
    {
    $n= read-Host -prompt "No es una cantidad válida de vectores, da una nueva"
    }
    
while ($m -le 0)
    {
    $m= read-Host -prompt "No es una cantidad válida de para R, da una nueva"
    }

#funcion con parametros e if
function validador {
    [CmdletBinding()] param([Parameter()] [string] $msg="Dependiente")
    if ($n -gt $m){
    Write-Host "En este caso es linealmente " $msg
    }else{
    Write-Host "En este caso NO es linealmente " $msg
    }
    }

validador 