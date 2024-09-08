import hashlib
import xml.etree.ElementTree as ET
tree = ET.parse('nmap.xml')
root = tree.getroot()
"""
> Hora de ejecución
> MD5 de archivo xml
> SHA1 de archivo xml
> Cantidad de hosts prendidos
> Cantidad de hosts apagados
> Cantidad de hosts con puerto 22 abierto
> Cantidad de hosts con puerto 53 abierto
> Cantidad de hosts con puerto 80 abierto
> Cantidad de hosts con puerto 443 abierto
> Cantidad de hosts que tienen nombre de dominio          service "domain"
> Servidores HTTP xxxxxxxxxxxxxxxxxxxxxxxxxxx
> Cuántos usan Apache name http y product Apache
> Cuántos honeypots (Dionaea) name honeypot
> Cuántos usan Nginx name http product nginx
""" 
def texto():    
    texFinal=""
    #Hora de ejecución
    horaEjecucion= root.get("startstr")
    texFinal+=horaEjecucion + "\n"
    #MD5 de archivo xml
    arch= open("nmap.xml", "r")
    contenido= arch.read()
    arch.close()
    m = hashlib.md5(contenido.encode())
    texFinal+= m.hexdigest() + "\n"
    #SHA1 
    x = hashlib.sha1(contenido.encode())
    texFinal += x.hexdigest() + "\n"

    host= root.findall("host")
    contadorP= 0 #Host prendidos
    contadorA = 0 #Host apagados
    for i in host:
        if i.find("status").get("state") == "up":
            contadorP+=1
        else:
            contadorA+=1
    texFinal+=  "Cantidad de puertos prendidos: " + str(contadorP ) + "\n"
    texFinal+=  "Cantidad de piertos apagados: " + str(contadorA ) + "\n"

    #Puertos abiertos y otros
    contador22 = 0 
    contador53 = 0
    contador80 = 0
    contador443 = 0
    contadorDom = 0
    contadorApa = 0
    contadorHoney = 0
    contadorNgi = 0

    for i in host:
        if i.find("ports") != None:
            for j in i.find("ports").findall("port"):
                if j.get("portid") == "22":
                    contador22 += 1
                elif j.get("portid") == "53":
                    contador53 += 1
                elif j.get("portid") == "80":
                    contador80 += 1
                elif j.get("portid") == "443":
                    contador443 += 1
                if j.find("service").get("name") == "domain":
                    contadorDom+= 1
                elif j.find("service").get("name") == "honeypot":
                    contadorHoney+= 1
                if j.find("service").get("name") == "http" and j.find("service").get("product") == "Apache httpd":
                    contadorApa+= 1
                elif j.find("service").get("name") == "http" and j.find("service").get("product") == "nginx":
                    contadorNgi+= 1
        else:
            continue
    
    texFinal+=  "Cantidad de puertos 22 abiertos: " + str(contador22 ) + "\n"
    texFinal+=  "Cantidad de piertos 53 abiertos: " + str(contador53 ) + "\n"
    texFinal+=  "Cantidad de puertos 80 abiertos: " + str(contador80) + "\n"
    texFinal+=  "Cantidad de puertos 443 abiertos: " + str(contador443 ) + "\n"
    texFinal+= "Cantidad de puertos dominio: " + str(contadorDom) + "\n"
    texFinal+=  "Cantidad de puertos Apache: " + str(contadorApa ) + "\n"
    texFinal+=  "Cantidad de puertos Honey: " + str(contadorHoney) + "\n"
    texFinal+=  "Cantidad de puertos Nginx: " + str(contadorNgi) + "\n"

    return texFinal

Resul= texto()
print(Resul)

nuevo= open("Tarea 4.txt", "w")
nuevo.write(Resul)
nuevo.close()

#get() obtiene atributos root.get(starstr)
#find() obtiene el primer elemento (hijo) con cierto nombre
#findall() obtiene iterable con todos los elementos que coinciden con una expresión