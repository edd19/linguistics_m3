#!/usr/bin/env python3
from __future__ import division
import string
import re
import sys

# complete rules with their respective count
rules_with_counts = {}

# proba to see a rule with R as "R -> AB"
proba_of_rule_r = {}

# proba to see a rule with R A B exactly in "R -> AB"
proba_of_full_rule = {}

reverse_rules = {}

sum_counts = {}

# Input : (R (A ...)(B ...)), output : R AB
# extrait R->AB puis appelle la méthode sur A et sur B
def parser(line):
    newline = line[1:-1]

    substring_start = newline.split(' ', 1)[0]
    rest = newline.split(' ', 1)[1]

    tab = []
    tab.append(substring_start)
    left, right = splitcorrectly(rest)
    tab.append(left)

    if len(right) > 0:
        tab.append(right)
    return tab


def add_to_dico(rule):
    actual = rules_with_counts.get(rule, 0)
    rules_with_counts[rule] = actual + 1

    parent = rule[0]
    actual = proba_of_rule_r.get(parent, 0)
    proba_of_rule_r[parent] = actual + 1


    childs = rule[1]
    if len(rule) == 3:
        childs = (rule[1], rule[2])
    actual = reverse_rules.get(childs, [])
    actual.append(parent)
    reverse_rules[childs] = actual

# input : (X ...)(Y ...), returns (X ...) and (Y ...)
def splitcorrectly(line):
    ouvrante = 0
    fermante = 0
    index = 0
    if line.count('(') > 1:  # if not rule -> terminal
        for x in line:
            if x == '(':
                ouvrante += 1
            elif x == ')':
                fermante += 1

            if ouvrante - fermante == 0:
                break
            index += 1
        return (line[:index + 1], line[index + 1:])
    else:
        # if rule -> terminal
        return (line[1:-1].split(' ')[0], line[1:-1].split(' ')[1])


# string of the form (word XXXXX), returns "word"
def extract_symbol(sub):
    symbol = ''
    sub = sub.replace('(', '')
    split = sub.split(' ', 1)
    return split[0]


# tells if a rule is terminal
def terminal(line):
    if line.count(' ') == 1:
        return True
    else:
        return False


# parses recursively a line
def parser_recursive(line):
    newline = line[1:-1]
    split = newline.split(' ', maxsplit=1)  # line split with the first space
    substring_start = split[0]  # start symbol

    # what comes after "->"
    rest = split[1]
    tab = []

    # if line isn't of the form R->terminal
    if not terminal(line):
        tab.append(substring_start)  # first elem of tab = start
        left, right = splitcorrectly(rest)  #
        tab.append(left)  # second elem is

        tab.append(right)
        rule = (tab[0], extract_symbol(tab[1]), extract_symbol(tab[2]))
        add_to_dico(rule)
        parser_recursive(tab[1])  # recursion on first operand
        parser_recursive(tab[2])  # recursion on second operand

    elif terminal(line):  # ici ca marche
        # no right part, left part is a terminal
        rule = (substring_start , rest)

        add_to_dico(rule)
        # end of recursion


def compute_probability():
    for rule in rules_with_counts.keys():
        parent = rule[0]
        proba_of_full_rule[rule] = rules_with_counts[rule] / proba_of_rule_r[parent]


#input : dico of rules with counts, returns : dictionary with sum of counts of R -> ..., for each rule that starts with R
def sum_of_counts(dico):
    newdico = {}

    for symbol in dico:
        # start of rule = the "R"
        start_of_rule = symbol[0]

        #add_to_dico(start_of_rule, newdico)
        if start_of_rule not in newdico:
            count = dico[symbol]
            newdico[start_of_rule] = count
        elif start_of_rule in newdico:
            newdico[start_of_rule]=newdico[start_of_rule]+dico[symbol]
    return newdico

#proba of choosing R->Beta among all rules starting with R
#in : rules_with_count, out = dico of each rule with its probability
def likelihood(dico):
    newdico = {}

    for symbol in dico:
        counter_of_rule = dico[symbol]
        start = symbol[0] #to retrieve 'R'

        counter_of_sum = sum_counts[start]
        newdico[symbol] = counter_of_rule /counter_of_sum

    return newdico


#in : dictionary with probabilities for each rules, out : verify if sums are equal to one
def verif_sum_equal_one(dico):
    dico_with_sum = {}
    for symbol in dico:
        start_of_rule=symbol[0]
        count = dico[symbol]
        if start_of_rule not in dico_with_sum:
            dico_with_sum[start_of_rule]=count
        else:
            dico_with_sum[start_of_rule]=dico_with_sum[start_of_rule]+dico[symbol]
    return dico_with_sum


#in : dico, out : count of R->AB rules
def count_non_terminals(dico):
    list = []
    for symbol in dico:
        if len(symbol) == 3:
            start_symbol = symbol[0]
            if start_symbol not in list:
                list.append(start_symbol)
    return len(list)

#in : dico, out : count of R->terminal rules
def count_terminals(dico):
    list = []
    for symbol in dico:
        if len(symbol)==2:
            terminal = symbol[1]
            if terminal not in list:
                list.append(terminal)
    return len(list)

#takes the text as input and returns a standardized text

def standardize(input):
    with open(input, 'r') as f:
        for line in f:
            parser_recursive(line)
    compute_probability()
    f.closed

# standardize('/Users/Ivan/PycharmProjects/linguistics_m3/resources/test.txt')
# #parser_recursive('(SBARQ (WHNP what)(SBARQ (SQ (VBZ <s)(NP (NP (DT the)(NP (JJS <unknown>)(<NN> planet)))(PP (IN from)(NP (DT the)(<NN> sun)))))(<.> ?)))')
#
# newdico = {'A B C': 1, 'A B D': 1, 'A B E' : 1, 'R A B': 1, 'R A C':1}
# newdico2 = {'A B C': 1, 'A B D': 1, 'A B E' : 1, 'R A B': 1, 'R A C':1, 'R a':1, 'R b':1}
# print(rules_with_counts)
#
# sum_counts = sum_of_counts(rules_with_counts)
# print(sum_counts)
# proba_of_rule = likelihood(rules_with_counts)
#
# print(proba_of_rule)
# test_sum = verif_sum_equal_one(proba_of_rule)
# print(test_sum)
# terminal_counts = count_terminals(rules_with_counts)
# print(terminal_counts)
# nontermcounts = count_non_terminals(rules_with_counts)
# print(nontermcounts)
# #print(str(len(rules_with_counts) == len(proba_of_rule)))