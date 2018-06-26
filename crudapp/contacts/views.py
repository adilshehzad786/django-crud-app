from django.shortcuts import render, redirect  
from contacts.forms import ContactForm  
from contacts.models import Contacts  


##Index View (Home Page)
#Route '/' (localhost:8000)
def index(request):
    return render(request,'index.html')


##Create View
#Route '/create' (as per urls.py)
#If: this view is called with "POST" request then the form is validated
#and saved to database, and then redirected to route '/show'.
#Else: it will render the contact form in index.html and display it.
def create(request):  
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:  
        form = ContactForm()  
    return render(request,'create.html',{'form':form})


##Show View
#Route '/show'
#Retrieve all contacts data from database and send it to 'show.html' to be rendered.
def show(request):  
    contactData = Contacts.objects.all()  
    return render(request,"show.html",{'contactData':contactData})  


##Edit View
#Route /edit/<ID>
#@param int id Primary ID
#Retrieve contact based on <ID> and render it in 'edit.html'.
def edit(request, id):  
    contactData = Contacts.objects.get(id=id)  
    return render(request,'edit.html', {'contactData':contactData})  


##Update View
#Route 'update/<ID>'
#@param int id Primary ID/Key
#Retrieves contact data based on <ID>,and
#if: requested using POST method then save the data into database
#else: render edit.html form with contact data.
def update(request, id):  
    contactData = Contacts.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contactData)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'contactData': contactData})  


##Delete Request
#Route '/delete/<ID>'
#When called with Primary ID/Key, the appropiate entry is delete
#from database and redirected to show page.
def delete(request, id):  
    contacts = Contacts.objects.get(id=id)  
    contacts.delete()  
    return redirect("/show")