
def is_symmetric(lst):
    return lst == lst[::-1]

def can_remove_two_to_order(lst):
    for i in range(len(lst) - 2):
        if lst[i] > lst[i + 2]:
            return True
    return False

def count_unique_values(lst):
    return len(set(lst))
