tickets = int(input("Введите необходимое количество билетов:"))
price = 0
for i in range(tickets):
    age = int(input("Возраст посетителя для билета:"))
    if age < 18:
        price = price + 0
    elif 18 <= age < 25:
        price = price + 990
    else:
        price = price + 1390
if tickets > 3:
    print("Сумма к оплате с учетом скидки: ", (price - (price / 100) * 10), "рублей")
else:
    print("Сумма к оплате: ", price, "рублей")

