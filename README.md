## Это пример докер и докер компос файла, приложения фастапи и базового счетчика редис.
***
### Склонировать приложение в свою дерикторию:
```shell
git clone https://github.com/Kvezac/ideal-guide
```
### Установка библиотек и зависимостей
```shell
poetry install
```
***
### Запуститите контейнер командой:
```shell
docker compose up --build
```
***
### [Перейдите по адрессу](http://localhost:8000/api/docs)

***
### [Или по этому адрессу](http://0.0.0.0:8000/api/docs)
***
### CTRL + C остановит контейнер
***
### Если докер в файлах ничего не менялось перезапустить контейнер 
### в фоновом режиме
```shell
docker compose up -d
```
***
### Если требуется пересоздать контейнер рекомендуется удалить образы для очистки места
```shell
docker compose down
```
***
### Перезапустите контейнер 
***

>[!NOTE] 
> #### На windows не открывает приложение по указанному адресу в контейнере. После запуска WSL из терминала
> #### открывает по адресу http://localhost:8000/api/docs
***
