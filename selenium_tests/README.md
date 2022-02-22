## Setup

Скачиваем драйвер и устанавливаем зависимости

https://github.com/mozilla/geckodriver/releases

wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
tar -xvzf geckodriver-v0.30.0-linux32.tar.gz
sudo python3.7 -m pip install selenium




## Run 

PATH="./:$PATH" python3.7 main.py https://etu.ru


## Run headless

sudo apt install xvfb

./run_headless.sh
