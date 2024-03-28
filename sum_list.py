def sum_list(l1):
    sum=0
    for i in l1:
      sum+=i
    return sum

print("Enter number saparated by comma")
l1=[int(i) for i in input().split(",")]
print("sum of list is",sum_list(l1))