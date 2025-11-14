lst = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
print("Lenth Of The List: " , len(lst))
print("The First Eliment Of The List: " , lst[0])
print("The last Eliment Of The List: " , lst[-1])
lst.remove(6)
print("UPDATED LIST: " , lst)
lst.reverse()
print("REVERSED LIST: " , lst)
lst = lst[1:5]
print("Sliced List: " , lst)