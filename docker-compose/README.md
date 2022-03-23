## networks

Создание сети для конфигурации

docker-compose -f ./docker-compose-network.yml up

Задание сети по умолчанию

docker-compose -f ./docker-compose-network-default.yml up

Задание ссылки на внешнюю сеть

docker-compose -f ./docker-compose-network-external.yml up
