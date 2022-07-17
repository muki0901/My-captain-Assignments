list1=[]
list2=[]
my_list1=[]
my_list2=[]
n=int(input("Enter size of list1 "))        #entering list size
for i in range(0,n):
    e=int(input("Enter element of list1 ")) 
    list1.append(e)                         #appending the elements to the list
print(list1)
k=int(input("Enter size of list2 "))        #entering list size
for f in range(0,k):
    e=int(input("Enter element of list2 "))
    list2.append(e)                         #appending the elements to the list
print(list2)
for x in list1:
    if x>0:                                 #checking whether the numbers are positive
        print("The pos numbers are:",x)
        my_list1.append(x)                  #appending the positive elements to the list
print(my_list1)
for y in list2:
    if y>0:                                 #checking whether the numbers are positive
        print("The pos numbers are:",y)
        my_list2.append(y)                  #appending the positive elements to the list
print(my_list2)
