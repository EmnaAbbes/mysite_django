from django.shortcuts import render

def acceuil(request):
        if request.user.is_authenticated:
                request.session['username'] = request.user.username
        return render(request,'acceuil.html')


