i=input("введите слово для проверки ")
def ujn(i,r):
    if i[r] != i[-1-r]:
        return "нет"
    elif r < (len(i)+1)//2:
        return ujn(i,r+1)
    else:
        return "полендром"
print(ujn(i,0))
