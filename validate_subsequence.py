"""
Validate Subsequence
Given two non-empty arrays of integers, write a function that
determines whether the second array is a subsequence of the first
one.

A subsequence of an array is a set of numbers that aren't necessarily
adjacent in the same order as they appear in the array. For instance,
the numbers [1,3,4] form a subsequence of the array [1,2,3,4],
and so do the numbers [2,4]. Note that a single number in an array and
the array itself are both valid subseqneces of the array.
"""

"""
Tests:
1. { 
    "array" : [5,1,22,25,6,-1,8,10]
    "sequence" : [1,6,-1,10]
   }
   expected output: true
2. {
    "array": [5, 1, 22, 25, 6, -1, 8, 10],
    "sequence": [5, 1, 22, 25, 6, -1, 8, 10]
   }
   expected output: true
3. {
    "array": [5, 1, 22, 25, 6, -1, 8, 10],
    "sequence": [5, 1, 22, 6, -1, 8, 10]
    }
   expected output: true
4. {
    "array": [5, 1, 22, 25, 6, -1, 8, 10],
    "sequence": [22, 25, 6]
   }
   expected output: true
5. {
    "array": [5, 1, 22, 25, 6, -1, 8, 10],
    "sequence": [1, 6, 10]
   }
   expected output: true
6. {
    "array": [5, 1, 22, 25, 6, -1, 8, 10],
    "sequence": [5, 1, 22, 10]
   }
   expected output: true
7. {
    "array": [5, 1, 22, 25, 6, -1, 8, 10],
    "sequence": [5, -1, 8, 10]
   }
   expected output: true
8. {
    "array": [5, 1, 22, 25, 6, -1, 8, 10],
    "sequence": [25]
   }
   expected output: true
9. {
    "array": [1, 1, 1, 1, 1],
    "sequence": [1, 1, 1]
   }
   expected output: true
10. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 12]
    }
    expected output: false
11. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [4, 5, 1, 22, 25, 6, -1, 8, 10]
    }
    expected output: false
12. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [5, 1, 22, 23, 6, -1, 8, 10]
    }
    expected output: false
13. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [5, 1, 22, 22, 25, 6, -1, 8, 10]
    }
    expected output: false
14. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [5, 1, 22, 22, 6, -1, 8, 10]
    }
    expected output: false
15. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [1, 6, -1, -1]
    }
    expected output: false
16. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [1, 6, -1, -1, 10]
    }
    expected output: false
17. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [1, 6, -1, -2]
    }
    expected output: false
18. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [26]
    }
    expected output: false
19. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [5, 1, 25, 22, 6, -1, 8, 10]
    }
    expected output: false
20. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [5, 26, 22, 8]
    }
    expected output: false
21. {
     "array": [1, 1, 6, 1],
     "sequence": [1, 1, 1, 6]
    }
    expected output: false
22. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [1, 6, -1, 10, 11, 11, 11, 11]
    }
    expected output: false
23. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 10]
    }
    expected output: false
24. {
     "array": [5, 1, 22, 25, 6, -1, 8, 10],
     "sequence": [1, 6, -1, 5]
    }
    expected output: false   
"""

#Solution Number 1
def is_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
def isValidSubsequence(array, sequence):
    validation_index_list=[]
    if len(array)==len(sequence):
        if array!=sequence:
            return False
        else:
            return True
    for item in sequence:
        if item not in array:
            return False
        elif sequence.count(item)>array.count(item):
            return False
        else:
            validation_index_list.append(array.index(item))
    return is_ascending(validation_index_list)


#Solution Number 2, with while loop
#Idea of the solution is to traverse the array and the sequence once,
#In this case the time complexity will be O(n), where n is the length
#of the array and the depth complexity, will be O(1), 
def isValidSubsequence(array, sequence):
    arrayId=0
    seqId=0
    while seqId<len(sequence) and arrayId<len(array):
        if sequence[seqId]==array[arrayId]:
            seqId += 1
        arrayId += 1
    return seqId == len(sequence)

#Solution Number 3, with the for loop
#Time and space complexity will remain the same
def isValidSubsequence(array, sequence):
    seqId = 0
    for value in array:
        if seqId==len(sequence):
            break
        if sequence[seqId]==value:
            seqId += 1
    return seqId==len(sequence)