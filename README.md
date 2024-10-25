# 🌳 Laboratories of "Workshop on design and development of information systems"
## MIPT x SberTech
### Laboratory 1
🍄 **Task**: Нужно написать shell файл:
Который принимает на вход три параметра START|STOP|STATUS.
START запускает его в фоне и выдает PID процесса,
STATUS выдает состояние - запущен/нет,
STOP - останавливает PID
Сам shell мониторит утилизацию дискового пространства, количество свободных inode.
Выводит информацию в виде csv файла. Имя файла должно содержать timestamp запуска +
дату за которую мониторинг. Предусмотреть создание нового файла при переходе через сутки

🍄 **Solution**: src -> script.sh

🍄 **Description:** для запуска

```bash 
    sh script.sh START / STOP / STATUS
```

команда START создает два файла: `monitor.pid` и `monitor_{timestamp}.csv`, частота мониторинга 60 секунд. Команда STOP заканчивает мониторинг и удаляет созданные файлы.


### Laboratory 3
🍄 **Task**: Задание состоит из двух частей:
1. Через dockerfile собрать свое рабочее приложение и отправить его в docker-registry
2. Собрать через docker-compose двух или более компонентное приложение (состоящее из более чем одного docker image), где один компонент БД и научить их ""общаться"" между собой. "

🍄 **Solution**: приложение на flask и БД на Postgres 

🍄 **Description:** скрипт start.sh собирает приложение и стартует два контейнера: с базой данных и самим приложением.
Приложение содержит эндпоинты:
- http://127.0.0.1:8080/ - создает табличку в БД и выводит сообщение;
- http://127.0.0.1:8080/add - POST метод добавляет строчки в БД;
пример запроса:
```bash 
    curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"name":"Lera"}' \
    http://127.0.0.1:8080/add
```