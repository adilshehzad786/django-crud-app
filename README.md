# CRUD Application in Django
We will create a simple app to store, edit and delete contacts information. The codes are commented enough for anyone to understand the flow.



Download/Clone repository and run following commands:

- Create Django CRUD project:
```
django-admin startproject crudapp
```

- In project directory, create application:
```
python manage.py startapp contacts
```

- Define model in /contact/models.py

- Create and define form fields /contacts/forms.py

- Create edit, index and show view in /contacts/templates/

- Define urls in /crudapp/urls.py

- Add 'contacts' app to main app in /crudapp/settings.py

- Migrate Models:
```
python manage.py migrate
```

- Run server:
```
python manage.py runserver
```
and, access application in browser **localhost:8000**



### TRY AND TWEAK STUFF
If model defination is changed, then run following commands:
```
python manage.py migrate --run-syncdb

python manage.py makemigrations

python manage.py migrate
```



For concerns related code / bug write me at chettri@live.com