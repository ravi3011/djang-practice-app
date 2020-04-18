# this is my file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuation', 'analyzing_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("<h1>Error you didn't select to remove option</h1>")    

# def capfirst(request):
#     return HttpResponse("<h1>caplitalize first</h1>")

# def spaceremove(request):
#      return HttpResponse("<h1>space remover</h1>")


# def newlineremover(request):
#      return HttpResponse("<h1>new line remover</h1>")


# def charcount(request):
#      return HttpResponse("<h1>char counter</h1>")     