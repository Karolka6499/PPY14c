import math

print("--1--")
podlogaDlugosc = int(input("Jaka jest dlugosc podlogi ? :"))
podlogaSzerokosc = int(input("Jaka jest szerokosc podlogi ? :"))

panelDlugosc = int(input("Jaka jest dlugosc panela ? :"))
panelSzerokosc = int(input("Jaka jest szerokosc panela ? :"))

paneleWopak = int(input("Jaka jest ilosc paneli w opakowaniu? :"))

def ilePotrzeba(podlogaDl,podlogaSzer,panelDl,panelSzer,ilePaneli) :
    powPomieszczenia = podlogaDl * podlogaSzer
    powPanela = panelDl * panelSzer
    ilePotrzebne = powPomieszczenia / powPanela
    ileOpak = math.ceil(ilePotrzebne/ilePaneli)
    return ileOpak
print(ilePotrzeba(podlogaDlugosc,podlogaSzerokosc,panelDlugosc,
                  panelSzerokosc,paneleWopak))


print("--2--")

liczbyDoSpr = input("Podaj liczby do sprawdzenia, niech beda oddzielone jedna spaca : ").split(" ")
#print(liczbyDoSpr)

def czyPierwsza(doSpr) :
    liczby = []
    pierwsza = []

    for i in doSpr :
        liczby.append(int(i))
    for i in range(max(liczby) + 1) :
        pierwsza.append(True)
    pierwsza[0] = False
    pierwsza[1] = False

    for i in range(len(pierwsza)) :
        if pierwsza[i] :
            kwadrat = i * i
            while kwadrat < len(pierwsza) :
                pierwsza[kwadrat] = False
                kwadrat = kwadrat + i

    for i in liczby :
        print("{0} --> {1}".format(str(i), str(pierwsza[i])))

czyPierwsza(liczbyDoSpr)

print("--3--")

napis = input("Podaj tekst do zaszyfrowania : ").upper()
szyfr = input("Podaj szyfr :").upper()
opcjaAlf = input("Czy chcesz podać własny alfabet ?  n(nie) lub t(tak) :")
alfabet = []
alf = ""

def podajAlf():
    alf = input("Podaj litery alfabetu, rozdzielone spacją").upper().split(" ")
    for i in szyfr :
        if alf.count(i) == 0 :
            print("ERROR -> Znaki w SZYFR nie znajduja sie w alfabecie")
            return podajAlf()
    print("CORRECT -> Znaki z SZYFR znajduja sie w alfabecie ")
    return alf


def brakAlf (b,alf):
    index = 0
    a = ""
    if alf == "" :
        alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W', 'X', 'Y', 'Z']
    for i in b :
        if alf.count(i) == 0 :
            a = a + i
        else :
            i = alf.index(i) +(alf.index(szyfr[index % len(szyfr)]))
            index = index + 1
            a = a + alf[i % len(alf)]
    return a

if

