x = [1,2,3,4,5,'b',6]

for i in x:

    try:
        if int(i) % 1 == int(i):
            pass
    except Exception as e:
        # print(f"Not an Integer : {i}")
        print(e.__class__)