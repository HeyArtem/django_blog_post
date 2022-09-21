# Самая наипростейшая модель Django

### Алгоритм

mkdir django_test = создали директорию<br/>
cd django_test = <br/>python3 -m venv venv= создали виртуалку<br/>
source venv/bin/activate = активировали виртуалку 

sudo apt update  = обновит все пакеты<br/>
sudo apt upgrade -y = будет устаналивать их (-y значит я согласен)<br/>
sudo apt autoremove = очистка от ненужных и временных файлов, делать периодически.<br/>
sudo apt autoclean = подчистка за autoremove

pip install -U pip = установили  pip <br/>
pip install django =<br/>
pip install -U setuptools<br/>  pillow  = установили setuptools bs4 	requests  pillow<br/>

django-admin startproject app = создаю  проект аpp(это имя, лучше всегда такое)<br/>
cd  app = перемещаемся в наш app для проверки сделать ls (увидим: имя 	проекта и  manage.py)<br/>
django-admin startapp имяПрилож_app  = создаем приложение (имя новое, лучше добвавить app)<br/> 
	  [python manage.py startapp имяПрилож_app  = альтернативное написание команды]<br/>
Для проверки: после создания приложения в папке app будут лежать 
app, manage.py, приложение_app (мое приложение)<br/>


запустить проект в vsc
	code . = запуск в VSC через терминал (убедись, что в директории с app и venv)<br/>  
	Убедится, что виртуалка запущена!
django-admin help = выведет команды




python manage.py runserver = просто тест  
 После создания приложения, нужно его зарегистрировать, 

 * регистрирую приложение в файле setting — в разделе: INSTALLED_APPS — пишу имя приложения-
'test_djan_blog'




models — фаил для моделей
views — фаил для функций и классов
urls — для формирования маршрутов, путей

 * создал папку templates

 * присоединяю папку templates к базе данных ('DIRS': [os.path.join(BASE_DIR, "templates")],)
    
 * в models.py создаю модели, 
 * создаю директорию media

 * После создания моделей, выполнить миграции (создание таблиц)  [$ python manage.py, makemigrations (альтернативная команда $ ./manage.py 	makemigrations)
$ ./manage.py migrate]



Для того что бы увидеть модели в админке их нужно зарегистрировать в файле admin.py (у каждого приложения свой фаил).

Для доступа к админке нужно создать суперползователя (админ сайта). 
Создаем суперпользователя
$ python manage.py createsuperuser
	Username (leave blank to use 'heyartem'): admin
	Email address: не заполняю
	Password: admin
	Password (again): admin

запускаю сервак ($ ./manage.py runserver), вхжу в админку (http://127.0.0.1:8000/admin/)
создаю несколько постов