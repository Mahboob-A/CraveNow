from django.shortcuts import render


def test(request): 
        template_path = 'home.html'
        return render(request, template_path)