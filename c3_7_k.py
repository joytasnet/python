age = int(input('年齢>>'))
if age >= 40:
    price = 500
elif age <= 10:
    price = 300
else:
    price = 1000
print(f'金額は{price}円です')
