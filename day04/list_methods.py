# append() : add element
# clear() : remove all elements
# extend() : add collection of elements to the list
# sort() : sort in ascending order
# reverse()
# copy()
# remove() : remove the specified element
# pop() : by default removes the last inserted element. removes the index element if specified
# insert() : insert specified element at the specified index
# index() : returns the index number of the specified element
# count() : returns the frequency of the specified element

# extend() : add collection of elements to the list
students=['a','b','c','d','e']
print(students)
group1=['f','g','h']
students.extend(group1)
print(students)

# sort() : sort in ascending order
numbers=[2,4,7,23,54,-2,-6]
print(numbers)

numbers.sort()
print(numbers)

n=[23,34,45,56,67,89]
n.sort(reverse=True)
print(n)

# reverse()
students.reverse()
print(students)

# index() : returns the index number of the specified element
subjects=['Math','Chemistry','Biology']
has_math='Math' in subjects
print(has_math)
print(subjects.index('Math'))