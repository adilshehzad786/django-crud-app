from django.contrib import admin  
from django.urls import path  

#Using views defined in /contacts/views.py
from contacts import views

#Define Routes (in URL Patterns)
#Routes as in "localhost:8000/"
urlpatterns = [  
    #Django Admin Panel
    path('admin/', admin.site.urls),  


    #Index Route
    #localhost:8000/route
    path('', views.index),

    #Create Contact Route
    #localhost:8000/create
    path('create', views.create),  

    #Show/List Contacts
    #localhost:8000/show
    path('show',views.show),  

    #Edit Contact
    #localhost:8000/edit/<ID>
    path('edit/<int:id>', views.edit),

    #Update Contact
    #localhost:8000/update/<ID>
    path('update/<int:id>', views.update),  

    #Delete Contact
    ##localhost:8000/delete/<ID>
    path('delete/<int:id>', views.delete),  
]  