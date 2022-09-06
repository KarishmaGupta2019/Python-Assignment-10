#Write a python script to print first N even natural numbers

num=int(input("Enter a no:"))
for e in range(1,2*num+1):
    if e%2==0:
        print(e,end="  ")