
string = input("PLease enter your own string:")

string_2 = ('')


for i in string:
    string_2 = i + string_2

print("\nThe Original String =", string)
print("\nThe Reversed String =", string_2)