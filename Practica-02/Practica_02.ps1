# Ibrahim Zavala Hernandez
# Script con una variable, if, ciclo y función con parametro
$servicios = Get-Service
Write-Host $servicios.GetType().Name 

foreach($elemento in $servicios){
    Write-Host $elemento.Name "-->" $elemento.status 
}

#for($i = 0; $i -lt $servicios.Length; $i++){
#    Write-Host $servicios[$i].Name "-->" $servicios[$i].status
#}
