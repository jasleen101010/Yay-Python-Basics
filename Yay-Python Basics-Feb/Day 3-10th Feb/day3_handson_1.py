is_good_customer = input("Is the Customer good? : ")
customerAge = int(input("What's his/her Age : "))

price = 1000
discount = 0

if is_good_customer == "Yes":
    if customerAge < 18:
        discount = price * 0.5
    elif customerAge >= 65:
        discount = price * 0.4
    else:
        discount = price * 0.3

else:
    if customerAge < 18:
        discount = price * 0.2
    elif customerAge >= 65:
        discount = price * 0.1
    else:
        discount = 0

print(f"The Customer will Pay : ${price - discount}")