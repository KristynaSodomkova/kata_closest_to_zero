from kata_closest_to_zero.zero import *

list_of_num = [-7, -5, -3, -2, 0, 2, 8, 20]
list_of_num2 = [-7, -5, -3, -2, 2, 8, 20]


def test_neg_and_pos_num_only():
    neg_list, pos_list = create_neg_and_pos_lists(list_of_num)
    assert all(num < 0 for num in neg_list)
    assert all(num >= 0 for num in pos_list)

def test_find_closest_neg():
    negative_list, positive_list = create_neg_and_pos_lists(list_of_num)
    assert find_closest_neg(negative_list) == -2


def test_find_closest_pos():
    negative_list, positive_list = create_neg_and_pos_lists(list_of_num)
    assert find_closest_pos(positive_list) == 0


def test_compare_two_values():
    assert compare_two_values(list_of_num) == 0
    assert compare_two_values(list_of_num2) == 2

