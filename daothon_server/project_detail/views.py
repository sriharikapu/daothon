from django.shortcuts import render

# Create your views here.
def project_detail(request):
    return render(request, 'project_detail.html', 
        {'project_name': 'aaa'})