#-----------podstawy----------------------------
# imie = 'Wiktoria'
# ilosc_ksiazek = 10
# srednia = 4.5
#
# print ("Hello " + imie + "!")
# print ("Mam " + str(ilosc_ksiazek) + " lat")
# print ("Srednia: "+ str(srednia))
#----------ZAD 5-----------------------------

# a=1+3
# print(a)
# b=10/3
# print(b)
# c=10.0/3
# print(c)
# d=float(10)/3
# print(d)


#----------ZAD 7 -----------------------------
# marka = 'Pegout'
# ilosc_drzwi = 5
# pojemnosc = 1.3


# marka_upp = marka.upper()

# marka_up = marka.lower()
# print("Samochod " + marka + " ma " + str(ilosc_drzwi))
# print("Marka " + marka_up)
# print("Marka " + marka_upp)
# print("Pojemnosc po zmianach: "+ str(pojemnosc * 2))

# marka ='Peugot'
# m = marka[1:-1]
# print(m)
#
# mn = marka[-1]
# print(mn)
#----------ZAD 8 -----------------------------

# print("Podaj haslo:")
# z = input()
# zz = len(z)
# haslo = (len(z)-2) * "*"


# if zz == 0:
#     print("Haslo puste")
# elif zz < 3:
#     print("**")
# elif zz >= 3:
#     p = z[0]
#     k = z[-1]
#     print(p + haslo + k)


# print ('helo, ' + str(z)) # do cyft
# print ('helo, ' + z) # do liczb

#----------ZAD 9 -----------------------------

# imie = 'Ala'
# zwierze = 'kot'
# print("{0} ma {1}a".format(imie, zwierze))

#----------ZAD 10 -----------------------------
# samochody = ['BMW', 'VW', 'OPEL']
# # print(samochody[0])
# # print(samochody[2])
#
# # for s in samochody:
# #     print(s)
#
# for idx in range(len(samochody)):
#     print("idx: " + str(idx) + " : " + samochody[idx])



#----------ZAD 11 -----------------------------
# samochody = ['BMW', 'VW', 'OPEL', 'SAAB', 'KIA']
# ilosc = [3, 5, 4, 4, 5]
#
# for idx in range( len(samochody)):
#     print("idx: " + str(idx) + " : " + samochody[idx])
     #print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))

#----------ZAD 12 Slownik - uruchom w Pythonie 2 -----------------------------

# samolot = {'name': 'boing',
#             'przebieg': '1000',
#             'type': 'pasazerski'}

# for key, value in samolot.iteritems():
#     print("{0}: {1}".format(key, value))

# for key in samolot:
#     print("{0}: {1}".format(key, samolot[key]))

#----------ZAD 12 cwiczenie -----------------------------

# kontakt = {
#     "Jan": 1,
#     "Ala": 2,
#     "Ela": 3
# }
# for imie, numer in kontakt.iteritems():
#     print "%s ma numer telefonu: %d" % (imie, numer)


#----------ZAD 13 -----------------------------

# def print_dict(d):
#     for key in samolot:
#         print("{0}: {1}".format(key, d[key]))

# if __name__ == "__main__":
#     samolot = {'name': 'boing',
#                 'przebieg': '1000',
#                 'type': 'pasazerski'}


#     print_dict(samolot)
#     print_dict(samolot)

#----------ZAD 14 -----------------------------

# def calucate_vat(netto):
#     vat = float(netto * 23)/100
#     return vat

# if __name__ == "__main__":
#     vat = calucate_vat(1000)
#     print("{0}".format(vat))


#----------ZAD 15 -----------------------------
#
# def main():
#     print ("Tutaj program")
# if __name__ == "__main__":
#     main()

#----------ZAD 3 -----------------------------

# import pprint
#
# def main():
#
#     produkt_1 = {'nazwa': 'mlekovita',
#                 'cena': '10',
#                 'vat': '7',
#                 'jednostka': '5'}
#
#     produkt_2 = {'nazwa': 'ziemniaki',
#                 'cena': '5',
#                 'vat': '23',
#                 'jednostka': '8'}
#
#     produkt_3 = {'nazwa': 'pomidory',
#                 'cena': '12',
#                 'vat': '23',
#                 'jednostka': '18'}
#
#     koszyk = [produkt_1, produkt_2, produkt_2 ]
#
#     # pprint.pprint(koszyk)
#
#     file = open("koszyk.csv", "w")
#     file.write(str(koszyk))
#     file.close()
#
#     #-----odczyt
#     file = open("koszyk.csv", "r")
#     pprint.pprint(file.read())
#
#
# if __name__ == "__main__":
#      main()

#----------ZAD 33-----------------------------
#
# import pprint
#
# def main():
#
#     produkt_1 = {'nazwa': 'mlekovita',
#                 'cena': '10',
#                 'vat': '7',
#                 'jednostka': '5'}
#
#     produkt_2 = {'nazwa': 'ziemniaki',
#                 'cena': '5',
#                 'vat': '23',
#                 'jednostka': '8'}
#
#     produkt_3 = {'nazwa': 'pomidory',
#                 'cena': '12',
#                 'vat': '23',
#                 'jednostka': '18'}
#
#     koszyk = [produkt_1, produkt_2, produkt_3]
#
#     # pprint.pprint(koszyk)
#
#     file = open("koszyk.csv", "w")
#     for poz in koszyk:
#
#         linia = ""
#         for key in ['nazwa', 'cena', 'vat', 'jednostka']:
#             linia += "{0},".format(poz[key])
#         file.write(linia)
#         file.write("\n")
#     file.close()
#
#
#
#     # -----odczyt
#     file = open("koszyk.csv", "r")
#     pprint.pprint(file.read())
#
#
# if __name__ == "__main__":
#      main()


#----------ZAD 333-----------------------------

# import pprint


# def main():
#     koszyk = [
#                     {"nazwa": "ziemniaki","cena": 5, "VAT": 23, "unit": "kg"},
#                     {"nazwa": "jajka","cena": 1, "VAT": 23, "unit": "szt"},
#                     {"nazwa": "marchew","cena": 4, "VAT": 23, "unit": "kg"},
#                     {"nazwa": "pietruszka","cena": 20, "VAT": 23, "unit": "kg"},
#                     {"nazwa": "seler","cena": 9, "VAT": 23, "unit": "kg"}]

#     f = open("koszyk.csv", "w")
#     for poz in koszyk:
#         for pole in ['nazwa', 'cena', 'VAT', 'unit']:
#             f.write("{0},".format(poz[pole]))
#         f.write('\n')
#     f.close()



#     koszyk2 = []
#     print("koszyk2")

#     f2 = open("koszyk.csv", "r")
#     calosc = f2.read()
#     linie = calosc.split('\n')
#     for l in linie:
#         if len(l) > 0:
#             print(l)

# if __name__ == "__main__":
#     main()



#----------ZAD 333m-----------------------------

# import pprint

# def main():
#     koszyk = [
#                     {"nazwa": "ziemniaki","cena": 5, "VAT": 23, "unit": "kg"},
#                     {"nazwa": "jajka","cena": 1, "VAT": 23, "unit": "szt"},
#                     {"nazwa": "marchew","cena": 4, "VAT": 23, "unit": "kg"},
#                     {"nazwa": "pietruszka","cena": 20, "VAT": 23, "unit": "kg"},
#                     {"nazwa": "seler","cena": 9, "VAT": 23, "unit": "kg"}]

#     f = open("koszyk.csv", "w")
#     for poz in koszyk:
#         for pole in ['nazwa', 'cena', 'VAT', 'unit']:
#             f.write("{0},".format(poz[pole]))
#         f.write('\n')
#     f.close()

#     koszyk2 = []
#     print("#### koszyk2")

#     f2 = open("koszyk.csv", "r")
#     calosc = f2.read()
#     linie = calosc.split('\n')
#     for l in linie:
#         produkt = {}
#         if len(l) > 0:
#             pola = l.split(',')
#             produkt['nazwa'] = pola[0]
#             produkt['cena'] = pola[1]
#             koszyk2.append(produkt)

#     pprint.pprint(koszyk2)

# if __name__ == "__main__":
#     main()


#----------ZAD -----------------------------


# for i in range(10):
#     print("Prosze wcisnac litere n lub c")
#     d = input()
#     if (d == "n" or d == "c"):
#         print("Dziekuje!")
#         break
#     else:
#         print("Blad!")

#----------ZAD definowanie funkcji-----------------------------



# def mm():
#     print ('podaj a'); a = input()
#     print ('podaj b'); b = input()
#     if a > b:
#         print(a, ' jest wieksze')
#     elif a == b:
#         print(a, 'jest rowne')
#     elif a < b:
#         print (b, "jest wieksze")
# mm()
    
#----------ZAD -----------------------------
# def mm(x,y):
#     if x > y:
#         return x
#     else:
#         return y

# print (mm(9,4))


#----------ZAD -----------------------------

# a = list(range(1,9))

# print("Moja lisa:",a)
# print("----------------")
# for s in a: #wykorzystuje nowa liste do petli
#    if s==5: # ograniczenie listy do 5
#       break
#    print(s)
#----------ZAD -----------------------------
    
for x in [1, 2, 3]:
    for y in 'abc':
        print (x,y)
# ----------ZAD -----------------------------
# for a in range(6):
#     a = a + 1
#     while a ==5:
#         print("Znalazlm 5!")
#         break
#     print(a)
#----------ZAD -----------------------------
# suma_liczb = 0
# for a in range(5):
#     nowa_wartosc = int(input("Wprowadz dowolna liczbe od 1 do 10:  "))
#     if nowa_wartosc == 5:
#         suma_liczb +=1
# print("Uztkownik wybral",suma_liczb,"razy liczbe 5.")


# suma_liczb = 0

# for a in range(5):
#     wartosc = int(input('Wprowadz liczbe: '))
#     if wartosc == 5:
#         suma_liczb += 1
# print('Uzytkownik wybral', suma_liczb, 'razy 5' )


#----------ZAD -----------------------------
# for a in range(5):
#     print (a)

