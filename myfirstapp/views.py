from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import*

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello Kashi")

def myfunctionabout(request):
    return HttpResponse("this is about section")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request, name, age):
    mydictionary = {
        "name":name,
        "age":age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request, 'index.html')

def mysecondpage(request):
    return render(request, 'second.html')

def mythirdpage(request):
    var = "hello there"
    greeting = "hey how are you?"
    fruits = ["apple","mango","banana"]
    num1, num2 = 3, 5
    ans = num1 > num2
    print(ans)
    mydictionary = {
        "var":var,
        "msg": greeting,
        "myfruits": fruits,
        "num1":num1,
        "num2":num2,
        "ans": ans
    }
    return render(request, 'third.html', context=mydictionary)

def myimagepage(request):
    return render(request, 'imagepage.html')

def myimagepage2(request):
    return render(request, 'myimagepage2.html')

def myimagepage5(request, imagename):
    myimagename = str(imagename);
    myimagename = myimagename.lower();
    print(myimagename)
    if myimagename == "hhh":
        var=True
    elif myimagename == "kkk":
        var=False
    mydictionary= {
        "var":var
    }
    return render(request, 'imagepage5.html', context=mydictionary)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mydictionary = {
        "var1" : request.POS['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method == "POST":
        form = FedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            mydictionary={
                "form":FedbackForm()
            }
            
            mydictionary["success"]= True
            mydictionary["successmsg"] = "Form submitted successfully"
            return render(request, 'myform2.html',context=mydictionary)
            
            # print(title)
            # print(subject)
            # var = str("form submitted"+ str(request.method))
            # return HttpResponse(var)
        else:
            mydictionary={
                'form':form
            }
            return render(request,'myform2.html', context=mydictionary)
    elif request.method =="GET":
        form = FedbackForm()
        mydictionary = {
            "form": form
        }
        return render(request,'myform2.html', context=mydictionary)
