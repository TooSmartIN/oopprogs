num = (input("enter a number"))
final_str = ' '
str_len = len(num)

for i in range(len(num)):
    if num[i] == '1':
        final_str = final_str+ 'one '
    
    if num[i] == '2':
        final_str = final_str+ 'two '   

    if num[i] == '3':
        final_str = final_str+ 'three '

print(final_str)

