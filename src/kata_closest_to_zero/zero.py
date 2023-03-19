
negative_list = []
positive_list = []


def create_neg_and_pos_lists(list_of_num):
    for num in list_of_num:
        if num < 0:
            negative_list.append(num)
        else:
            positive_list.append(num)
    return negative_list, positive_list


def find_closest_neg():
    neg_closest = max(negative_list)
    return neg_closest


def find_closest_pos():
    pos_closest = min(positive_list)
    return pos_closest
