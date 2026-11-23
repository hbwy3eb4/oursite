from django.db import models
from core.models import Employee

class MilitaryRecord(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    category = models.CharField('Категория годности', max_length=10)
    voenkomat = models.CharField('Военкомат', max_length=100, blank=True)
    last_med_check = models.DateField('Последний медосмотр', null=True, blank=True)
    next_med_check = models.DateField('Следующий медосмотр', null=True, blank=True)
    notes = models.TextField('Примечания', blank=True)
    
    def __str__(self):
        return f"ВУ: {self.employee.full_name}"