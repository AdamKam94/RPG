import time
import random

#   NarratorText1 - Chapter 1, Text 1 
#   To są tekstty narratora
NarratorText1 = """Witaj ponownie"""
NarratorText2 = """[Narrator]: Idziesz opuszczoną drogą, w jednej ręce trzymasz zakrwawiony sztylet, a drugiej nie masz. 
W pewnym momencie zauważasz samotną kobietę siedzącą na pniaku przy drodze. Co robisz?"""


#   Chapter 1, Choice 1
#   To są teksty wyboru
Question1 = """[1] pytasz kim jest i co tu robi (łatwy)
[2] atakujesz (średni)
[3] czytasz jej w myślach (trudny
Co wybierasz?: """
#   To są teksty odpowiedzi
Answer1_1A = """[Narrator]: Kobieta patrzy na Ciebie z przestrachem, z trudem próbując ukryć drżenie rąk, odpowiada:
[Kobieta]: zbieram grzybu na maść przeciwko mrowieniu rąk, ale zrobiłam sobie rzerwę wsłuchuję się w odgłosy lasu,
jestem zielarką z wioski nieopodal, zgubiłeś się?
"""
Answer1_1B = """[Narrator]: Kobieta z przestrachem na CIebie patrzy i ucieka. Z braku wyboru idziesz ścieżką dalej mając nadzieję ze gdzieś dotrzesz"""
Answer1_2A = """[Narrator]: Sprawną ręką zręcznie wbijasz jej sztylet w żebro, kobieta padda martwa na ziemie.
W kieszeni miała list, otwierasz go i czytasz:
'B ma nie dowiedzieć się kim jesteś, 
podążaj za nim, 
ma bezpieczny dotrzeć do miasta
Niebieski kwiat i kolce'
"""
Answer1_2B = """[Narrator]: Bierzesz zamach by ciąć sztyletem kobietę lecz poślizgasz się i upadasz na niego raniąc się w brzuch.
Kobieta widząc to podbiega do Ciebie i krzyczy:
[Kobieta]: nie ruszaj się, jestem zielarką, opatrzę Ci rany.
Ciemnieje Ci w oczach i odpływasz 
"""
Answer1_3A = """[Narrator]: Skupiasz się i wytężasz siły, odnajdujesz  moce których dawno nie czułeś. 
Patrzysz na kobietę, a granica między światem psychicznym i fizycznym pęka. Zaczynasz słyszeć jej myśli:
[Kobieta]: 'w końcu idzie, myślałam że będzie wyższy, czemu kurwa nie ma jednej ręki, co to krew na jego rękach.' 
[Kobieta]: 'Skup się, cokolwiek się będzie działo ma cały dotrzeć do Bernarda, co on się tak gapi?'
[Kobieta]: Hej wędrowcze, nie zgubiłeś się?
"""

# Tutaj są moduły

EndNumberLooptext = "To już jest koniec, bywaj"
ContinueLoopNumberText = """Cóżże wpisujesz, dej liczbe,
podaj odpowiedź jeszcze raz: """
#   M1 - moduł sprawdzający wybór przy 1 opcji
def M1(SelectedNumber):
    counter = 0
    while SelectedNumber not in ["1"]:
        if counter < 4:
            counter = counter + 1
            SelectedNumber = input(ContinueLoopNumberText)
        else:
            print(EndNumberLooptext) 
            break
    return SelectedNumber
#   M2 - moduł sprawdzający wybór przy 2 opcjach
def M2(SelectedNumber):
    counter = 0
    while SelectedNumber not in ["1", "2"]:
        if counter < 4:
            counter = counter + 1
            SelectedNumber = input(ContinueLoopNumberText)
        else:
            print(EndNumberLooptext) 
            break
    return SelectedNumber
#   M3 - moduł sprawdzający wybór przy 3 opcjach
def M3(SelectedNumber):
    counter = 0
    while SelectedNumber not in ["1","2","3"]:
        if counter < 4:
            counter = counter + 1
            SelectedNumber = input(ContinueLoopNumberText)
        else:
            print(EndNumberLooptext) 
            break
    return SelectedNumber

#Chapter 1

#Powitanie
print(NarratorText1.center(20,"~"))
time.sleep(0.5)

#Pierwsze pyanie
print(NarratorText2)
time.sleep(1)


#Wybór odpowiedzi
Ch1In1 = input(Question1)

#sprawdzenie odpowiedzi
Ch1In1 = M3(Ch1In1)

if Ch1In1 == "1":
    print("1")
elif Ch1In1 == "2":
    print("2")
elif Ch1In1 == "3":
    print("3")
