from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from.models import User_details
# from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def User_details_save(request):
    if request.method=="POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = User_details.objects.create(phone=phone, password=password)
        user.save()
        # messages.error(request, "incorrect password and email")
    return render(request, 'index.html')
        