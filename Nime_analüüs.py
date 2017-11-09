nimi = input("Sisesta oma nimi: ").lower()
arv0= nimi.count('g')
arv1 = nimi.count('b')
arv2 = nimi.count('d')
arv3 = nimi.count('k')
arv4 = nimi.count('p')
arv5 = nimi.count('t')
arv = arv0 + arv1 + arv2 + arv3 + arv4 + arv5
print("Sulghäälikuid kokku " + str(arv) + " tükki.")
