from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#
#     return render(request,"results.html",
#                   {'result1':res1,'result2':res2,'result3':res3, 'result4':res4})
# # def about(request):
# #     return render(request,"about.html")
# #
# # def contact(request):
# #     return render(request,"contact.html")