from django.shortcuts import render, redirect
from apps.bill_tracker.models import BillItem

def index(request):
    if 'user_id' in request.session:
        context = {
            'bills' : BillItem.objects.filter(user_id = request.session['user_id'])
        }
        return render(request, 'bill_tracker/index.html', context)

    return redirect('travel_app:login')

def create_bill(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        description = request.POST['html_description']
        amount = request.POST['html_amount']

        BillItem.objects.create(
            user_id = user_id,
            description = description,
            amount = amount
        )

        return redirect('bill_tracker:index')
    return render(request, 'bill_tracker/index.html')

def delete_bill(request, bill_id):
    bill = BillItem.objects.get(id = bill_id)
    bill.delete()
    return redirect('bill_tracker:index')

def edit_bill(request, bill_id):
    context = {
        'bill' : BillItem.objects.get(id = bill_id)
    }
    return render(request, 'bill_tracker/edit_bill.html', context)

def update_bill(request, bill_id):
    if request.method == 'POST':
        bill = BillItem.objects.get(id = bill_id)
        bill.description = request.POST['html_description']
        bill.amount = request.POST['html_amount']
        bill.save()

        return redirect('bill_tracker:index')
    return render(request, 'bill_tracker/index.html')