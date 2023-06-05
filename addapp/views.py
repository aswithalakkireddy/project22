from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def add(request):
    x = request.GET["t1"]
    y = request.GET["t2"]
    i = int(x)
    j = int(y)
    z = i + j
    res=HttpResponse("the sum is:"+str(z))

