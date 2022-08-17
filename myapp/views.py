from django.shortcuts import render,redirect,HttpResponse
from .models import Student,Blog

# Create your views here.
def loadhtml(request):
    
    data = Blog.objects.all
    return render(request, "index.html", )


def signup(request):
    if request.session.has_key('is_login'):
        return redirect(('/home'))
    return render(request, "register.html")



def savedata (request):
    if request.POST:
        sid = request.POST['sID']
        sname = request.POST['sName']
        semail = request.POST['sEmail']
        spassword = request.POST['sPassword']
        obj = Student(sID=sid, sName=sname, sEmail=semail, sPassword=spassword)
        obj.save()
    return redirect('/login')    


def login(request):
    if request.session.has_key('is_login'):
        return redirect(('/home'))
    if request.POST:
        semail = request.POST['sEmail']   
        spassword = request.POST['sPassword']
        count = Student.objects.filter(sEmail=semail, sPassword=spassword).count()

        if count>0:
            request.session['is_login']=True
            request.session['user_id'] = Student.objects.values('id').filter(sEmail=semail, sPassword=spassword)[0]['id']
            return redirect('/home')
             
        else:
            return redirect('/#')  

    return render(request, "login.html")    


def register(request):
    return render(request, "register.html")   
     

def home(request):
    data = Blog.objects.all
    return render(request, "home.html", {"data":data})



def About_us(request):
    return render(request, "about us.html")       

def Company(request):
    return render(request, "company.html")     

def sendEmail(request):
    return render(request, "sendEmail.html")   

def Services(request):
    return render(request, "services.html")


def logOut(request):
    del request.session['is_login']
     
    return redirect('/login')    


def webDesign(request):
    return HttpResponse("This is Web Design page")

def javaScript(request):
    return HttpResponse("This is Web JavaScript page")
    
def Html(request):
    return HttpResponse("This is Web Html page")     

def Css(request):
    return HttpResponse("This is Css page")     

def Freebies(request):
    return HttpResponse("This is Web Freebies page")     

def Tutorials(request):
    return HttpResponse("This is Web Tutorials page")      


def createpost(request):

    if request.POST:
        uid = request.POST['user_id']
        pname = request.POST['pname']
        ptitle = request.POST['ptitle']
        pdetail = request.POST['pdetail']
        img = request.FILES['img']
        obj = Blog(publisherName = pname,title=ptitle,postDetail = pdetail,image = img)
        obj.user_id_id = uid
        obj.save()
        return redirect('/home')
    return render(request, "createpost.html")

def Visit (request):
    return render(request, "visit.html")    
        
     


                  
            
        

