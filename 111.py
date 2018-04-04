"""
Ex.: A = [1,2,3], n = 3
Output = 216 (1+2+3 = 6, which is not prime so the output is 63)

Ex.: A = [1,5,3,4], n = 4
Output = 169 (1+5+3+4 = 13, which is prime so the output is 132)

Ex.: A = [-5,3,1,1,2], n = 5
Output = 4 (-5+3+1+1+2 = 2, which is prime so the output is 22)
"""

def fuck(n):
    total = sum(n)
    print(total)

    for i in range(2,total):
        if total % i == 0:
            return total**3

    return total**2


# print(fuck([1,2,3]))
# print(fuck([1,5,3,4]))
# print(fuck([-5,3,1,1,2]))
print(fuck([1,3,5,7,9]))
