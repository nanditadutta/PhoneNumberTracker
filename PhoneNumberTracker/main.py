import phonenumbers
from test import number

from phonenumbers import geocoder
ch_numer = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_numer,"en"))

from phonenumbers import carrier
service_numer =phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_numer,"en"))
