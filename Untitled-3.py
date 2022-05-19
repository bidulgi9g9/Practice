days = 5000
cnt = 2022
while True:
    if days > 365 and cnt % 4 != 0 :
        5000 - 365
        cnt += 1
    elif days > 365 and cnt % 4 == 0:
        5000 - 366
        cnt += 1
    else :
        break
print(days)