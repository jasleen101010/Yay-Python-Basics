# string indexing 0 to n-1
randomString="girlscript yay"
print(randomString[8])
print(randomString[0:4])
print(randomString[4:12])
print(randomString[1::3])
# string indexing and slicing -1 to -n
newRandomString="National"
print(newRandomString[-1])
print(newRandomString[-5:-1])
print(newRandomString[-3::1])
# string slicing snippet
string='Red Panda'
print(string[-6:-2])
print(string[::-3])
print(string[-5: : 1])
# string formatting methods- 4 types
myName = "Jasleen"
myname = "Jasleen"
comp="Yay"
msg= myName+" is "+"a mentor at "+comp
print(msg)
print(f'{myname} is a mentor at {comp}')
print('{} is a mentor at {}'.format(myName,comp))
print('%s is a mentor at %s'%(myName,comp))
#string operations  
sampleString="Beautiful"
print(len(sampleString))
print(sampleString.upper())
print(sampleString.isdigit())
dig_str="I LOVE INDIA"
print((dig_str.isdigit()))
print(dig_str.lower())
