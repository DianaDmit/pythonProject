per_cent = {'ТКБ': 5.6,'СКБ': 5.9,'ВТБ': 4.28,'СБЕР': 4.0 }
money = int(input("Введите ваше значение:"))
B1 = int((per_cent['ТКБ'])*(money/100))
B2 = int((per_cent['СКБ'])*(money/100))
B3 = int((per_cent['ВТБ'])*(money/100))
B4 = int((per_cent['СБЕР'])*(money/100))
deposit= [B1, B2, B3, B4]

print(list(map(int, deposit)))
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать: {} рублей.'.format(max_deposit))