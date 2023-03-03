from django.db import models


class Header(models.Model):
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/')
    button = models.CharField(max_length=255)


class Info(models.Model):
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/')
    

class Product(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/')
    cost = models.IntegerField()

class Productinfo(models.Model):
    logo = models.ImageField(upload_to='media/')
    text_uz = models.TextField()
    text_ru = models.TextField()

class Aboutus(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()

class Faq(models.Model):
    desc_uz = models.CharField(max_length=255)
    text_uz = models.TextField()
    desc_ru = models.CharField(max_length=255)
    text_ru = models.TextField()

class Productfaq(models.Model):
    desc_uz = models.CharField(max_length=255)
    text_ru = models.TextField()
    desc_ru = models.CharField(max_length=255)
    text_uz = models.TextField()

class Fakt(models.Model):
    number = models.IntegerField()
    desc_uz = models.CharField(max_length=255)
    text_uz = models.TextField()
    desc_ru = models.CharField(max_length=255)
    text_ru = models.TextField()


class Order(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()

class Advice(models.Model):
    photo = models.ImageField()
    text_uz = models.TextField()
    text_ru = models.TextField()

class Abouttea(models.Model):
    question_ru = models.CharField(max_length=255)
    question_uz = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    
class Ijtimoiy(models.Model):
    facebok = models.URLField()
    facebok_img = models.ImageField(upload_to='media/')
    Instagram = models.URLField()
    Instagram_img = models.ImageField(upload_to='media/')
    telegram = models.URLField()
    telegram_img = models.ImageField(upload_to='media/')
    youtube = models.URLField()
    youtube_img = models.ImageField(upload_to='media/')
