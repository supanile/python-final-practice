def maxmin(num):
    num_list = []

    for i in range(num):
        value = int(input(f"Enter value[{i+1}]: ")) 
        num_list.append(value)

    max_value = max(num_list)
    min_value = min(num_list)

    print("Maximum value:", max_value)
    print("Minimum value:", min_value)

num = int(input("Enter n: "))

maxmin(num)