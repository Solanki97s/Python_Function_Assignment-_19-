def my_fun(num):
    if num in range(1,20):
        print(num,"available in range")
    else:
        print(num,"Not available in range")
num=int(input("Enter number-"))
my_fun(num)