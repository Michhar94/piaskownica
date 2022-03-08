dzien = "Sroda"
dzisiaj = "Sroda"

dni_pracujace = [
	"Poniedzialek",
	"Wtorek",
	"Sroda",
	"Czwartek",
	"Piatek",
]
weekend = [
	"Sobota",
	"Niedziela",
]
print(dni_pracujace)
print(weekend)
print()

#if dzien == dzisiaj:
#	print("Tak dzisiaj jest  sroda")

if dzien in dni_pracujace:
	print("Dzisiaj jest dzien pracujacy")
elif dzien in weekend:
	print("Dzisiaj jest weekend")
else:
	print("Zle napisales dzien tygodnia")
