def calculate_sum(n):
    factorial = 1
    total_sum = 0

    for i in range(1, n + 1):
        factorial *= i
        total_sum += factorial / i

    return total_sum

# รหัสนักศึกษาสองตัวสุดท้าย
n = int(input("input n: "))

result = calculate_sum(n)
print("summation is:", result)


