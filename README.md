Primi passi con Django

Installa Django e crea il tuo primo progetto:  
- `pip install django`
- `django-admin startproject mysite`
- `cd mysite`
- `python manage.py runserver`


Crea una nuova app:  
`python manage.py startapp blog`


Mostra la tua prima pagina web con una view:  
- in blog/views.py scrivi:  
``` python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Ciao dal mio primo progetto Django!")
```

- collega la view a un URL.


Crea una pagina HTML usando un template.  

Passa dati dal view al template (es. un nome utente).  

*💡 Obiettivo: capire la struttura project / app / urls / views / templates.*
