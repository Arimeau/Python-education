def func1(num):
    
    if num % 2 == 0 :
        return True

    return False

print(func1(54))

def max(list):

    current = list[0]
    for key in list: 
        if current < key:
            current = key
    return current

print(max([1,3,4,2,6,9]))

def three(*nums):
    tom = 0
    counter = 0
    for key in nums:
        counter +=1
        tom += key
    return tom / counter

print(three(4,2,7,3))