import phonenumbers

from phonenumbers import geocoder

phone = input('digite o telefone no formato: +551140028922: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_nunber(phone_number, 'pt'))