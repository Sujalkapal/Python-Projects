sum_odd_digits = 0
sum_even_digits = 0
total = 0

#12345678912345
card_num = input("Enter a credit card number: ")
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")
card_num = card_num[::-1]
print(card_num)

for x in card_num[::2]:
    sum_odd_digits += int(x)
print(sum_odd_digits)

for x in card_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += int(x)
print(sum_even_digits)

total = sum_odd_digits + sum_even_digits
print(total)

if total % 10 == 0:
    print("VALLID")
else:
    print("INVALID")