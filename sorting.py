def sorting(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        a = arr.pop()
        
    greater_num = []
    lower_num = []
    
    for num in arr:
        if num>a:
            greater_num.append(num)
        else:
            lower_num.append(num)
            
    return sorting(lower_num) + [a] + sorting(greater_num)

print(sorting([2,1,4,10,23,21,3,4,5,0,6,7]))

/*
Algo:
1. check for the length of array 
If => length < 1 return array
else => take the last element as pivot
2. for every num in array:
    if => num > pivot, Put num in greater_num[]
    else => Put num in lower_num[]
3. return greater_num[] + [pivot] + lower_num
    
*/
