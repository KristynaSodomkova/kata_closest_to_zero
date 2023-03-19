
negative_list = []


def create_neg_list(list_of_num):
    for num in list_of_num:
        if num < 0:
            negative_list.append(num)
    return negative_list


