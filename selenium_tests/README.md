## Setup

Скачиваем драйвер и устанавливаем зависимости

https://github.com/mozilla/geckodriver/releases

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz
tar -xvzf geckodriver-v0.35.0-linux64.tar.gz
pip install selenium
```



## Run 

PATH="./:$PATH" python main.py https://etu.ru


## Run headless

sudo apt install xvfb

./run_headless.sh
