# # getting input from user

name = input("What is your name? ")
print(name + " is learning python")
print(name + " is eating coconut for breakfast")
#  input is always of type str

x = input("Write a number:") 
x / 2
print(float(x)/2)

print(str(123))
print(int("8"))


'''

We will now look at LISTs

'''

int_list = [1, 2, 3] 
string_list = ['abc', 'defghi']

empty_list = []

mixed_list = [1, 'abc', True, 2.34, None]

nested_list = [['a', 'b', 'c'], [1, 2, 3]]

# # The elements of a list can be accessed via an index

names = ['Alice', 'Bob', 'Craig','billy bob jr', 'Diana', 'Eric'] 
print(names[0]) # Alice 
print(names[2]) # Craig

# # Indices can also be negative which means counting from the end of the list

print(names[-1]) # Eric 
print(names[-4]) # Bob

# # Lists are mutable, so you can change the values in a list

names[0] = 'Ann' 
print(names) # Outputs ['Ann', 'Bob', 'Craig', 'Diana', 'Eric']

# #Append object to end of list with L.append(object).
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric'] 
names.append("Sia") 
print(names) # Outputs ['Alice', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

# #Add a new element to list at a speciﬁc index. L.insert(index, object)
names.insert(1, "Nikki") 
print(names) # Outputs ['Alice', 'Nikki', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

# #what if I need to add many names?
names.extend(["Liya", "Niharika"]) 
print(names) 

# # Remove the ﬁrst occurrence of a value with L.remove(value)
names.remove("Bob") 
print(names) # Outputs ['Alice', 'Nikki', 'Craig', 'Diana', 'Eric', 'Sia']

# # Get the index in the list of the ﬁrst item whose value is x. 
names.index("Alice") #0

# #Count length of list
len(names) #6

#count occurrence of any item in list
a = [1, 1, 1, 2, 3, 4] 
a.count(1) #3

# #Reverse the list
a.reverse()

# # Remove and return item at index (defaults to the last item) with L.pop([index])
names.pop() # Outputs 'Sia'

# join lists
list1 = [1,2,3]
list2 = [3,4,5]
list = list1 + list2
print(list)

nums = [1,2,3,4,5,6]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)