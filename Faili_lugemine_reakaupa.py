f = open('andmed.txt')

nimi = f.readline().strip()
vanus = f.readline().strip()
aadress = f.readline().strip()

print("Nimi:", nimi)
print("Vanus:", vanus, "aastat")
print("Aadress:", aadress)

f.close()


