from django.shortcuts import render,redirect
from testapp.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum, F
from testapp.models import CommonTotal
import datetime
common_total = CommonTotal.objects.create(total=0)




@login_required
def indexView(request):
    return render(request,'index.html',{'user':request.user })
# --------------------------------------------------------------
@login_required
def binaryView(request):
    return render(request,'binary.html')
# --------------------------------------------------------------
def regView(request):
    return render(request,'register.html',{'user':request.user })
# --------------------------------------------------------------
@login_required
def tableView(request):
    return render(request , 'tables-datatables.html')
# --------------------------------------------------------------

@login_required
def showProfile(request):
    return render(request,'pages-profile.html')
# --------------------------------------------------------------
@login_required
def profileSetting(request):
    return render(request,'pages-profile-settings.html')
# --------------------------------------------------------------
@login_required
def helpView(request):
    return render(request,'pages-faqs.html')
# --------------------------------------------------------------
@login_required
def transView(request):
    return render(request,'trans.html')
# --------------------------------------------------------------
@login_required
def searchView(request):
    return render(request,'pages-search-results.html')
# --------------------------------------------------------------
@login_required
def ticketView(request):
    return render(request,'apps-tickets-list.html')
# --------------------------------------------------------------
@login_required
def kyc(request):
    return render(request,'apps-crypto-kyc.html')
# --------------------------------------------------------------
@login_required
def walletView(request):
    return render(request,'apps-crypto-wallet.html')
# --------------------------------------------------------------

# --------------------------------------------------------------

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request , 'registration/auth-signin-basic.html')
# --------------------------------------------------------------

def signUpView(request):
    form =SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            new_user = authenticate(username = username,password = password)
            if new_user is not None:
                login(request,new_user)
                return redirect('login')
        else:
            form = SignUpForm() 
    context ={
        'form':form
    }
    return render(request ,'auth-signup-basic.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
# --------------------------------------------------------------


@login_required
def create_child_left(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        referal = request.POST.get('referal', '')
        password = request.POST.get('password')
        package = request.POST.get('package')

        # Create the child model
        child = Left.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            city=city,
            state=state,
            country=country,
            referal=referal,
            package=package,
        )

        # Create the user model and link it to the child model
        user_left = User.objects.create_user(username=email, password=password)
        user_profile = UserProfile.objects.create(user=user_left)
        child.user_profile = user_profile
        child.save()

        # Render the child and user info on the HTML page
        context = {'child_left': child, 'user_left': user_left}
        return render(request, 'index.html', context)
    else:
        form = LeftForm()
    return render(request, 'forms-elements-left.html', {'form': form})


@login_required
def create_child_right(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        referal = request.POST.get('referal', '')
        password = request.POST.get('password')
        package = request.POST.get('package')

        # Create the child model
        child = Right.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            city=city,
            state=state,
            country=country,
            referal=referal,
            package=package,
        )

        # Create the user model and link it to the child model
        user_right = User.objects.create_user(username=email, password=password)
        user_profile = UserProfile.objects.create(user=user_right)
        child.user_profile = user_profile
        child.save()

        # Render the child and user info on the HTML page
        context = {'child_left': child, 'user_left': user_right}
        return render(request, 'index.html', context)
    else:
        form = LeftForm()
    return render(request, 'forms-elements-right.html', {'form': form})
# @login_required
# def member_count(request):
#     current_user = request.user
#     user_profile = UserProfile.objects.get(user=current_user)
#     left_members_count = user_profile.left.count()
#     right_members_count = user_profile.right.count()
#     return render(request, 'member_count.html', {'left_count': left_members_count, 'right_count': right_members_count})
# @login_required
# def rightView(request):
#     right_list=Right.objects.all()
#     context = {'right':right_list}
#     return render(request,'binary.html',context)
@login_required
def right_list(request):
    rights = Right.objects.all()
    return render(request, 'binary.html', {'rights': rights})
@login_required
def left_list(request):
    lefts = Left.objects.all()
    return render(request, 'binary.html', {'lefts': lefts})
@login_required
def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'binary.html', {'parents': parents})


def calculate_common_packages_with_commission():
    left_total = Left.objects.aggregate(Sum('package'))['package__sum'] or 0
    right_total = Right.objects.aggregate(Sum('package'))['package__sum'] or 0
    if left_total < right_total:
        common_total = left_total
        Left.objects.update(package=0)
        Right.objects.update(package=F('package') - left_total)
    else:
        common_total = right_total
        Right.objects.update(package=0)
        Left.objects.update(package=F('package') - right_total)
    commission = common_total * 0.075
    common_total -= commission
    common_total_obj, _ = CommonTotal.objects.get_or_create(id=1)
    common_total_obj.total += common_total
    common_total_obj.save()
def commision_view(request):
    common_total = CommonTotal.objects.first()  # get the first CommonTotal instance
    commission_string = common_total.calculate_commission()  # calculate the commission
    context = {
        'commission': commission_string,
    }
    return render(request,'output.html',context)