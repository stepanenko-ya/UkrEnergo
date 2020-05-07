from django.shortcuts import render
from. models import Catalog


def main(request):

    list_name = Catalog.objects.all()

    x = request.GET.get('n')
    if x:

        g = ""

        for i in list_name:
            if i.name.find(x) == 0:
                g = Catalog.objects.filter(id=i.id)
                print(i)

        if not g:
            g = Catalog.objects.filter(phone=x)
            if not g:
                error_massage = "Не обнаружено"

        print(g)

    if request.method == "POST":
        e = request.POST['new']
        phone = request.POST['phone']
        address = request.POST['address']

        f = Catalog.objects.create(name=e, phone=phone, address=address)

    m = request.GET.get('z')
    Catalog.objects.filter(name=m).delete()

    return render(request, 'main/main.html', locals())







