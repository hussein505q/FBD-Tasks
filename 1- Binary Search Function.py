import math
def binarySearch(A, target):
  #1. here is to just print the whole array
  print("A = {}\n".format(A))
  low = 0
  high = len(A)-1
  while low<=high:
    mid = math.floor((low+high)/2)
    if target == A[mid]:
      #2. When the target fount, the array index returned as string, as if A starts from index 1 (not 0) up to last index
      return "If A[1 ... {}], target = A[{}] = {}".format(len(A), mid+1, target)
    elif target < A[mid]:
      high = mid-1
    else:
      low = mid+1
  #3. When the target is not found, a not-found message is returned as string
  return "The traget = {} not found in A[1 ... {}]".format(target,len(A))
if __name__ == "__main__":
  #4. here you can modify the array
  A = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
  #5. here you can modify the target value to searh
  target = 19
  #6. here is to just printed the output tring from the binarySearch() function
  print(binarySearch(A, target))