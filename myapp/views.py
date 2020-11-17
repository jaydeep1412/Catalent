from time import ctime

from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, request
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from .forms import AnalysisForm, RegisterForm

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
from .models import Analyst, Analysis


def register(request):
    msg = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            msg = 'Your data has been registered in the database'
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'myapp/order_response.html', {'msg': msg})
        else:
            msg = 'Make sure the data entered is valid'
            return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = RegisterForm
    return render(request, 'myapp/register.html',{'form':form,'msg':msg,})



def user_login(request):
    #request.session['last_login'] = ctime()
    #to expire after cetain seconds
    #request.session.set_expiry(3600)
    #to expire as the user closes the window
    #request.session.set_expiry(0)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('myapp:list_entry'))
    else:

        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                if user.is_active:
                    request.session['username'] = username
                    request.session['first_name'] = Analyst.objects.get(username__iexact=username).first_name
                    request.session['last_name'] = Analyst.objects.get(username__iexact=username).last_name
                    login(request, user)
                    return HttpResponseRedirect(reverse('myapp:list_entry'))
                    #return HttpResponse('Successfully Logged In')
                else:
                    return HttpResponse('Your account is disabled.')
            else:
                return HttpResponse('Invalid login details.')
        else:
            #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
            return render(request, 'myapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect(reverse('myapp:user_login'))


def my_analysis(request):
    if(request.user.is_authenticated):
        if(request.method=='POST'):

            form = AnalysisForm(request.POST)
            if form.is_valid():
                msg = 'Your data has been saved in the database'
                form.save()
                return render(request, 'myapp/order_response.html', {'msg':msg})
            else:
                msg = 'Please input correct data and try again'
                return render(request, 'myapp/order_response.html', {'msg': msg})

        else:
            form = AnalysisForm
        return render(request, 'myapp/analysis.html',{'form':form})
    else:
        msg = 'Please login to access this feature'
        return render(request, 'myapp/order_response.html', {'msg': msg})

def list_entries(request):
    if request.user.is_authenticated:
        print(request.user.username)
        analyst = Analyst.objects.get(first_name__iexact=request.user.username)
        analyst_details = Analysis.objects.filter(analyst__username__iexact = request.user.username)
        return render(request,'myapp/list_entry.html', {'analyst_details' : analyst_details, 'analyst' : analyst})
    else:
        msg = 'Please login to see your entries'
        return render(request,'myapp/order_response.html',{'msg':msg})


#Trying chartit
'''def charts_visualize(request):
    if request.user.is_authenticated:

        # Step 1: Create a DataPool with the data we want to retrieve.
        date_RSD = \
            DataPool(
                series=
                [{'options': {
                    'source': Analysis.objects.filter(analyst__username=request.user.username)},
                    'terms': [
                        'date',
                        'standard_RSD',
                        ]}
                ])

        # Step 2: Create the Chart object
        cht = Chart(
            datasource=date_RSD,
            series_options=
            [{'options': {
                'type': 'line',
                'stacking': False},
                'terms': {
                    'date': [
                        'standard_RSD']
                }}],
            chart_options=
            {'title': {
                'text': 'Trying date vs Std RSD'},
                'xAxis': {
                    'title': {
                        'text': 'Date'}}})

        # Step 3: Send the chart object to the template.
        render(request,'myapp/charts.html',{'cht':cht})

    else:
        render(request,'myapp/order_response.html',{'msg':"Please login to use this feature"})'''

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

def display( request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, 'charts.html')
    else:
        return render(request,'myapp/order_response.html',{'msg':"You need to login to see the visualization"})

User = get_user_model()

class ChartData( APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        print(request.session['username'])
        data = {
            "Date":Analysis.objects.filter(analyst__username__iexact = request.session['username']).values_list('date', flat=True),
            "peakTailing":Analysis.objects.filter(analyst__username__iexact = request.session['username']).values_list('peakTailing', flat=True),
            "standard_RSD": Analysis.objects.filter(analyst__username__iexact=request.session['username']).values_list('standard_RSD', flat=True),
            "standardStdDev": Analysis.objects.filter(analyst__username__iexact=request.session['username']).values_list('standardStdDev', flat=True),
            "CorrelationOfStandards": Analysis.objects.filter(analyst__username__iexact=request.session['username']).values_list('CorrelationOfStandards', flat=True),
            "resolution": Analysis.objects.filter(analyst__username__iexact=request.session['username']).values_list('resolution', flat=True)
        }
        return Response(data)