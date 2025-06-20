mark =int(input("enter student marks: "))

if(mark>=90):
    grade= "A+"
elif(mark>=80):
    grade="A"
elif(mark>=70):
    grade="B"
elif(mark>=60):
    grade="C"
else:
    grade="D"

print("Your grade is : ",grade)
