import uuid as uuid
from django.db import models


# Create your models here.


class directory(models.Model):
    guid
    code
    name = models.CharField(verbose_name="Наименование", max_length=50)


class Client(HandBook):
    full_name = models.CharField(verbose_name="ФИО", max_length=50)
    phone = models.CharField(verbose_name="Телефон", max_length=11)
    email = models.EmailField(verbose_name="Email", max_length=50)

    def __str__(self):
        return self.full_name


class Employee(HandBook):
    full_name = models.CharField(verbose_name="ФИО", max_length=50)
    phone = models.CharField(verbose_name="Телефон", max_length=11)
    email = models.EmailField(verbose_name="Email", max_length=50)

    def __str__(self):
        return self.full_name


class Document(models.Model):
    guid
    date = models.DateTimeField(verbose_name="Дата документа", default='')
    number = models.CharField(verbose_name='Номер документа', max_length=50)


class Status(models.Model):
    state = models.CharField(verbose_name='Статус выполнения', max_length=10)

    def __str__(self):
        return self.state


class CostumerContact(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, verbose_name='Сотрудник')
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE, verbose_name='Клиент')
    appeal = models.CharField(verbose_name="Суть обращения", max_length=5000)

    def __str__(self):
        return f'{self.client} - {self.employee}'


class Costumer(HandBook):
    inn = models.CharField(verbose_name='ИНН', max_length=10)

    def __str__(self):
        return f'{self.name} - {self.inn}'


class Application(Document):
    contractor = models.ForeignKey(Contractor, null=True, on_delete=models.CASCADE, verbose_name='Контрагент')
    status = models.ForeignKey(Status, null=True, on_delete=models.CASCADE, verbose_name='Статус обращения')
    contacts = models.ForeignKey(CostumerContact, null=True, on_delete=models.CASCADE,
                                 verbose_name='Контакты с клиентом')
    performer = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, verbose_name='Исполнитель')

    def __str__(self):
        return f'{self.contractor} - {self.status}'
