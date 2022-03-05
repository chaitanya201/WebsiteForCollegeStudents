from django.shortcuts import render,HttpResponse
# Create your views here.

def photo(request):
    return render(request,'photo.html')
def contact(request):
    return render(request,'contact.html')
def creator_contact(request):
    return render(request,'creator contact.html')




