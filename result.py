import sys

def evaluate_performance(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3

    if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
        status = "PASS"
    else:
        status = "FAIL"

    return total, average, status


# Get marks from command-line arguments
if len(sys.argv) == 4:
    sub1 = float(sys.argv[1])
    sub2 = float(sys.argv[2])
    sub3 = float(sys.argv[3])
else:
    # Default marks for manual execution
    sub1, sub2, sub3 = 75.0, 62.0, 45.0

total, average, status = evaluate_performance(sub1, sub2, sub3)

print("\n=== Jenkins Student Report Card ===")
print(f"Subject 1 Marks : {sub1}")
print(f"Subject 2 Marks : {sub2}")
print(f"Subject 3 Marks : {sub3}")
print("-----------------------------------")
print(f"Total Marks     : {total}")
print(f"Average Score   : {average:.2f}%")
print(f"Final Decision  : {status}")
print("===================================\n")