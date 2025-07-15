a=(100,200,300)  #create a tuple and print it
print(a)
print(type(a))

b=("red","green","blue","yellow")  #print second to last element
print(b[-2])

c=(10,20,5,15)   #print a minimum number
d=min(c)
print(d) 


e=('dog','cat','rabbit')  #finding the index of cat
index=e.index('cat')
print(index)


fruits = ('apple', 'banana', 'orange')  #print kiwi is in list or not
if "kiwi" in fruits:
    print("Kiwi is in the tuple")
else:
    print("Kiwi is not in the tuple")

num={10,20,30}  #print a set type
print(num)
print(type(num))


num2={12,34,55,67,88,99,9,33,}  #using clear method clear the elements
print(num2)
num2.clear()
print(num2)  



set1={1,2,3,4}   #remove 4 from the set
print(set1)
set1.remove(4)
print(set1) 

set1 = {1, 2, 3}  #union of set remove the duplicate value
set2 = {4, 5, 6,3}
union_set = set1.union(set2)
print(union_set)     


dict1={"Name":"Shivani","Age":20,"City":"Hamirpur"}  #print dictionary
print(dict1)
print(type(dict1))       


person = {"name": "jon", "age": 25}   #add country to dictionary
person.update({"country": "USA"})
print(person)         

dict2 = {"Name": "Alice", "age": 30}   #acees the name
print(dict2["Name"])

dict2 = {"Name": "Alice", "age": 30,"Rollno":23}  #remove age 
print(dict2)
dict2.pop("age")
print(dict2)
   


dict9={"Name":"Shivani","Age":20,"city":"Hamirpur"} #print city is in or not present
if "city" in dict9:
    print("Key 'city' exists in the dictionary.")
else:
    print("Key 'city' does not exist in the dictionary.")



list3=[1,2,3,4,5,66]  #print list
print(list3)
print(type(list3))
tuple3=(334,55,66,777,"cherry",777)  #print tuple
print(tuple3)
print(type(tuple3))
dict0={"Name":"Shivani","Age":20,"city":"Hamirpur"}   #print dictionary
print(dict0)
print(type(dict0))  


my_list = [64, 34, 25, 12, 22, 11, 90]  # print the sorted list
print(my_list)
sorted_list = sorted(my_list)
print(sorted_list)

my_list3 = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]  #print a 2nd index elemet
print(my_list3[2])



dict1 = {"Name": "John", "Age": 30}  #combined 2 dictionaries in 1
dict2 = {"City": "New York", "Country": "USA"}
dict1.update(dict2)
print(dict1)

my_list = ["Apple", "Banana", "Cherry", "Apple", "Banana"] #list into set
my_set = set(my_list)
print(my_set)

