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
    print()
    print(new_dict)
