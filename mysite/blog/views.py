from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("Ciao dal mio primo progetto Django!")
def home(request):
    context = {"nomeUtente": "Pietro"}
    return render(request, "home.html", context)

# In python tutte le funzioni sono automaticamente esportate,
# non c'è bisogno di un export esplicito come in JavaScript
