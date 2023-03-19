from kata_closest_to_zero.zero import *

list_of_num = [-7, -5, -3, -2, 0, 2, 8, 20]


def test_negative_num_only():
    result = create_neg_list(list_of_num)
    assert all(num < 0 for num in result)


