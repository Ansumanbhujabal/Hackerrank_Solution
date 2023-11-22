def nonDivisibleSubset(k, s):
    result_set = set()

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if (s[i] + s[j]) % k != 0:
                result_set.add(s[i])
                result_set.add(s[j])

    result_list = len(result_set)
    return result_list-1


# Example usage:
k_value = 4
s_values = [1, 7, 2, 4]
result = nonDivisibleSubset(k_value, s_values)
print(result)
