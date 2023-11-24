from django.http import HttpResponse
from django.shortcuts import render
from .forms import userform

def calc(request):
    fn=userform()
    finalans=0
    data={'form': fn}
    try:
        if request.method=="GET":
            n1=int(request.GET.get('num1'))
            op=request.GET.get('op')
            n2=int(request.GET.get('num2'))
            if op=='+':
                finalans=n1+n2
            elif op=='-':
                finalans=n1-n2
            elif op=='*':
                finalans=n1*n2
            else:
                finalans=n1/n2
            data={'form': fn, 'final':finalans}
    except:
        pass
    return render(request, "calculator.html", data)