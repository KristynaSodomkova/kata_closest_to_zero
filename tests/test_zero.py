from kata_closest_to_zero.zero import *

list_of_num = [-7, -5, -3, -2, 0, 2, 8, 20]


def test_negative_or_positive_num_only():
    neg_list, pos_list = create_neg_and_pos_lists(list_of_num)
    assert all(num < 0 for num in neg_list)
    assert all(num >= 0 for num in pos_list)


