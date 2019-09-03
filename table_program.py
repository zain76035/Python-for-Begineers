
# A Simple table program that take input from the user and output (Display 1 less then, or 1 greater than ) table 



table = int(input("Enter table number : "))
for i in range(1,11):
        print(f"{table - 1} * {i} = {(table - 1) * i} \t {table} * {i} = {i*table} \t {table + 1} * {i} = {(table + 1) * i}")

