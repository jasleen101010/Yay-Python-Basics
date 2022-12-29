a = list(map(int,input("\nEnter the numbers : ").strip().split()))
def greater(x):
     if x>5:
         return True
     else:
         return False
filtering=filter(greater,a)
for i in filtering:
    print(i)