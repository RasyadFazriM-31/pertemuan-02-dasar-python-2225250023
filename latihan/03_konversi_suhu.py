# Latihan 3 - Konversi Suhu (Celsius ke Fahrenheit dan Kelvin)
# Nama    : Rasyad Fazri Mulyono
# NIM     : 2225250023
# Kelas   : 3A

KELVIN_OFFSET = 273.15

celsius = float(input("Suhu (Celsius): "))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print(f"Celsius    = {celsius:.2f} C")
print(f"Fahrenheit = {fahrenheit:.2f} F")
print(f"Kelvin     = {kelvin:.2f} K")
