age = [10, 25, 30, 18, 15, 66, 98, 55]


def f_age(x):
    if x<18:
        return False
    else:
        return True


y = filter(f_age,age)
for i in y:
    print(i)
