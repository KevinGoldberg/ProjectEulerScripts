#Problem 76

import time

"""
100: [99, 1]
99:  [98, 1, 1], [98, 2]
98:  [97, 1, 1, 1], [97, 2, 1], [97, 3]
97:  [96, 1, 1, 1, 1], [96, 2, 1, 1], [96, 2, 2], [96, 3, 1], [96, 4]
etc.

10: 1 [9, 1]
9: 2 [8, 2], [8, 1, 1]
8: 3 [7, 3], [7, 2, 1], [7, 1, 1, 1]
7: 5 [6, 4], [6, 3, 1], [6, 2, 2], [6, 2, 1, 1], [6, 1, 1, 1, 1]
6: 7 [5, 5], [5, 4, 1], [5, 3, 2], [5, 3, 1, 1], [5, 2, 2, 1], [5, 2, 1, 1, 1],
    [5, 1, 1, 1, 1, 1]
5: 9 [4, 4, 2], [4, 4, 1, 1], [4, 3, 3], [4, 3, 2, 1], [4, 3, 1, 1, 1],
    [4, 2, 2, 2], [4, 2, 2, 1, 1], [4, 2, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1]

1: 0:
2: 1: [1, 1]
3: 2: [2, 1], [1, 1, 1]
4: 4: [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]
5: 6: [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]
6: 8: [5, 1], [4, 2], [4, 1, 1], [3, 3], [3, 2, 1], [3, 1, 1, 1], [2, 1, 1,
        1, 1], [1, 1, 1, 1, 1, 1]

f = number of summations
g = number of summations with a 1

n | f(n) | g(n)
--|------|------
1     0      1
2     1      1
3     2      2
4     4      3
5     6      5
6     8      6
"""

def countSums(n):
        return sumCount(n, n-1)

def sumCount(n, t):
        if n == 0:
                return 1
        else:
                total = 0
                for i in range(1, t+1):
                        total += sumCount(n-i, min(i, n-i))
                return total

#To make this function faster, create a dictionary that updates
#the number of sums for each value so that that value can be accessed more
#quickly.

def updateCountSums(n, t, d):
        if n == 0:
                return 1
        if (n, t) in d:
                return d[(n, t)]
        else:
                total = 0
                for i in range(1, t+1):
                        total += updateCountSums(n-i, min(i, n-i), d)
                d[(n, t)] = total
        return total

def partition(n, d):
        return updateCountSums(n, n-1, d) + 1

def main():
        
        print(countSums(5))

        SC = dict()
                
        print("The answer to problem 76 is", updateCountSums(100, 99, SC))
        print("There are ", updateCountSums(115, 114, SC), "partitions of 115")

        even = [0]
        odd = []
        for i in range(1, 1000):
                #print("There are ", updateCountSums(i, i-1, SC), "partitions of ", i)
                if partition(i, SC) % 2 == 0:
                        even.append(i)
                else:
                        odd.append(i)
                if i % 100 == 99:
                        print(i)
                        print(len(even), "is even")
                        print(len(odd), "is odd")

        

if __name__ == '__main__':
        main()



