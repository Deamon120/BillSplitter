import random
number_of_friends = int(input())
print()
if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    new_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friends):
        name_friend = input()
        new_dict[name_friend] = 0

    bill = int(input("Enter the total bill value:\n"))
    if bill % number_of_friends == 0:
        bill_for_all = bill // number_of_friends
    else:
        bill_for_all = round(bill / number_of_friends, 2)


    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky == "Yes":
        random_key = random.choice(list(new_dict.keys()))
        print(f"{random_key} is the lucky one!")
    else:
        print("No one is going to be lucky")
