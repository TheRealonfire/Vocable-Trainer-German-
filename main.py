# Preparations
ey_cool = True
vokabel = list()
from time import sleep
import random
from translate import Translator
translator = Translator(to_lang="de")
# This  Script save the vocable:
print('Lol K Prouduce © 0.0.01')
print('First write your vocables')
sleep(2)
while ey_cool:
    LULW = input ('Write your one vocable here: ')
    if LULW == 'exit v':
        break
    elif LULW == 'show list':
        print(vokabel)
    vokabel.append (LULW)
    print('Word has been saved ')
    sleep(1)

# Main Script
print("Now you're ready. I took the vocable in a temporary Vocabulary,  ")
sleep(3)
print(random.choice(vokabel))
translation = translator.translate()
