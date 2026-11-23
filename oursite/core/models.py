from django.db import models

class Department(models.Model):
    name = models.CharField('Название отдела', max_length=100)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')
    position = models.CharField('Должность', max_length=100)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    
    def __str__(self):
        return self.full_name