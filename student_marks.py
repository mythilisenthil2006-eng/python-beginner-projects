name = input("Enter Student Name: ")

tamil = int(input("Tamil Mark: "))
english = int(input("English Mark: "))
maths = int(input("Maths Mark: "))

total = tamil + english + maths
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
