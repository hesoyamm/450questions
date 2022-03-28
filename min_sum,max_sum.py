def Answer_for_Anin():  
    import math
    arr=[1,3,7,5,9]
    arr.sort()
    min_sum,max_sum=reduce(lambda x,y:x+y,arr[:len(arr)-1]),reduce(lambda x,y:x+y,arr[1:])
    return min_sum,max_sum
Answer_for_Anin()
