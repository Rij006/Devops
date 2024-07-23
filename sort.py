def sortSecond(val): 
	return val[1] 
my_list1 = [(1, 2), (3, 3), (1, 1)] 
my_list1.sort(key=sortSecond) 
print(my_list1) 
my_list1.sort(key=sortSecond, reverse=True) 
print(my_list1)
