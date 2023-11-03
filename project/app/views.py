from django.shortcuts import render
from .models import Data

# Create your views here.
def index(request):
    if request.method == "POST":
        b_name = request.POST['b_name']
        b_number = request.POST['b_number']
        data = Data.objects.create(book_name = b_name,book_number = b_number)

        data_read = Data.objects.filter().all()

        Data.objects.filter(book_name = "Book1").update(book_number=12)
        Data.objects.filter(book_name = "Book3").delete()
        return render(request,"index.html",{'data_read':data_read})
    return render(request,"index.html")