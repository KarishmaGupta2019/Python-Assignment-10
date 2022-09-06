#Write a python script to print first N natural numbers in reverse order

num=int(input("enter a number:"))
for e in range(num,0,-1):
    print(e, end='  ')

