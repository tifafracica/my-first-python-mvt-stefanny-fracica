from django.shortcuts import render
from .models import Relative
import datetime

# Create your views here.
def show_relatives(request):
    relative1 = Relative(first_name='Marina', last_name='Barboza', age=53, birthday=datetime.date(1959, 2, 10))
    relative2 = Relative(first_name='Ana', last_name='Fracica', age=35, birthday=datetime.date(1987, 9, 10))
    relative3 = Relative(first_name='German', last_name='Medina', age=33, birthday=datetime.date(1989, 10, 17))
    return render(request, 'all_relatives.html', {'relatives': [relative1, relative2, relative3]})
    