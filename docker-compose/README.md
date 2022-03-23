## networks

Создание сети для конфигурации

docker-compose -f ./docker-compose-network.yml up

Задание сети по умолчанию

docker-compose -f ./docker-compose-network-default.yml up

Задание ссылки на внешнюю сеть

docker-compose -f ./docker-compose-network-external.yml up


## healthcheck 

docker-compose -f ./docker-compose-healthcheck.yml up

## volumes

Работа с существующим volume

docker-compose -f ./docker-compose-volumes-external.yml up 


Автоматическое создание нового volume 

docker-compose -f ./docker-compose-volumes.yml up

## profiles

docker-compose --profile dev -f docker-compose-profiles.yml up

docker-compose --profile prod -f docker-compose-profiles.yml up
