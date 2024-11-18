number_of_rows = int(input("Enter the number of rows: "))

num = 1
for row in range(1, number_of_rows + 1):
    for column in range(row):
        print(num, end=" ")
        num = num + 1
    print()
