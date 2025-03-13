from django.shortcuts import render

def contacts(request):
 return render(request,'contacts_page/contacts.html')