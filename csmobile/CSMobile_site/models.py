from django.db import models


# Create your models here.


class Directory(models.Model):
    guid = models.CharField(verbose_name='GUID', max_length=50, editable=False, default='')
    code = models.CharField(verbose_name='Код', max_length=20, default='')
    name = models.CharField(verbose_name="Наименование", max_length=50, default='')


class Contact(Directory):
    phone = models.CharField(verbose_name="Телефон", max_length=11)
    email = models.EmailField(verbose_name="Email", max_length=50)

    def __str__(self):
        return self.name


class Employee(Directory):
    phone = models.CharField(verbose_name="Телефон", max_length=11)
    email = models.EmailField(verbose_name="Email", max_length=50)

    def __str__(self):
        return self.name


class Document(models.Model):
    guid = models.CharField(verbose_name='GUID', max_length=50, editable=False)
    date = models.DateTimeField(verbose_name="Дата документа", default='')
    number = models.CharField(verbose_name='Номер документа', max_length=50, default='')


class Status(models.Model):
    state = models.CharField(verbose_name='Статус выполнения', max_length=10)

    def __str__(self):
        return self.state


class CostumerContact(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, verbose_name='Сотрудник')
    client = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE, verbose_name='Клиент')
    appeal = models.CharField(verbose_name="Суть обращения", max_length=5000)

    def __str__(self):
        return f'{self.client} - {self.employee}'


class Contractor(Directory):
    inn = models.CharField(verbose_name='ИНН', max_length=10)

    def __str__(self):
        return f'{self.name} - {self.inn}'


class Request(Document):
    costumer = models.ForeignKey(Contractor, null=True, on_delete=models.CASCADE, verbose_name='Контрагент')
    contact = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE, verbose_name='Клиент')
    status = models.ForeignKey(Status, null=True, on_delete=models.CASCADE, verbose_name='Статус обращения')
    CostumerContacts = models.ForeignKey(CostumerContact, null=True, on_delete=models.CASCADE,
                                         verbose_name='Контакты с клиентом')
    executor = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, verbose_name='Исполнитель')

    def __str__(self):
        return f'{self.costumer} - {self.status}'
