def sum(list):
  if list == []:
    return 0
  print(list[0], list[1:])
  return list[0] + sum(list[1:])


print(sum([5]))