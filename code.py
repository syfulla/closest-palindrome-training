def is_palindrome(n):
    if n==n[::-1]:
        return True
    else:
        return False

def convert_to_str(n):
    n=str(n)
    return n

def nearest_palindrome(n):
    rp_num=(n)-1
    while not is_palindrome(convert_to_str(abs(rp_num))):
        rp_num-=1
    sp_num=int(n)+1
    while not is_palindrome(convert_to_str(abs(sp_num))):
        sp_num+=1
    if abs(n-(rp_num))>abs(n-(sp_num)):
        return sp_num
    else:
        return rp_num
n=int(input())
print(nearest_palindrome(n))
