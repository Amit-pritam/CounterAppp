from django.db import models


class CounterModel(models.Model):                       #model(table) name is countermodel and column name is number.	
	number = models.CharField(max_length = 10)