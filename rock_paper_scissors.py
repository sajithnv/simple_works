import random
p_score = 0
m_score = 0
n = 1
print(' *****   NEW GAME    ***** \n MAX SCORE IS " 3 "')
def play(p_score,m_score,n):
    dictt = dict(r='ROCK',p='PAPER',s='SCISSOR')
    print(f'____________________LEVEL {n} _______________________')
    player = input('"r" for ROCK "p" for PAPER and " s" for SCIOSSORS...\n Enter a choice : ')
    try:
        print(f'YOUR CHOICE IS {dictt[player]} ')
    except KeyError:
        print('Invalid Choice !!!')
        play(p_score,m_score,n)
    else:
        computer = random.choice(['r','p','s'])
        print(f'MY CHOICE IS {dictt[computer]} ')
        x = result(player,computer)
        if x == 1:
            p_score += 1
            n += 1
            print(f'You scored !! \n Your Score is : {p_score}\n My Score is : {m_score}')
        elif x == 0:
            print('IT\'s A TIE')
            print(f'___Live Score details___\n My Score is : {m_score}\n Your Score is : {p_score}')
        else:
            m_score += 1
            n += 1
            print(f'Got it !!\n My Score is : {m_score}\n Your Score is : {p_score}')
        if p_score == 3 :
            print("___GAME OVER___\n YOU\'RE THE WINNER")
        elif m_score == 3:
            print("___GAME OVER___\n I WON << BETTER LUCK NEXT TIME >>")
        else:
            return play(p_score,m_score,n)

def result(p,c):
    if score(p,c)==1:
        return 1
    elif p == c:
        return 0
def score(p,c):
    # r<p and p<s and s<r
    if (p == 'p' and c == 'r') or (p == 's' and c == 'p') or (p == 'r' and c == 's'):
        return 1
play(p_score,m_score,n)