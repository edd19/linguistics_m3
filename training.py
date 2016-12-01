#!/usr/bin/env python3
import string
import re

dico1 = {}
dico2 = {}
dico3 = {}



def balanced(s, i=0, cnt=0):
    if i == len(s):
        return cnt == 0
    if cnt < 0:
        return False
    if s[i] == "(":
        return  balanced(s, i + 1, cnt + 1)
    elif s[i] == ")":
        return  balanced(s, i + 1, cnt - 1)
    return balanced(s, i + 1, cnt)




#Input : (R (A ...)(B ...)), output : R AB
#extrait R->AB puis appelle la méthode sur A et sur B
def parser(line):
    substring_start=''
    substring_op1=''
    substring_op2=''
    terminal = ''

    newline = line[1:-1]

    ouvrante = 0
    fermante = 0
    substring_start = newline.split(' ', 1)[0]
    terminal = newline.split(' ', 1)[1]
    tab = []
    tab.append(substring_start)
    left, right = splitcorrectly(terminal)
    tab.append(left)
    if len(right) > 0:
        tab.append(right)
    return tab


def splitcorrectly(line):
    ouvrante = 0
    fermante = 0
    index = 0
    for x in line:


        if x == '(':
            ouvrante +=1
        elif x == ')':
            fermante +=1

        if ouvrante-fermante==0:
            break
        index +=1
    print("Index" + str(index))
    return (line[:index], line[index+1:])




yo1 = '(test)'

#string commence par une parenthese ouvrante
#string = le string restant apres ouverture de la parenthese
# def sub_string_paren(line):
#     ouvrante = 0
#     fermante = 0
#     solution = ''
#     x = 0
#
#     for x in range(0, len(line)):
#         if line[x] == '(':
#             ouvrante = ouvrante + 1
#             solution = solution + line[x]
#         elif line[x] == ')':
#             fermante = fermante + 1
#             solution = solution + line[x]
#         x=x+1
#     return solution


#string of the form (word XXXXX), returns "word"
def extract_symbol(sub):
    symbol=''
    x = 0
    while(sub[x]!=' '):
        if(sub[x]!='('):
            symbol = symbol + sub[x]
        x=x+1
    return symbol

#takes the text as input and returns a standardized text
def standardize(input):
    with open(input, 'r') as f:
        for line in f:
            print(line)
            #newline = process_line(line)
    f.closed


yo = '(coucou ())()()()()()()()()()()()'
#print(extract_symbol(yo))
#standardize('/Users/Ivan/PycharmProjects/linguistics_m3/resources/test.txt')