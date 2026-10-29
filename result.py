import sys


def calculate_total_and_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return total, average


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def evaluate_performance(mark1, mark2, mark3):
    total, average = calculate_total_and_average(mark1, mark2, mark3)
    grade = calculate_grade(average)
    return total, average, grade


# Get marks from command-line arguments
if len(sys.argv) == 4:
    sub1 = float(sys.argv[1])
    sub2 = float(sys.argv[2])
    sub3 = float(sys.argv[3])
else:
    # Default marks for manual execution
    sub1, sub2, sub3 = 75.0, 62.0, 45.0


total, average, grade = evaluate_performance(sub1, sub2, sub3)

print("\n=== Jenkins Student Report Card ===")
print(f"Subject 1 Marks : {sub1}")
print(f"Subject 2 Marks : {sub2}")
print(f"Subject 3 Marks : {sub3}")
print("-----------------------------------")
print(f"Total Marks     : {total}")
print(f"Average Score   : {average:.2f}%")
print(f"Grade           : {grade}")
print("===================================\n")
