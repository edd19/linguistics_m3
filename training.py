#!/usr/bin/env python3
import sys

# complete rules with their respective count
rules_with_counts = {}

# proba to see a rule with R as "R -> AB"
proba_of_rule_r = {}

# proba to see a rule with R A B exactly in "R -> AB"
proba_of_full_rule = {}


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
    # print("Start = " + substring_start)

    # what comes after "->"
    rest = split[1]
    # print("Rest = " + rest)
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


# newdico = {}
# parser_recursive('(SBARQ (WHADVP where)(SBARQ (SQ (VBD was)(SQ (NP <unknown>)(VP born)))(<.> ?)))')
# print(rules_with_counts)


# takes the text as input and returns a standardized text
def standardize(input):
    with open(input, 'r') as f:
        for line in f:
            parser_recursive(line)
            # print(rules_with_counts)

    # standardize('/Users/Ivan/PycharmProjects/linguistics_m3/resources/train.txt')
