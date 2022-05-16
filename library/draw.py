"""
There are here necessary definitions to correctly working program.
"""
import os
import random
import numpy as np
import matplotlib.pyplot as plt

def render(obs):
    '''Allow user to view the current state.'''
    # Inspired by: https://github.com/TristanBester/gym_algos/tree/master/NChain-v0
    states = ['x'] * 4 +['G']
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(5):
        if i == obs:
            print(f'\x1b[1;32;44m' + states[i] + '\x1b[0m', end='')
        else:
            print(f'\x1b[1;35;40m' + states[i] + '\x1b[0m', end='')
            
def chart(tl,tr):
    '''Allow user to view how the probability will change.'''
    w=0.4
    x=[0,1,2,3,4]

    plt.bar(x,tl,w,label="Decision Back")
    plt.bar(x,tr,w,bottom=tl,label="Decision Forward")

    plt.xlabel("Every decision")
    plt.ylabel("Summary probability")
    plt.title("Decision where to go")
    plt.legend()
    plt.show()