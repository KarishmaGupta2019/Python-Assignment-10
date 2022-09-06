#Write a python script to print first N odd natural numbers

num=int(input("Enter a number:"))
for e in range(1 ,(2*num)+1):
    if e%2!=0:
        print(e, end=' ')
