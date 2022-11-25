
# Preparations

from time import sleep
import random
from typing import Counter
from googletrans import Translator
while_voc_input = True
many_loop = True
vokabel = list()
vokabel_finish = list()
Counter = 0
score = 0
percent = 100

# This  Script save the vocable:

print('Lol K Prouduce © 0.0.1')
print('First write your vocables')
sleep(2)
while while_voc_input:
    voc_input = input ('Write your one vocable here: ')

    if voc_input == 'exit v':
        break

    elif voc_input == 'show list':
        print(vokabel)

    else:
        vokabel.append(voc_input)
        print('Word has been saved ')


    sleep(1)

print("Now we are ready. I took the vocable in a temporary Vocabulary, but you don't added in the same session ")
sleep(1)

backup_voc = vokabel

#Loop many

many = input ('How many words do u want to test u ?: ')
many = int(many)

# Main Script

sleep(1)
while many_loop:
    if not vokabel:
        print ('No more vocables')
        break

    random_voc = random.choice(vokabel)

    questionvoc = input ('What is the german word of '+ random_voc + ': ')

    vokabel.remove(random_voc)

    denword = Translator(service_urls=['translate.googleapis.com'])

    enword = denword.translate(random_voc, src="en", dest="de")

    correct_voc = enword.text
    
    if questionvoc == correct_voc:
        print('correct')
        score += 1


    Counter  += 1

    if Counter == many:
        break

print('stopp')
sleep(1)
print('You got ' +  str(score) + ' coorect')

percentscore = score / many
percent = round(percentscore * 100, 2)

print('You got: ' + str(percent) + '% right' )
