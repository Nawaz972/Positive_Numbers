# All ppositive numbers in the range or list
li=list()
n=int(input("Enter the size of the list: "))          # Reading the size of the list
print("Enter the numbers: ")
for i in range(n):
    ele=int(input())
    li.append(ele)                                              # Append function -> Adds the element at the end of the list 
print("List:",li)                                                # Printing the list given by user
print("The positive numbers from the list are: ")  
for num in li:
    if num >= 0:
        print(num, end = " ")                             # Printing the positive numbers from the list