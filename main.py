import training
import sys


def train_grammar(file_path):
    training.standardize(file_path)
    return training.proba_of_full_rule, training.reverse_rules

if __name__ == '__main__':
    file_path = sys.argv[1]
    proba_rules, reverse_rules = train_grammar(file_path)


