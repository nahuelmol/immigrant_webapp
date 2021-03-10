from django.db import models

class procces(models.Model):
    fate_country = models.CharField(max_length = 20)
    main_visa = models.CharField(max_length=50)
    visas_considered = models.TextField(max_length=200)
    ifresident_ = models.BooleanField(blank=True)
    resident_type = models.CharField(max_length=20)

#the next model is for monitors seeking some interestjng users

class interested_list(models.Model):
    name = models.CharField(max_length=20)
    howold = models.IntField()
    language_native = models.BooleanField()
    current_laboral_state = models.CharField(max_lenght=20)
