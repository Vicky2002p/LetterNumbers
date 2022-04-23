def ascii_sum(mystr1):
    sum = 0
    for item in mystr1:
        print(ord(item))
        sum += ord(item)
    return sum

name =input("Please enter your first name: ")
print(f"Welcome {name}")
mysum = ascii_sum(name)
print(f"So the sum of the letter in your name is: {mysum}")
