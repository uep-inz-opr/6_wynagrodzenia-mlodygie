

class Pracownik:
    def __init__(self, imie, wynagrodzenie):
        self.imie = str(imie)
        self.wynagrodzenie = int(wynagrodzenie)
    
    def __repr__(self):
        return f"{self.imie} {self.wynagrodzenie}"
    
    def __wynagrodzenie_netto__(self):
       a = round(round(self.wynagrodzenie * 0.0976,2) + round(self.wynagrodzenie * 0.015,2) + round(self.wynagrodzenie * 0.0245,2), 2)
       b = round(self.wynagrodzenie-a,2)
       c = round(b*0.09, 2)
       e = round(b*0.0775, 2)
       f = round(111.25, 2)
       g = round(self.wynagrodzenie - f - a, 2)
       h = round(g, 0)
       i = round(((h)*0.18)-46.33,2)
       j = round(i-e, 2)
       k = round(j, 0)
       self.wynagrodzenienetto = round((self.wynagrodzenie - a - c - k), 2)
       return round(self.wynagrodzenienetto, 2)
    
    def __obliczanie_skladki__(self):
        self.skladki = round(self.wynagrodzenie *0.0976, 2) + round(self.wynagrodzenie*0.065, 2) + round(self.wynagrodzenie*0.0193,2) + round(self.wynagrodzenie*0.0245,2) + round(self.wynagrodzenie*0.001,2)
        return round(self.skladki,2)

    def __koszt__(self):
        self.koszt = round(self.wynagrodzenie + self.skladki, 2)
        return self.koszt
    def __razem__(self):
        return round(self.wynagrodzenie + self.__obliczanie_skladki__(),2)      

wszyscy_pracownicy = int(input())
pracownicy = []
for n in range(wszyscy_pracownicy):
    imie_wynagrodzenie = input().split()
    imie = imie_wynagrodzenie[0]
    wynagrodzenie = imie_wynagrodzenie[1]
    pracownik_obj = Pracownik(imie, wynagrodzenie)
    pracownicy.append(pracownik_obj)

laczny_koszt_pracodawcy = 0 

for m in range(wszyscy_pracownicy):
    laczny_koszt_pracodawcy += pracownicy[m].__razem__()
    imie = pracownicy[m].imie
    wynagrodzenie = pracownicy[m].wynagrodzenie
    print(imie, f"{pracownicy[m].__wynagrodzenie_netto__():.2f}", f"{pracownicy[m].__obliczanie_skladki__():.2f}", f"{pracownicy[m].__koszt__():.2f}")

print(laczny_koszt_pracodawcy)



