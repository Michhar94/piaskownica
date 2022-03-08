import requests

def policz_znaki(string):
	dlugosc_stringu = len(string)
	return dlugosc_stringu

link = "https://zajecia-programowania-xd.pl/kubus_puchatek"
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

link_b = link[0]
print()
print(link)
print(link_b)
print()
