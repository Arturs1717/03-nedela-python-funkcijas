from utils import *
from validators import *
from data_collections import *


def run_demo():
    print("=== DEMO ===")

    numbers = [1, 2, 3, 4, 5]

    print("Saraksts:", numbers)
    print("Vidējais:", average(numbers))
    print("Max:", max_in_list(numbers))
    print("Min:", min_in_list(numbers))

    text = "programmesana"
    print("Patskaņi:", count_vowels(text))
    print("Apgriezts:", reverse_text(text))
    print("Palindroms:", is_palindrome("level"))

    print("Pozitīvs 5:", is_positive(5))
    print("Diapazons 7 (1–10):", is_in_range(7, 1, 10))


if __name__ == "__main__":
    run_demo()