UNKNOWN = "<unknown>"


def cyk(rules, reverse_rules, sentence):
    words = sentence.split()
    table = [[dict() for _ in range(0, x+1)] for x in range(0, len(words))]
    for j in range(0, len(words)):
        table[j][j] = get_terminal_rules(rules, reverse_rules, words[j])


def get_terminal_rules(rules, reverse_rules, word):
    key = word
    if key not in reverse_rules:
        key = UNKNOWN
    terminal_rules = dict()
    for parent in reverse_rules[key]:
        terminal_rules[(parent, key)] =  rules[(parent, key)]
    return terminal_rules

