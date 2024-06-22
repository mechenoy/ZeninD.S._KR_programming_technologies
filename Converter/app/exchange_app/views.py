from django.shortcuts import render
import requests

def exchange(request):
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    exchange = response.get('rates')

    if request.method == 'GET':
        context = {
            'currenties':exchange
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')
    
        coverted_amount = round((exchange[to_curr] / exchange[from_curr]) * float(from_amount), 2)

        context = {
            'currenties':exchange,
            'coverted_amount':coverted_amount,
            'from_curr':from_curr,
            'to_curr': to_curr,
            'from_amount':from_amount
        }
        
        return render(request=request, template_name='exchange_app/index.html', context=context)


