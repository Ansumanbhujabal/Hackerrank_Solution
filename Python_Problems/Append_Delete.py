def appendAndDelete(s, t, k):
    same_ele_count = 0

    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            same_ele_count += 1
        else:
            break

    remaining_to_delete = len(s) - same_ele_count
    remaining_to_append = len(t) - same_ele_count

    total_count = remaining_to_delete + remaining_to_append

    return "Yes" if k-total_count >= 0 and (k - total_count) % 2 == 0 or k >= len(s) + len(t) else "No"
