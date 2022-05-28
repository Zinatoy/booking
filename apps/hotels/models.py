from django.db import models

# Create your models here.
class Bedroom(models.Model):
    bedroom = models.SmallIntegerField(verbose_name="Односпальная комната")

    def __str__(self):
        return self.bedroom
    
    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Bedrooms(models.Model):
    bedrooms =  models.SmallIntegerField(verbose_name="Двуспальная комната")
    
    def __str__(self):
        return self.bedrooms
    
    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

class Parking(models.Model):
    parking_cost = models.CharField(max_length=255,verbose_name="Стоимость парковки", help_text="Платная")

    def __str__(self):
        return self.parking
    
    class Meta:
        verbose_name = "Парковка"
        verbose_name_plural = "Парковки"

class Swimming(models.Model):
    swimming = models.CharField(max_length=255, verbose_name="Бассейн", help_text="Есть")

    def __str__(self):
        return self.swimming
    
    class Meta:
        verbose_name = "Бассейн"
        verbose_name_plural = "Бассейны"

class Skiing(models.Model):
    skiing = models


class Hotel(models.Model):
    hotel_image = models.ImageField(upload_to ='hotel_detail/',verbose_name="Отель")
    name = models.CharField(max_length=255,verbose_name="Название",help_text="Royal Hotel")
    description = models.TextField(verbose_name="Описание")
 