#Write a python script to print cubes of first N natural numbers

num=int(input("enter a number:"))
for e in range(1,num+1,1):
    print(e**3, end="  ")