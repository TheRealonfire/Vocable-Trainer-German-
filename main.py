# Damit du jetzt siehst wie ich Vokabel Lernen werde Hier:
print('This Script based on a normal Vocable Trainer')
# Sachen die man als Vorbereitung braucht
ey_cool = True
vokabel = list()
vokabel_de = list()
from random import randint
from time import sleep
import random
# Das Script zum Speichern von Vokabeln:
print('Lol K Prouduce © 0.0.01')

while ey_cool:
    LULW = input ('Zuerst gibst du deine Vokabeln der Fremdsprache ein: ')
    if LULW == 'exit vokal':
        break
    elif LULW == 'show list':
        print(vokabel)
    OMEGALUL = input ('Jetzt gibst du das Deutsche Wort / Satz ein: ')
    vokabel.append (LULW)
    vokabel_de.append(OMEGALUL)
    print('Wort wurde gespeichert')
    sleep(2)

# So jetzt kommt der wichtigste Teil
print('So da du jetzt deine Vokabeln ausgesucht hast werden diese als Random Generate gehalten')
sleep(2)
print(random.choice(vokabel))