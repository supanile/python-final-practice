def cal_age(n, m, y):
    oat = n + y
    jai = m + y
    return oat, jai

n, m, y = [int(x) for x in input().split()]

oat, jai = cal_age(n, m, y)

print(f"oat: {oat}, jai: {jai}")
