number=input("enter a word or number:")

if number == number[::-1]:
    print("it is palindrome")
else:
    print("not a palindrome")