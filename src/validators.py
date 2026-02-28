def is_positive(n):
    """Pārbauda vai skaitlis ir pozitīvs"""
    return n > 0


def is_non_empty_list(lst):
    """Pārbauda vai saraksts nav tukšs"""
    return isinstance(lst, list) and len(lst) > 0


def is_non_empty_string(text):
    """Pārbauda vai teksts nav tukšs"""
    return isinstance(text, str) and len(text.strip()) > 0


def is_in_range(n, min_val, max_val):
    """Pārbauda vai skaitlis ir diapazonā"""
    return min_val <= n <= max_val

if __name__ == "__main__":
    print(is_positive(5))
    print(is_positive(-2))

    print(is_non_empty_list([1, 2]))
    print(is_non_empty_list([]))

    print(is_non_empty_string("hello"))
    print(is_non_empty_string("   "))

    print(is_in_range(5, 1, 10))
    print(is_in_range(15, 1, 10))