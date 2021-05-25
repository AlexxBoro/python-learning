# expenses = [10.50, 8, 5, 50, 20, 5, 3]
# sum = 0

# for x in expenses:
#     sum = sum + x

# total = sum(expenses)

total = 0
expenses = []

num_expenses = int(input("Enter # of expenses:"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent $", total, sep="")
