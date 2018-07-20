from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Trip
import bcrypt

def index(request):
    return render(request, 'belt_app/index.html')

def travels(request):
    if 'userid' in request.session:
        context={
            "trips": Trip.objects.all(),
            "my_trips": Trip.objects.filter(travelers__id = request.session['userid'])
        }
        return render(request, 'belt_app/homepage.html', context)
    else:
        messages.error(request, 'NOT LOGGED IN', extra_tags = 'login')
        return redirect('/')

def addtrip(request):
    if 'userid' in request.session:
        return render(request, 'belt_app/addplan.html')
    else:
        messages.error(request, 'NOT LOGGED IN', extra_tags = 'login')
        return redirect('/')

def viewplan(request, idnumber):
    if 'userid' in request.session:
        context={
            "this_trip": Trip.objects.get(id=idnumber),
            "travelers": User.objects.filter(trips__id = idnumber).exclude(id=request.session['userid']),
        }
        return render(request, 'belt_app/viewplan.html',context)
    else:
        messages.error(request, 'NOT LOGGED IN', extra_tags = 'login')
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    result = User.objects.filter(email = request.POST['email']).values()
    if len(result)>0:
        if bcrypt.checkpw(request.POST['password'].encode(), result[0]['password'].encode()):
            request.session['first_name'] = result[0]['first_name']
            request.session['userid'] = result[0]['id']
            return redirect('/travels')
    messages.error(request, 'Login Failed', extra_tags = 'login')
    return redirect('/')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        request.session["first_name"] = request.POST["first_name"]
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        this_user = User.objects.filter(email = request.POST['email']).values()
        request.session['userid']= this_user[0]['id']
        return redirect('/travels')

def create(request):
    # errors = Trip.objects.trip_validator(request.POST)
    # if len(errors)



    this_user = User.objects.get(id=request.session['userid'])
    Trip.objects.create(destination = request.POST['destination'], plan = request.POST['plan'], travel_start_date = request.POST['travel_start_date'], travel_end_date = request.POST['travel_end_date'], planned_by = this_user)
    this_trip = Trip.objects.last()
    this_trip.travelers.add(this_user)
    this_trip.save()
    return redirect('/travels')

def join(request, idnumber):
    this_user = User.objects.get(id=request.session['userid'])
    this_trip = Trip.objects.get(id = idnumber)
    this_trip.travelers.add(this_user)
    return redirect('/travels')

def cancel(request, idnumber):
    this_user = User.objects.get(id=request.session['userid'])
    this_trip = Trip.objects.get(id = idnumber)
    this_trip.travelers.remove(this_user)
    return redirect('/travels')

def delete(request, idnumber):
    this_trip = Trip.objects.get(id = idnumber)
    this_trip.delete()
    return redirect('/travels')








































# def wall(request):
#     if 'userid' in request.session:
#         context = {
#             "all_messages" : Message.objects.all().order_by('-id'),
#             "all_comments" : Comment.objects.all(),
#         }
#         return render(request, 'wall_app/wall.html',context)
#     else:
#         messages.error(request, 'NOT LOGGED IN', extra_tags = 'login')
#         return redirect('/')

# def edit(request, idnumber):
#     context = {"users": User.objects.get(id=idnumber)}
#     return render(request, "semi_rest_users/edituser.html", context)

# def create(request):
#     email = request.POST['email']
#     User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
#     idnum= User.objects.get(email=email).id
#     return redirect('/users/'+str(idnum))

# def update(request):
#     idnumber = request.POST['idnumber']
#     b = User.objects.get(id=idnumber)
#     b.first_name = request.POST['first_name']
#     b.last_name = request.POST['last_name']
#     b.email = request.POST['email']
#     b.save()
#     return redirect('/users/'+idnumber)