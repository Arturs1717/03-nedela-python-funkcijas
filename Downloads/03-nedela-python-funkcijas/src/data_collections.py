students = ["Anna", "Jānis", "Pēteris", "Laura", "Marta"]
print("Studenti:", students)

print("\nStudentu saraksts:")
for s in students:
    print("-", s)

long_names = [s for s in students if len(s) > 5]
print("\nGarāki vārdi:", long_names)

grades = {
    "Anna": 8,
    "Jānis": 7,
    "Pēteris": 9,
    "Laura": 10,
    "Marta": 6
}

print("\nAtzīmes:", grades)

print("\nStudentu atzīmes:")
for name, grade in grades.items():
    print(name, "->", grade)

good_students = {n: g for n, g in grades.items() if g >= 8}
print("\nSekmīgie studenti:", good_students)