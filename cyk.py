from math import log, e

UNKNOWN = "<unknown>"


def cyk(rules, reverse_rules, sentence):
    words = sentence.split()
    table = [[dict() for _ in range(0, x + 1)] for x in range(0, len(words))]
    back = [[dict() for _ in range(0, x + 1)] for x in range(0, len(words))]
    for j in range(0, len(words)):
        table[j][j] = get_terminal_rules(rules, reverse_rules, words[j])
        for i in range(j - 1, -1, -1):
            for k in range(i, j):
                possible_rules = get_all_possible_rules(rules, reverse_rules, table[i][k], table[k+1][j])
                for possible_rule in possible_rules:
                    table[j][i][possible_rule[0][0]] = log(possible_rule[1]) + \
                                                       table[i][k].get(possible_rule[0][1], 0) + \
                                                       table[i][k].get(possible_rule[0][2], 0)
                    back[j][i][possible_rule[0][0]] = (k+1, possible_rule[0][1], possible_rule[0][2])
    tree = build_parse_tree(table, back, words, len(words)-1, 0, list(table[len(words)-1][0].keys())[0] )
    return tree, list(table[len(words)-1][0].values())[0]


def build_parse_tree(table, back, words, i, j, key):
    if i == j:
        return  "(" + key + " " + (words[i]) + ")"
    backpointer = back[i][j].get(key)
    k = backpointer[0]
    left = backpointer[1]
    right = backpointer[2]
    return "(" + key + " " + build_parse_tree(table, back, words, i-k, j, left) + \
           build_parse_tree(table, back, words, i, j+k, right) + ")"


def get_terminal_rules(rules, reverse_rules, word):
    key = word
    if key not in reverse_rules:
        key = UNKNOWN
    terminal_rules = dict()
    for parent in reverse_rules[key]:
        terminal_rules[parent] = log(rules[(parent, key)])
    return terminal_rules


def get_all_possible_rules(rules, reverse_rules, child1, child2):
    b_childs = child1.keys()
    c_childs = child2.keys()

    for b_child in b_childs:
        for c_child in c_childs:
            parents = reverse_rules.get((b_child, c_child), [])
            for parent in parents:
                yield ((parent, b_child, c_child), rules[(parent, b_child, c_child)])
