#Check if a year is a leap year
year=int(input("enter an year"))
print(year,"is leap year") if (year%4==0 and year%100!=0) or (year%400==0) else print(year,"is not a leap year")

#Calculate the grade of a student based on the marks they score: 1. 90-100 : Grade A 2. 80-89 : Grade B 3. 70-79 : Grade C 4. <70 : Fail.
marks=int(input("enter student marks"))
if marks<=100:
    if marks>=90 and marks<=100:
        print("Grade-A")
    elif marks>=80 and marks<=89:
        print("Grade-B")
    elif marks>=70 and marks<=79:
        print("Grade-C")
    else:
        print("Fail")
else:
    print("enter valid marks")

#Write a program to check if three sides length form a valid triangle.
a,b,c=map(int,input().split())
print("valid triangle") if (a+b>c) and (b+c>a) and (a+c>b) else print("invalid triangle")


