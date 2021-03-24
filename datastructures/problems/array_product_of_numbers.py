#  You have a list of integers, and for each index you want to find the product of every integer
#  except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products. 

# ex.: [1, 7, 3, 4] -> [84, 12, 28, 21]

def test_answer():
    given = [1, 7, 3, 4]
    expected = [84, 12, 28, 21]
    assert get_product(given) == expected

def get_product(value):
    size = len(value)
    result = []*size

    for i in range(size):
        acc = 1
        for j in range(size):
            if i != j:
                acc = acc * value[j]
        result.append(acc)
    return result