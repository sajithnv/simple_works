import random
from word_list import word_list1 as word
from word_list import a_z
while True:
    print( '**** NEW_GAME ****' )
    new_word = random.choice(word)
    chances = len(new_word)
    print(f'you have {chances} chances')
    lis1 = []
    trush = ''
    list_display = []
    for i in new_word:
        lis1 += i
        list_display.append('_')
    lis2 = lis1.copy()
    for _ in range(len(lis1)):     # len(double) choices, if len(word) == 3 then, no of choice is 6
        lis2 += random.choice(a_z)
    opt = set(lis2)                 # avoid repeating letters
    while chances > 0:
        y = ''
        for i in list_display:
            y += i
            y += ' '
        print(f'____Remaining Chances : {chances} ____\nPattern is : {y} : {trush}')
        inp =input('Guess a letter : ')
        low = inp.lower()
        if low == 'sajith':
            print(f"The word is : # {new_word} #.. *** You're the MASTER ***")
            continue
        if '_' not in list_display or inp == new_word:
            print(f'______________________RESULT_____________________\n ***** YOU WON..You SAVE Him ****\n The Word is "{new_word}"')
            break
        if inp.isalpha() == False or len(inp) > 1 :
            print('InValid Choice !!!!!')
            continue
        if low in lis1:
            ind = lis1.index(low)
            print(' **** Gotcha **** ')
            list_display[ind] = low
            lis1[ind] = '_'
        else:
            print(f'loosed one chance !!! Option = {opt}')
            trush += low
            trush += ' '
            chances -= 1
        if chances == 0:
            print(f'______________________RESULT_____________________\nG A M E   O V E R...You Killed him !!!\nThe word is "{new_word}" \nEntered letters are : {trush}\nTotal chances : {len(new_word)}')       
    x = str(input('Continue the Game\n "any key" for Continue "N" for EXIT\nENTER A CHOICE : '))
    if x == 'N' or x == 'n':
        print('Exited')
        break      