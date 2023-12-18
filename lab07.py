import math

def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

def A(n):
    a = [1]
    b = [1]
    for k in range(2, n + 1):
        b_k_minus_1 = b[k - 2]
        a_k_minus_1 = a[k - 2]
        a_k = 0.5 * (math.sqrt(b_k_minus_1) + 0.5 * math.sqrt(a_k_minus_1))
        a.append(a_k)
        b.append(a_k)
    return a

nested_list = [1, [2, [3, 4, [5]]]]
print(sum_nested(nested_list))

n = 10
result = A(n)
print(result)