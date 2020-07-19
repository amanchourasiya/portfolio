from django.shortcuts import render


def port(request):
    return render(request, 'portfolio.html', {})
