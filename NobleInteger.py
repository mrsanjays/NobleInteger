def NobleInteger(Array):
    Array.sort(reverse=True)
    """
    Approach sort reverse and mark how many elements
    are greater than its value 
    Based on Ranking Concept
    """

    count=[0]
    prev_value=Array[0]
    current_count=0
    for i in range(1,len(Array)):
        if prev_value!=Array[i]:
            count.append(i)
            current_count=i
        else:
            count.append(current_count)
    for i in range(len(Array)):
        if Array[i]==count[i]:
            return 1
    return -1
if __name__ == '__main__':
    Array=list(map(int,input().split()))
    print(NobleInteger(Array))
"""
Noble Integer
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.
Example Input

Input 1:

A = [3, 2, 1, 3]
Input 2:

A = [1, 1, 3, 3]


Example Output

Output 1:

1
Output 2:

-1
"""