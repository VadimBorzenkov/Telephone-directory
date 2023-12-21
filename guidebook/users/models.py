from django.db import models


class Firstname(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Surname(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Patronymic(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Main(models.Model):
    firstname = models.ForeignKey(to=Firstname, on_delete=models.CASCADE)
    surname = models.ForeignKey(to=Surname, on_delete=models.CASCADE)
    patronymic = models.ForeignKey(to=Patronymic, on_delete=models.CASCADE)
    street = models.ForeignKey(to=Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=20)
    corpus = models.CharField(max_length=10)
    apartments = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.surname.name} {self.firstname.name} {self.patronymic.name}. Адрес: {self.street.name} {self.house} {self.corpus} {self.apartments}. Телефон: {self.phone}"
