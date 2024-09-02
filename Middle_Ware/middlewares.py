def my_middleware(get_response):
    print('One Time Initializations')  # This runs only once when the middleware is loaded
    def my_func(request):
        print("This is Before View")   # This runs for every request
        response = get_response(request)
        print('This is After View')    # This runs after the view has processed the request
        return response
    return my_func



# Class BasedMiddleware
class my_middleware:
    def __init__(self,get_response):
        print('One Time Initializations')
        self.get_response=get_response

    def __call__(self,request):
        print("This is Before View")
        response=self.get_response(request)
        print("This is After View")
        return response


#Family middleware Work
class Father:
    def __init__(self, get_response):
        # This is executed only once when the server starts.
        # It's used for one-time initializations or setup.
        print('One Time Father Initializations')
        self.get_response = get_response
    def __call__(self, request):
        # This method is called every time a request is made.
        # Code here is executed before the view function is called.
        print("This is Father Before View")
        # The get_response method is called to continue processing the request.
        response = self.get_response(request)
        # Code here is executed after the view function has returned a response.
        print("This is Father After View")
        # The response is returned to the client.
        return response

class Mother:
    def __init__(self,get_response):
        print('One Time Mother Initializations')
        self.get_response=get_response

    def __call__(self,request):
        print("This is Mother Before View")
        response=self.get_response(request)
        print("This is Mother After View")
        return response
    
class Child:
    def __init__(self,get_response):
        print('One Time Child Initializations')
        self.get_response=get_response

    def __call__(self,request):
        print("This is Child Before View")
        response=self.get_response(request)
        print("This is Child After View")
        return response


#MiddleWare Hooks
from typing import Any
from django.http import HttpResponse
#ProcessMiddleWare
class ProcessMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_view(request,*args,**kwargs):
        # return HttpResponse("This is Before View")
        return None


#Exceptions Occur
class ExceptionsMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        print('Exceptions Occurd')
        class_name=exception.__class__.__name__
        print(class_name)
        return HttpResponse(f"An Error occured {exception}")
    
#Templates
class MyTemplates_Middleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_template_response(self,request,response):
        print("Process Tem Response MiddleWare From Middleware")
        response.context_data['name']="nasir"
        return response


#Views.py
def Home(request):
    print('Iam View')
    return HttpResponse("This Is View ")
    # return render(request,'Dashboard/dashboard.html')
def Except(request):
    print('Iam Except')
    a=10/0
    return HttpResponse("This Is Exceptions ")
    # return render(request,'Dashboard/dashboard.html')
from django.template.response import TemplateResponse
def user_info(request):
    print("Iam User Info ")
    context={'name':'Rahul'}
    return TemplateResponse(request,'Dashboard/dashboard.html',context)

#Settings.py
'test_study.middlewares.my_middleware'
'test_study.middlewares.Father',
'test_study.middlewares.Mother',
'test_study.middlewares.Child',
'test_study.middlewares.ExceptionsMiddleWare',
'test_study.middlewares.ProcessMiddleWare',
'test_study.middlewares.MyTemplates_Middleware',

#Project Site Under Constractions
class SiteConstractions:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("Iam Run Before View")
        response=HttpResponse("The Site is Under Constractions")
        print("Iam Run After The View ")
        return response
#Call the middleWare From Setting.py 
'test_study.middlewares.SiteConstractions'