# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    for i in range(0,len(arr)):
        count=[0]*6
        for bird in arr:
            count[bird]+=1
        return count.index(max(count)) 