nums = [0,10,6,4,7,54,1,88,79,11,45,54,19,59,21,15,23,18]
counter = 1

arr = []
flag = False
for i in nums:
    if i % 6 == 0 and counter % 6 == 0:
        arr.append(i)
        flag = True
    counter += 1

if flag:
    arr.sort()
    # print("\n",arr,"\n")
    # arr =  # -> {} is empty dictionary
    for something in set(arr):
        print(something, end=" - ")

else:
    print("\nNothing")
