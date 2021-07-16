

a = [1,2,3,5,6,8,5,4,2,1,3,5,3,2,7,0,7,2,5,7,7,8,9,4,3,6,5,3,7]

more_than_3 = lambda some_list,check_val: [ item for item in some_list if item > check_val ]

print(more_than_3(a,5))

