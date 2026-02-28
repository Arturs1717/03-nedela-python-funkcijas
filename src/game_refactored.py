from utils import *
from validators import *


def play_game():
    print("Laipni lūgts spēlē!")

    numbers = [1, 2, 3, 4, 5]

    if is_non_empty_list(numbers):
        avg = average(numbers)
        print("Vidējais:", avg)

    text = "level"
    print("Vai palindroms:", is_palindrome(text))


if __name__ == "__main__":
    play_game()