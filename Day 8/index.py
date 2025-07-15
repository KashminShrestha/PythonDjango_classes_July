lst=[1,2,3,4,5,6,7,8,9,10]

lst.append(11)  # Adding 11 to the end of the list
print(lst[::-1])


name=["John", "Doe", "Jane"]
name.append("Smith")  # Adding "Smith" to the end of the name list
print(name)

name.insert(0, "Alice")  # Inserting "Alice" at index 1
print(name)

name.pop()
print(name)

nep_name =["Hari" , "sita", "Ram"]
name.extend(nep_name) #Extending name list with nep_name
print(name)

# name.clear()
# print(name)

copy_name=name.copy()
print("copy",copy_name)

count = name.count("John")
print(f"count of 'John':{count}")

name.remove("John")
print(name)
name.reverse()
print(name)

unsort=[2,1,5,7,3,9]
unsort.sort()
print(unsort)

print(name+unsort)