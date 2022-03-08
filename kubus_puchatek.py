import requests	

link = "https://zajecia-programowania-xd.pl/kubus_puchatek"
kubus_raw = requests.get(link)

#kubus_status = kubus_raw_status_code

kubus_text = kubus_raw.text

kubus_linie_b = kubus_text.split("</p>")

start = 100
end = 400

#czyszczenie
kubus_linie = []
for l in kubus_linie_b:
#	print("surowe l", l)
	l = l.replace("<p>", " ")
	l = l.strip()
	kubus_linie.append(l)
#	print("l po replace", l)

#wyswietlanie

bohater = "Skin man"
bohater_2 = "Skeleton man"
bohater_3 = "Aniki"

for i, l in enumerate(kubus_linie):
	if i >= start and i < end:
		l = l.replace("Kubuś", bohater)
		l = l.replace("Puchatek",bohater)
		l = l.replace("Królik", bohater_2)
		l = l.replace("Prosiaczek", bohater_3)
		l = "<p>" + l + "</p>"
		print(l)
# for l in kubus_linie:
#	print(l)
#print(kubus_text)

#print ( len( kubus_linie) )
