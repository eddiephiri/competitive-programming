def isSubset( a1, a2, n, m):
    for num in a2:
        if num not in a1:
            return "No"
        elif a2.count(num) > a1.count(num):
            return "No"
    return "Yes"