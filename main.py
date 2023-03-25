import requests
API_KEY = '7016bb9e277d77e9a9c36da9937c153e'

# Pide al usuario que ingrese una dirección IP

print('Valhalla Tool')
print(' ')
print(' ')
ip_address = input('Ingresa una dirección IP: ')

# Utiliza la API de geolocalización para obtener la información de ubicación
response = requests.get('http://api.ipstack.com/' + ip_address + '?access_key=' + API_KEY)
json_response = response.json()


# Imprime la información de la ip con la ip de IPSTACK
print('Información de ubicación para la dirección IP:', ip_address)
print('IPSTACK: ')
print('País:', json_response['country_name'])
print('Ciudad:', json_response['city'])
print('Región:', json_response['region_name'])
print('Código Postal:', json_response['zip'])
print('Latitud:', json_response['latitude'])
print('Longitud:', json_response['longitude'])
print(' ')
print('Informacion del proveedor de internet: ')
print(' ')
print(' ')
input("Presiona Enter para salir...")