s=input("enter a string:")
vowel="aeiou"
count=0
for char in s:
    if char in vowel:
        count +=1
print("number of vowels:",count)
