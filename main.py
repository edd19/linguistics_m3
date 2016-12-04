import training
import sys


def train_grammar(file_path):
    training.standardize(file_path)
    print("Finished training")

if __name__ == '__main__':
    file_path = sys.argv[1]
    train_grammar(file_path)
    print(training.rules_with_counts)
    print(training.proba_of_rule_r)
    print(training.proba_of_full_rule)

