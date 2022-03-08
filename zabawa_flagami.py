import requests 

link = "http://zajecia-programowania-xd.pl/flagi"
flagi_response = requests.get(link)
flagi_tekst = flagi_response.text
print(flagi_tekst)

flagi = flagi_tekst.split("</p>")
for f in flagi:
	f = f[
	print(f)

#lista = [1 ,2 ,3]

#for i in lista:
#	print(i)

t
