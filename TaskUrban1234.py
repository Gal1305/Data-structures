# "1-я программа"
print(9**0.5*5)   # - арифметика с типом данных "integer" и "float" (результат - float)

# "2-я программа"
print(99.9 > 99.8 and 1000 != 1000.1)   # - тип данных boolean со строгим оператором "and"

# "3-я программа"
print(2+2*2 == (2+2)*2)     # - сравнение результатов арифметических оперций с типом данных "integer"
                            # - (результат - bool)

# "4-я программа"
print(int(float('123.456')*10)%10)   # - строку переводим в float, умножаем на 10, чтобы
                                        # перенести 4-ку в целую часть
                                        # выполняем операцию остаток от деления "%" и получаем "4"