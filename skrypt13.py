
class Czlowiek:
    iloscOczu = 2
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

And = Czlowiek("Andrzej", 22)
Ann = Czlowiek("Anna", 17)

print(And.iloscOczu)
print(Ann.wiek)

#-------------------------------
def dodawanie(x,y):
    return x+y

dod = lambda x,y: x+y
#print(dodawanie(2,3))
#print(dod(2,3))