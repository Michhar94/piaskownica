import   requests


url ="https://zajecia-programowania-xd.pl/flagi"
#print(url)
#print(type(url))

surowe_info = requests.get(url)
text = surowe_info.text
#print(text)

#Cel
#Lista znakow
linki = []
efekt = text.split("</p>")
for linia in efekt:
        link = linia.replace("<p>", "")
        link = link.replace("- ", "")
        link = link.strip()
        if " " in link or "<" in link:
            continue
        linki.append( link)
#        print(link)
#for l in linki:
#    print(l)
domeny_pl = 0
domeny_com = 0
domeny_x = 0
wszystkie_kropki = 0
for i, link in enumerate(linki):
    if "pl" in link:
        domeny_pl += 1
    if  "com" in link:
        domeny_com +=1
    if ".pl" in link and ".com" in link:
        domeny_x +=1

    n_kropek = link.count(".")
    wszystkie_kropki +=n_kropek

print(domeny_pl)
print(domeny_com)
print(domeny_x) 
print(wszystkie_kropki)
print(link.count("-"))