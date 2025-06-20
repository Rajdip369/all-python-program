#WAP to check if a list contains a palindrome of elements.(hint: use copy()method)
#like- [1,2,3,2,1] & [1,"abc","abc",1]

num=input("inter the number/str: ")
list1 = [num]

copy_list1 = list1.copy()

copy_list1.reverse()


if(copy_list1 == num):
    print("this is palindrome." )

else:
    print("This is Not a palindrome." )


#problem is using not a user input 