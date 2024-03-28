"""
def f1(a,b):
    print("a=",a,"b=",b)
f1(4,5)
"""
def f1(l1):
    print(sum(l1))
print("Enter four number")
list=[int(i) for i in input().split(",")]
f1(list)