question = input("Are you a boy?")
height = float(input("Enter your height:"))
is_a_girl=False
if question == "No":
    is_a_boy = False
else:
    is_a_boy = True

if is_a_boy:
    if height>=5.80:
        print("You are tall")
    else:
        print("You are not tall")
elif is_a_girl:
    print("You are a girl")
else:
    print("I dont know")
