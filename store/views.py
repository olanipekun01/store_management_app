from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
    dept1 = len(Items.objects.all().filter(dept_id = 1))
    dept2 = len(Items.objects.all().values().filter(dept_id = 2))
    dept3 = len(Items.objects.all().values().filter(dept_id = 3))
    dept4 = len(Items.objects.all().values().filter(dept_id = 4))
    
    # items = Items.objects.all()
    # print(items.values())
    return render(request, 'index.html', {"dept1": dept1, "dept2": dept2, "dept3": dept3, "dept4":dept4})

@login_required
def micro(request):
    if request.method == 'POST':
        input_name = request.POST['input_name']
        input_amount = request.POST['input_amount']
        print("type ", type(input_amount))
        op_type = request.POST['op_type']
        item = Items.objects.all().filter(item_name=input_name)[0]
        if op_type == "add":
            if input_amount != "":
                if int(input_amount) > 0:
                    amnt = int(input_amount)
                    # print(Items.objects.all().filter(item_name=input_name))
                    item.amount += amnt
                    item.save()
                    micro_history = MicroHistory.objects.create(item_name=item.item_name, amount="+ "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                    micro_history.save()
                    return redirect('/micro')
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/micro')
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/micro')
        else:
            if input_amount != "":
                if int(input_amount) > 0:
                    if item.amount >= int(input_amount) :
                        amnt = int(input_amount)
                        item.amount -= amnt
                        item.save()
                        micro_history = MicroHistory.objects.create(item_name=item.item_name, amount="- "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                        micro_history.save()
                        return redirect('/micro');
                    else:
                        messages.info(request, 'Not enough in stock')
                        return redirect('/micro');
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/micro');
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/micro');
    items = Items.objects.all()
    return render(request, 'dept1.html', {'items': items})


@login_required
def haem(request):
    if request.method == 'POST':
        input_name = request.POST['input_name']
        input_amount = request.POST['input_amount']
        op_type = request.POST['op_type']
        item = Items.objects.all().filter(item_name=input_name)[0]
        if op_type == "add":
            if input_amount != "":
                if int(input_amount) > 0:
                    amnt = int(input_amount)
                    # print(Items.objects.all().filter(item_name=input_name))
                    item.amount += amnt
                    item.save()
                    haem_history = HaemHistory.objects.create(item_name=item.item_name, amount="+ "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                    haem_history.save()
                    return redirect('/haem');
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/haem')
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/haem')
        else:
            if input_amount != "":
                if int(input_amount) > 0:
                    if item.amount >= int(input_amount) :
                        amnt = int(input_amount)
                        # item = Items.objects.all().filter(item_name=input_name)[0]
                        item.amount -= amnt
                        item.save()
                        haem_history = HaemHistory.objects.create(item_name=item.item_name, amount="- "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                        haem_history.save()
                        return redirect('/haem');
                    else:
                        messages.info(request, 'Not enough in stock')
                        return redirect('/haem');
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/haem');
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/haem');
    items = Items.objects.all()
    return render(request, 'dept2.html', {'items': items})


@login_required
def chem(request):
    if request.method == 'POST':
        input_name = request.POST['input_name']
        input_amount = request.POST['input_amount']
        op_type = request.POST['op_type']
        item = Items.objects.all().filter(item_name=input_name)[0]
        if op_type == "add":
            if input_amount != "":
                if int(input_amount) > 0:
                    amnt = int(input_amount)
                    # print(Items.objects.all().filter(item_name=input_name))
                    item.amount += amnt
                    item.save()
                    chem_history = ChemHistory.objects.create(item_name=item.item_name, amount="+ "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                    chem_history.save()
                    return redirect('/chem');
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/chem')
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/chem')
        else:
            if input_amount != "":
                if int(input_amount) > 0:
                    if item.amount >= int(input_amount) :
                        amnt = int(input_amount)
                        # item = Items.objects.all().filter(item_name=input_name)[0]
                        item.amount -= amnt
                        item.save()
                        chem_history = ChemHistory.objects.create(item_name=item.item_name, amount="- "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                        chem_history.save()
                        return redirect('/chem');
                    else:
                        messages.info(request, 'Not enough in stock')
                        return redirect('/chem');
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/chem');
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/chem');
    items = Items.objects.all()
    return render(request, 'dept3.html', {'items': items})


@login_required
def histo(request):
    if request.method == 'POST':
        input_name = request.POST['input_name']
        input_amount = request.POST['input_amount']
        op_type = request.POST['op_type']
        item = Items.objects.all().filter(item_name=input_name)[0]
        if op_type == "add":
            if input_amount != "":
                if int(input_amount) > 0:
                    amnt = int(input_amount)
                    # print(Items.objects.all().filter(item_name=input_name))
                    item.amount += amnt
                    item.save()
                    histo_history = HistoHistory.objects.create(item_name=item.item_name, amount="+ "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                    histo_history.save()
                    return redirect('/histo');
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/histo')
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/histo')
        else:
            if input_amount != "":
                if int(input_amount) > 0:
                    if item.amount >= int(input_amount) :
                        amnt = int(input_amount)
                        # item = Items.objects.all().filter(item_name=input_name)[0]
                        item.amount -= amnt
                        item.save()
                        histo_history = HistoHistory.objects.create(item_name=item.item_name, amount="- "+str(amnt), bal=str(item.amount), dept=item.dept, slug=item.slug)
                        histo_history.save()
                        return redirect('/histo');
                    else:
                        messages.info(request, 'Not enough in stock')
                        return redirect('/histo');
                else:
                    messages.info(request, 'enter a valid amount')
                    return redirect('/histo');
            else:
                messages.info(request, 'enter a valid amount')
                return redirect('/histo');
    items = Items.objects.all()
    return render(request, 'dept4.html', {'items': items})


@login_required
def newstock(request):
    if request.method == "POST":
        item_name = request.POST['item_name']
        item_amount = request.POST['item_amount']
        dept = request.POST['dept']
        
        if Items.objects.all().filter(item_name=item_name).exists():
            return redirect("/"+dept)
        else:
            if dept == 'micro':
                Items.objects.create(item_id = len(Items.objects.all()), item_name=item_name, amount=item_amount, dept=Department.objects.all()[0])
                item = Items.objects.all().filter(item_name=item_name)[0]
                history = MicroHistory.objects.create(item_name=item.item_name, amount="+ "+str(item_amount), bal=str(item_amount), dept=item.dept, slug=item.slug)
                history.save()
            elif dept == 'haem':
                Items.objects.create(item_id = len(Items.objects.all()), item_name=item_name, amount=item_amount, dept=Department.objects.all()[1])
                item = Items.objects.all().filter(item_name=item_name)[0]
                history = HaemHistory.objects.create(item_name=item.item_name, amount="+ "+str(item_amount), bal=str(item_amount), dept=item.dept, slug=item.slug)
                history.save()
            elif dept == 'chem':
                Items.objects.create(item_id = len(Items.objects.all()), item_name=item_name, amount=item_amount, dept=Department.objects.all()[2])
                item = Items.objects.all().filter(item_name=item_name)[0]
                history = ChemHistory.objects.create(item_name=item.item_name, amount="+ "+str(item_amount), bal=str(item_amount), dept=item.dept, slug=item.slug)
                history.save()
            elif dept == 'histo':
                Items.objects.create(item_id = len(Items.objects.all()), item_name=item_name, amount=item_amount, dept=Department.objects.all()[3])
                item = Items.objects.all().filter(item_name=item_name)[0]
                history = HistoHistory.objects.create(item_name=item.item_name, amount="+ "+str(item_amount), bal=str(item_amount), dept=item.dept, slug=item.slug)
                history.save()
            return redirect("/"+dept)
    return render(request, 'index.html')


@login_required
def delete(request, slug):
    item = Items.objects.filter(slug=slug)
    dept = item[0].dept.dept_name
    items = Items.objects.filter(slug=slug).delete()
    return redirect("/"+dept)


@login_required
def history(request, pk):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
   
    # items = Items.objects.all()
    # print(items.values())
    if pk == 1:
        history = MicroHistory.objects.all().filter(dept=pk).order_by('-date_created')
        history = history.values()
    elif pk == 2:
        history = HaemHistory.objects.all().filter(dept=pk).order_by('-date_created')
        history = history.values()
    elif pk == 3:
        history = ChemHistory.objects.all().filter(dept=pk).order_by('-date_created')
        history = history.values()
    elif pk == 4:
        history = HistoHistory.objects.all().filter(dept=pk).order_by('-date_created')
        history = history.values()
    return render(request, 'history.html', {'history': history})


@login_required
def ItemHistory(request, pk, slug):
    if pk == 1:
        history = MicroHistory.objects.all().filter(slug=slug).order_by('-date_created')
    elif pk == 2:
        history = HaemHistory.objects.all().filter(slug=slug).order_by('-date_created')
    elif pk == 3:
        history = ChemHistory.objects.all().filter(slug=slug).order_by('-date_created')
    elif pk == 4:
        history = HistoHistory.objects.all().filter(slug=slug).order_by('-date_created')
        
    return render(request, 'history.html', {'history': history})

def login(request):
     if request.method  == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credetials Invalid')
            return redirect('/login')
     else:
        return render(request, 'login.html')

@login_required    
def logout(request):
    auth.logout(request)
    return redirect('/')
