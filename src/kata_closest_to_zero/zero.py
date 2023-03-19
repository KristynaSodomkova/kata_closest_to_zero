
negative_list = []
positive_list = []


def create_neg_and_pos_lists(list_of_num):
    for num in list_of_num:
        if num < 0:
            negative_list.append(num)
        else:
            positive_list.append(num)
    return negative_list, positive_list


def find_closest_neg(negative_list):
    neg_closest = max(negative_list)
    return neg_closest


def find_closest_pos(positive_list):
    pos_closest = min(positive_list)
    return pos_closest


def compare_two_values(list_of_num):
    neg_list, pos_list = create_neg_and_pos_lists(list_of_num)
    neg = find_closest_neg(neg_list)
    pos = find_closest_pos(pos_list)
    if pos - 0 > 0 - neg:
        return neg
    elif pos - 0 < 0 - neg:
        return pos
    else:
        return pos
