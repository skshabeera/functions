# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# counter1 = 0
# while counter1 < len(big_list):
#     small_list_length = len(big_list[counter1])
#     counter2 = 0
#     while counter2 < small_list_length:
#         print (big_list[counter1][counter2])
#         counter2 = counter2 + 1
#     counter1 = counter1 + 1
#     print ('') 


def marks():
    i=0
    while i<len(list1):
        j=0
        max=0
        while j<len(list1[i]):
            if list1[i][j]>max:
                max=list1[i][j]
            j+=1
        print(max)
        i=i+1
list1=[[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
marks()