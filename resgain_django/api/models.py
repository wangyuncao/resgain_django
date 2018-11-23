from django.db import models

# Create your models here.


class CompleteInformation(models.Model):

    name = models.CharField(max_length=10)
    man = models.CharField(max_length=10)
    girl = models.CharField(max_length=10)
    details = models.CharField(max_length=1000)
    five_lines = models.CharField(max_length=10)
    three_talents = models.CharField(max_length=10)
    five_cases_tian = models.IntegerField()
    five_cases_ren = models.IntegerField()
    five_cases_di = models.IntegerField()
    five_cases_zong = models.IntegerField()
    five_cases_wai = models.IntegerField()
    five_grid_analysis_tian = models.CharField(max_length=255)
    five_grid_analysis_ren = models.CharField(max_length=255)
    five_grid_analysis_di = models.CharField(max_length=255)
    five_grid_analysis_wai = models.CharField(max_length=255)
    five_grid_analysis_zong = models.CharField(max_length=255)
    verse = models.CharField(max_length=100)

    sexual = models.ForeignKey('Sexual', on_delete=models.CASCADE, )

    class Meta:
        db_table = 'complete_information'


class Sexual(models.Model):
    sexual = models.CharField(max_length=10)

    class Meta:
        db_table = 'sexual'
