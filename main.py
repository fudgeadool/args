#args means i can use as many arguments as possible
def sum(*args):
  total = 0
  for arg in args:
    total+= arg
  return total

print(sum(2,3,4,5,7,7,8,8,8,8,88,8,9,9,54,44,4,4,))


#kwargs means using key values that are limitless