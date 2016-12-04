
def assess_perfomance(gold_standard, actual_sentence):
    decomposition_gold = decompose_tree(gold_standard)
    decomposition_acutal = decompose_tree(actual_sentence)
    g = len(decomposition_gold[2])
    p = len(decomposition_acutal[2])
    count_correct = return_count_correct(decomposition_gold[2], decomposition_acutal[2])
    return count_correct, p, g


def return_count_correct(gold_standard_table, actual_table):
    count = 0
    for element in gold_standard_table:
        if element in actual_table:
            count += 1
    return count


def decompose_tree(sentence_tree, start_index=1):
    table = []
    new_sentence_tree = sentence_tree[1:-1]
    label, childs = new_sentence_tree.split(" ", 1)
    left_child, right_child = split_childs(childs)
    if is_terminal(left_child, right_child):
        table.append((label, str(start_index) + "-" + str(start_index)))
        end_index = start_index
        return start_index, end_index, table
    left_decomposition = decompose_tree(left_child, start_index)
    right_decomposition = decompose_tree(right_child, left_decomposition[1]+1)
    table.append((label, str(start_index) + "-" + str(right_decomposition[1])))
    table.extend(left_decomposition[2])
    table.extend(right_decomposition[2])
    return start_index, right_decomposition[1], table


def is_terminal(left_child, right_child):
    if len(right_child) == 0:
        return True
    return False


def split_childs(childs):
    index = find_index_to_split(childs)
    if index == 0:
        return childs, ""
    return childs[:index+1], childs[index+1:]


def find_index_to_split(childs):
    count = 0
    for index in range(0, len(childs)):
        if childs[index] == "(":
            count += 1
        elif childs[index] == ")":
            count -= 1
        if count == 0:
            break
    return index