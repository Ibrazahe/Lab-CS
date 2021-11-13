# Práctica-03 del laboratorio que es consumir 1 API 5 veces, 2 peticiones basadas en peticiones pasadas #
# IBRAHIM ZAVALA HERNANDEZ 

import shodan
import requests

# API de Shodan

api=input("API key: ")
shodan= shodan.Shodan(api)
buscar= input("Término a buscar: ")

try:
        results = shodan.search(buscar)
        print('Total de resultados: %s' % results['total'])

        for i in results['matches']:
                print('IP: %s' % i['ip'])
                print('Puerto: %s' % i['port'])
                print('Hostnames: %s' % i['hostnames'])
                print('-----------'*5)


except Exception as e:
        print('Ups! Ha ocurrido un error: %s' % e)


r = requests.get('https://github.com/timeline.json')
print(r)

g = requests. get('http://google.com')
g.history

g.url