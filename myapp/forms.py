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