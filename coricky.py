# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:32:43 2020

@author: paul
"""


"""
        1           2           3           4           5           6
1   1   1er pasch   maechsle    31          41          51          61
1   2   maechale    2er pasch   32          42          52          62
1   3   31          32          3er pasch   43          53          63
1   4   41          42          43          4er pasch   54          64
1   5   51          52          53          54          5er pasch   65
1   6   61          62          63          64          65          6er pasch

"""
ranking = [0,31,32,41,42,43,51,52,53,54,61,62,63,64,65,11,22,33,44,55,66,21]

import random

class game_state:
    def __init__(self):
        self.last_go_claim = 0
        self.last_go_fact = 0
        self.current_claim = 0
        self.current_fact = 0
    def update_last(self, claim, fact):
        self.last_go_claim = claim
        self.last_go_fact = fact
    def update_current(self, claim, fact):
        self.current_claim = claim
        self.current_fact = fact
        

def roll_dice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    if d1 > d2:
        score = d1 * 10 + d2
    else:
        score = d2 * 10 + d1
    return score
    
        
def computer_go(last_score):
    if last_score != 0:
        print("Let me think if I believe the last score or not....")
    
    # arbritrary logic...
    if ranking.index(last_score) < 10:
        believe = True
    else:
        if random.randint(1,4) == 1:
            believe = True
        else:
            believe = False
    
    if not believe: 
        print("I don't believe you")        
        return False
    
    score = roll_dice()        
    #print('I got {}'.format(score))    
    if score == 21:
        print('MAECHSLE!')
    if ranking.index(score) <= ranking.index(last_score):
        # print("{} is less than or equal to {}, oh no, I have to lie!".format(score, last_score))
        position = ranking.index(last_score)
        my_say = ranking[random.randint(position, len(ranking)-1)]
    else:
        # random lie?
        if random.randint(1,5) == 2:
            position = ranking.index(last_score)
            my_say = ranking[random.randint(position, len(ranking)-1)]
        else:
            my_say = score
    print("I say I have got {}".format(my_say))

    return (my_say, score)    
    
def human_go(last_claim):
    believe = input("Do you believe the last claim?")
    if believe.lower() in ('n', 'no', 'nein'): return False
    score = roll_dice()
    print("You got {}".format(score))
    claim = int(input("What do you say?"))
    return (claim, score)
    
import os
os.system('cls')     
    
state = game_state()
winner = False
last_score = 0
while not winner:
    turn = computer_go(state.current_claim)
    if not turn:
        print("Computer doesn't believe")
        if state.current_fact == state.current_claim:
            print("But it was true!")
            winner = True
            break
        else:
            print("It was a lie!")
            winner = True
            break
    elif turn[1] == 21: 
            winner = True
            print("Kuriki")
            break
    else:
        state.update_last(state.current_claim, state.current_fact)
        state.update_current(turn[0], turn[1])
    
    turn = human_go(state.current_claim)
    if not turn:
        print("You don't believe Computer")
        if state.current_fact == state.current_claim:
            print("But it was true!")
            winner = True
            break
        else:
            print("It was a lie!")
            winner = True
            break
    elif turn[1] == 21: 
            winner = True
            print("Kuriki")
            break
    else:
        state.update_last(state.current_claim, state.current_fact)
        state.update_current(turn[0], turn[1])
        