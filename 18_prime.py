def check_prime(num):
    flag = 0
    for data in range(2,num+1):
        if num%data==0:
            flag = flag+1
            break
    if flag == 0:
        return True
    else:
        return False

num = int(input())
print(check_prime(num))