def is_len():
    s = input().split()
    if len(s) < 6:
        return False
    else:
        return True


a = [x for x in input().split()]
lst = [x for x in a if len(x) >= 6]
lst1 = 5
lst3 = 7
print(*lst)
print(lst1)
print(lst3)
