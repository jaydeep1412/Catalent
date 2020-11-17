from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Method(models.Model):
    Method_Name = models.CharField(max_length=50,blank=True, null=True)
    Method_Number = models.CharField(max_length=50,blank=True, null=True)
    Method_ID = models.AutoField(primary_key=True)

    class Meta:
        verbose_name_plural = "Method"

    def __str__(self):
        return "%s" % (self.Method_Name)

class Analyst(User):
    '''Analyst_ID = models.PositiveIntegerField(primary_key=True)
    Analyst_FirstName = models.CharField(max_length=50)
    Analyst_LastName = models.CharField(max_length=50)
    Analyst_Email = models.EmailField()'''

    def __str__(self):
        return "%s" % (self.get_full_name())

class Analysis(models.Model):
    analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    date = models.DateField()
    reference = models.CharField(max_length=50)
    standard_RSD = models.FloatField()
    standardStdDev = models.FloatField()
    CorrelationOfStandards = models.FloatField(blank=True, null=True)
    peakTailing = models.FloatField(blank=True, null=True)
    resolution = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Analysis"

    def __str__(self):
        return "%s %s" %(self.analyst.get_full_name(),self.method.Method_ID)







