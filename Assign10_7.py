"""Write a python script to print first N even natural numbers in reverse order"""

num=int(input("Enter a no:"))

for e in range(2*num,0,-1):
    if e%2==0:
       print(e, end="  ")
