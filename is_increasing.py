def is_increasing(n):
    prev= 10 
    while n > 0:
        current= n % 10
        if current>= prev:
            return False
        prev = current
        n //= 10
    return True
li=[123,413,642,678]
temp=[]
for i in li:
    res=is_increasing(i)
    temp.append(res)
print(temp)             #output: [True, False, False, True]
