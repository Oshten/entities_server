# entities_server
Server for save same entities

Сервер предназначен для сохранения объектов в базе данных. Для каждого объекта дополнительно сохраняется время сохранения.
Поддерживает следующие запросы:
1) Запрос списка всех сохраненных объектов
   ```GET  /api/entities```

3) Запрос на добавление нового объекта
   ```POST /api/entities```<br/>
   Тело запроса должно иметь вид ```{'entity': '<some_object>'}```


### Запуск сервера
Для запуска сервера в корневой дериктории выполните следующую команду:
```
docker-compose up -d
```
Для остановки сервера:
```
docker-compose stop
```
Запуск сервера после остановки:
```
docker-compose start
```

### Тестирование
Для тестирования выполните команду:
```
pytest tests/test_api.py
```
