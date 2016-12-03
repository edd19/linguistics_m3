#!/usr/bin/env python3
from __future__ import division
import string
import re


#complete rules with their respective count
rules_with_counts = {}

#proba to see a rule R->AB in all rules starting by R"
proba_of_rule = {}

#sum of counts
sum_counts = {}

newdico2 = {'A B C': 1, 'A B D': 1, 'A B E' : 1, 'R A B': 1, 'R A C':1}

#Input : (R (A ...)(B ...)), output : R AB
#extrait R->AB puis appelle la méthode sur A et sur B
# def parser(line):
#     newline = line[1:-1]
#
#     substring_start = newline.split(' ', 1)[0]
#     rest = newline.split(' ', 1)[1]
#
#     tab = []
#     tab.append(substring_start)
#     left, right = splitcorrectly(rest)
#     tab.append(left)
#
#     if len(right) > 0:
#         tab.append(right)
#     return tab




def add_to_dico(rule, dico):
    if rule not in dico:
        dico[rule]=1
    else:
        increment = dico[rule]
        increment = increment + 1
        dico[rule]= increment

# newdico = {'R A B' : 1, 'R A C' : 1}
# add_to_dico('R A B', newdico)
# add_to_dico('R A C', newdico)
# print(newdico)


#input : (X ...)(Y ...), returns (X ...) and (Y ...)
def splitcorrectly(line):
    ouvrante = 0
    fermante = 0
    index = 0
    if line.count('(') >1: #if not rule -> terminal
        for x in line:
            if x == '(':
                ouvrante +=1
            elif x == ')':
                fermante +=1

            if ouvrante-fermante==0:
                break
            index +=1
        return (line[:index+1], line[index+1:])
    else:
        #if rule -> terminal
        return (line[1:-1].split(' ')[0], line[1:-1].split(' ')[1])

#string of the form (word XXXXX), returns "word"
def extract_symbol(sub):
    symbol=''
    sub = sub.replace('(','')
    split = sub.split(' ', 1)
    return split[0]


#tells if a rule is terminal
def terminal(line):
    if line.count(' ') == 1:
        return True
    else:
        return False

#parses recursively a line
def parser_recursive(line):
    newline = line[1:-1]
    split = newline.split(' ',maxsplit=1) #line split with the first space
    substring_start = split[0]  # start symbol
    #print("Start = " + substring_start)

    # what comes after "->"
    rest = split[1]
    #print("Rest = " + rest)
    tab = []

    #if line isn't of the form R->terminal
    if not terminal(line):
        tab.append(substring_start) #first elem of tab = start
        left, right = splitcorrectly(rest) #
        tab.append(left) #second elem is


        tab.append(right)
        #print(tab)
        rule = tab[0] + ' ' + extract_symbol(tab[1]) + ' ' + extract_symbol(tab[2])
        add_to_dico(rule, rules_with_counts)
        #print('left : '+tab[1])
        #print('right : ' + tab[2])
        parser_recursive(tab[1])#recursion on first operand
        parser_recursive(tab[2])#recursion on second operand

    elif terminal(line):#ici ca marche
        #no right part, left part is a terminal
        rule = substring_start + ' ' + rest

        add_to_dico(rule, rules_with_counts)
        #end of recursion


#newdico = {}
#parser_recursive('(SBARQ (WHADVP where)(SBARQ (SQ (VBD was)(SQ (NP <unknown>)(VP born)))(<.> ?)))')
#print(rules_with_counts)


#input : dico of rules with counts, returns : dictionary with sum of counts of R -> ...
def sum_of_counts(dico):
    newdico = {}

    for symbol in dico:
        #print("Symbol is : " + symbol)
        # start of rule = the "R"
        start_of_rule = symbol.split(' ', maxsplit=1)[0]
        #print("Start is equal to : " + start_of_rule)

        #add_to_dico(start_of_rule, newdico)
        if start_of_rule not in newdico:
            count = rules_with_counts[symbol]
            newdico[start_of_rule] = count
            #print(newdico)
        elif start_of_rule in newdico:
            newdico[start_of_rule]=newdico[start_of_rule]+rules_with_counts[symbol]
            #print(newdico)
    return newdico

#proba of choosing R->Beta among all rules starting with R
def likelihood(dico):
    newdico = {}

    for symbol in dico:
        counter_of_rule = dico[symbol]
        start = symbol.split(' ', maxsplit=1)[0] #to retrieve 'R'

        counter_of_sum = sum_counts[start]
        newdico[symbol] = counter_of_rule /counter_of_sum

    return newdico

#in : dico, out : sum for all
def verif_sum_equal_one(dico):
    pass
#in : dico, out : count of R->AB rules
def count_non_terminals():
    pass

#in : dico, out : count of R->terminal rules
def count_terminals():
    pass

#takes the text as input and returns a standardized text
def standardize(input):
    with open(input, 'r') as f:
        for line in f:
            parser_recursive(line)
        #print(rules_with_counts)
    f.closed

standardize('/Users/Ivan/PycharmProjects/linguistics_m3/resources/train.txt')
#parser_recursive('(SBARQ (WHNP what)(SBARQ (SQ (VBZ <s)(NP (NP (DT the)(NP (JJS <unknown>)(<NN> planet)))(PP (IN from)(NP (DT the)(<NN> sun)))))(<.> ?)))')
#print(rules_with_counts)

sum_counts = sum_of_counts(rules_with_counts)
#print(sum_counts)
proba_of_rule = likelihood(rules_with_counts)

#print(proba_of_rule)
#print(str(len(rules_with_counts) == len(proba_of_rule)))