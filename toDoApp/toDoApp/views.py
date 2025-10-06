from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
    
    
def taskList(request):
    return render(request, 'tasks.html')