# Program for Reversing a list using loop.
list = [20,40,60,80,85]
print("list is",list)
length = len(list)
rev_list = [ ]
for i in range(length-1,-1,-1):
    rev_list.append(list[i])
print("list in Reverse order is", rev_list) # reverse order