from time import ctime

from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from myapp.models import Analyst,Analysis

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Analyst
        fields = ('username','first_name','last_name','password')
        required = ('username','password')
        widgets = {
            'password': forms.PasswordInput,
        }

class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = '__all__'
        required = ('analyst','method','date','reference','standard_RSD','standardStdDev','CorrelationOfStandards')
        widgets = {
            'date':forms.SelectDateWidget
        }

class ChartForm(forms.Form):
    #queryset=Analysis.objects.filter(analyst__username__iexact=username).values('method__Method_Number'),
    '''Method = forms.MultipleChoiceField(required=True)
    Date = forms.MultipleChoiceField(required=False)

    def __init__(self, *args, request=None, **kwargs):
        user = kwargs.pop('user')
        print("Hello",user)
        super(ChartForm, self).__init__(*args, **kwargs)
        # perhaps you want to set the request in the Form

        methodlist = [ (e.method.Method_Number,e.method.Method_Number) for e in Analysis.objects.filter(analyst__username__iexact=user)]
        datelist = [ (e.date,e.date) for e in Analysis.objects.filter(analyst__username__iexact=user)]
        print(methodlist)
        #print(Analysis.objects.filter(analyst__username__iexact=user).values('method__Method_Number'))
        self.fields['Method'].choices = methodlist
        self.fields['Date'].choices = datelist
'''
    #print(Analysis.objects.filter(analyst__username__iexact = username).values_list('method__Method_Number'))

    Method = forms.CharField(required=True)
    StartDate = forms.CharField(
        required=False,
        widget=forms.SelectDateWidget(years=range(1990,2030)),
    )
    EndDate = forms.CharField(
        required=False,
        widget=forms.SelectDateWidget(years=range(1990,2030)),
    )







