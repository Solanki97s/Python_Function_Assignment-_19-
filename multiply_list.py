def multiply_list(l1):
    result=1
    for i in l1:
        result*=i
    return result


print("Enter number saparated by comma")
l1=[int(i) for i in input().split(",")]
print(multiply_list(l1))
