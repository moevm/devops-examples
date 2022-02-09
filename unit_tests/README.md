## Установка unittest

Обычно входит в базовую установку Python. Если нет - используйте pip

## Тестируемое приложение
В файле calculator.py находится код простого калькулятора


## Запуск проверки

python unit_tests.py -v

//-v используется для подробного вывода результатов

Ожидаемый результат:  
test_add (__main__.TestCalculator) ... ok  
test_divide (__main__.TestCalculator) ... FAIL  
test_multiply (__main__.TestCalculator) ... ok  
test_subtract (__main__.TestCalculator) ... ok  


## Задание
Один из тестов нашел ошибку. Какой? Что он проверяет? Попробуйте найти ошибку в коде (ошибка в calculator.py, не в тестах). Какие еще тесты можно добавить?
