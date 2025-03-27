FROM python:3.6


RUN ls -la

# Данная строка работает как инвалидатор кэша сборки
# Если передать в docker build параметр --build-arg INVALIDATOR=222, то это автоматически инвалидирует все слои, идущие после данного ARG
# Но только на следующий запуск с --build-arg INVALIDATOR=222 кэш уже отработает штатно
ARG INVALIDATOR="1111"


RUN echo "ifdfdfsfsd"


CMD ["echo", "Hello World"]
