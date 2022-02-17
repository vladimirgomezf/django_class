from django.db import models


# Create your models here.
from duplicity.gpginterface import Process


class Person (models.Model):
    name = models.CharField('Person Name', max_length=50)
    phone = models.CharField('Person Phone Number', max_length=15)
    email = models.EmailField('Person Email')

    def __str__(self):
        return self.name


class Address (models.Model):
    street = models.CharField('Street', max_length=30)
    city = models.CharField('City', max_length=30)
    state = models.CharField('State', max_length=30)
    zip = models.CharField('Zip Code', max_length=6)
    country = models.CharField('Country ', max_length=30)

    def __str__(self):
        return f'Calle: { self.street}  de la ciudad { self.city} del estado: { self.state } del país: { self.country }.'


class Student (Person):
    student_number = models.IntegerField('Student Number')
    average_rank = models.FloatField('Average Rank')

    def __str__(self):
        return self.name


class Professor (Person):
    salary = models.FloatField('Professor Salary')

    def __str__(self):
        return self.name

class Group (models.Model):
    name = models.CharField('Group Name', max_length=50, default="Group")
    profesor = models.OneToOneField(Professor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
