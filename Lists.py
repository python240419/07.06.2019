st = "a b c a a"

# count how manhy times "a" appears?
print( st.split().count("a") );

# remove smallest item, and biggest item
list = [5, 70, 100, -20]
list.remove (max(list) )
list.remove (min(list) )
print(list)

# sort all letters
str2 = "c+c+g+e+s+y+a"
print (sorted( str2.split("+") ))

# concat lists
lst1 = [1,4,6]
lst2 = [7,8,9]
lst3 = lst1 + lst2;

# find the 2nd biggest and replace it with its value * 2
lst4 = [5, 9, -100, 3, 7, 343, 323]
lst4.sort()
lst4[-2] = lst4[-2] * 2
print(lst4)

lst4.sort(reverse=True)
print(lst4)
