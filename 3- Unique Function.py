def unique(A):
  uniqueArray = []
  for element in A:
    #1. here is to add element from A[] to uniqueArray[] withou duplicating
    if element not in uniqueArray:
      uniqueArray.append(element)
  return uniqueArray
if __name__ == "__main__":
  A = [11, 12, 13, 14, 14, 15, 15, 15, 15, 17, 11, 11, 12, 14, 17, 18, 19, 16, 16]
  #2. here is to print the old and unique arrays
  print("A = {}\nUnique Array = {}".format(A, unique(A)))