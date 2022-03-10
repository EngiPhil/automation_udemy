input_num = int(input("Please enter your number --- > "))

# Print table of given number but only display number where multiple is not divisible of 3, 5, 7

for i in range(1, 11):
    num = input_num * i
    print('tryin number ' + str(num))

    if (num % 3 != 0 and num % 5 != 0 and num % 7 != 0):
        print(num)
