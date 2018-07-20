from django.shortcuts import render, HttpResponse, redirect
# from django.contrib import messages
# from .models import User, Message, Comment
# import bcrypt



def index(request):
    return render(request, 'belt_app/index.html')

def travels(request):
    return render(request, 'belt_app/homepage.html')

def addtrip(request):
    return render(request, 'belt_app/addplan.html')

def viewplan(request, idnumber):
    return render(request, 'belt_app/viewplan.html')

def logout(request):
    # request.session.clear()
    return redirect('/')















# def login(request):
#     result = User.objects.filter(email = request.POST['email']).values()
#     if len(result)>0:
#         if bcrypt.checkpw(request.POST['password'].encode(), result[0]['password'].encode()):
#             request.session['first_name'] = result[0]['first_name']
#             request.session['userid'] = result[0]['id']
#             request.session["type"] = "login"
#             return redirect('/wall')
#     messages.error(request, 'Login Failed', extra_tags = 'login')
# # can call by messages".error" --> if message.level == DEFAULT_MESSAGE_LEVELS.ERROR
#     return redirect('/')

# def register(request):
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for tag, error in errors.items():
#             messages.error(request, error, extra_tags = tag)
#         return redirect('/')
#     else:
#         request.session["first_name"] = request.POST["first_name"]
#         request.session["type"] = "register"
#         pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
#         User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
#         this_user = User.objects.filter(email = request.POST['email']).values()
#         request.session['userid']= this_user[0]['id']
#         return redirect('/wall')

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