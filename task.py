#Q1
print("Hello World...by divya")

#Q2
cost_price = 100
selling_price = 120

if selling_price > cost_price:
    profite = selling_price-cost_price
    print("Profit =", profite)
elif cost_price > selling_price:
    loss = cost_price-selling_price
    print("Loss =", loss)
else:
    print("No profit, no loss")

#Q3
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

Q4
age = int(input("Enter your age:"))
if age >= 18:
    print("Age is valid and eligible for voting")
else:
    print("Age is valid but not eligible for voting")

#Q5
word1 = input("Enter word 1:")
word2 = input("Enetr word 2:")
if sorted(word1) == sorted(word2):
    print("Both words are Anagram")
else:
    print("Both words are not Anagram")