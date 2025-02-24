#Check if a given number is a prime number using a for loop.
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
print("1-100 divisible by 3 and 5")
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)
#Implement a menu-driven program where the user can choose to: 1. Find the square of a number. 2. Find the cube of a number. 3. Exit.
while True:
    option=int(input("enter options (1/2/3)"))
    if option==1:
         square=int(input("enter a number to square:"))
         print("square of number is:",square*square)
    elif option==2:
        cube=int(input("enter a number to cube:"))
        print("cube of a number is:",cube**3)
    elif option==3:
        print("you are exited")
        break
    else:
        print("invalid options")
        






    


