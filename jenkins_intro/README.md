## Начальная настройка

Запуск конфигурации:

docker-compose up -d

Получение начального админского пароля

`docker exec jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword`

Вход в систему (отключите Ad block)

http://localhost:8080/
