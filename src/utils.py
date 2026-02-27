def is_even(n):
    """Pārbauda vai skaitlis ir pāra"""
    return n % 2 == 0


def is_odd(n):
    """Pārbauda vai skaitlis ir nepāra"""
    return n % 2 != 0


def average(numbers):
    """Aprēķina saraksta vidējo"""
    return sum(numbers) / len(numbers)


def max_in_list(numbers):
    """Atrod lielāko skaitli sarakstā"""
    return max(numbers)


def min_in_list(numbers):
    """Atrod mazāko skaitli sarakstā"""
    return min(numbers)


def count_vowels(text):
    """Saskaita patskaņus tekstā"""
    vowels = "aeiouāēīūo"
    return sum(1 for c in text.lower() if c in vowels)


def reverse_text(text):
    """Apgriež tekstu otrādi"""
    return text[::-1]


def is_palindrome(text):
    """Pārbauda vai teksts ir palindroms"""
    t = text.lower()
    return t == t[::-1]