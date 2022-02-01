## Установка pylint 

sudo python3 -m pip install pylint


## Запуск проверки

pylint example1.py

echo $?


Анализируем сообщения, пытаемся пофиксить
 
## Запуск на определенных правилах

pylint --disable=W0614 example1.py


## Запускаем в параллель

pylint -j 4 example1.py

