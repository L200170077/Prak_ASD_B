def binSearching(kumpulan, target):
    low = 0
    high = len(kumpulan) -1

    while low <= high:
        mid = (high + low) //2
        
        if kumpulan[mid] == target:
            return mid
        elif kumpulan[mid] < target:
            high = mid +1
        else :
            low = mid -1
            
    return -1

b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

"""
untuk mencari berapa jumlah tebakan yang digunakan oleh Binary Search
yaitu dengan menggunakan Logaritma basis 2 (log2(n))""" 
