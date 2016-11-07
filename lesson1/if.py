# age = int(input("Enter your age: "))
# if age <= 5:
#     print("Go to kindergarden, kid!")
# elif age <= 16:
#     print("Go to school, boy")
# elif age <= 24:
#     print("Go to university, fellow student")
# else:
#     print("You're too old, go to work than")

def string_compare(str1, str2):
    if str1 == str2:
        return 1
    elif str1 > str2:
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3

print(string_compare('lala', 'learn'))