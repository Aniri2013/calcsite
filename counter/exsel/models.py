from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название')
	composition = models.CharField(max_length=500, null=True, blank=True, verbose_name='Состав')
	price = models.FloatField(verbose_name='Цена за 100 грамм')
	grams_per_person = models.FloatField(verbose_name='Грамм на человека')
	weight = models.FloatField(verbose_name='Заказ (грамм)')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время')
	total_price = models.FloatField(default=0, verbose_name='Стоимость заказа')
	rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Категория', max_length=600)
	image = models.ImageField(upload_to='static/images/', null=True, blank=True)
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Позиция')

	def __str__(self):
		return self.name[:25]

	def calculate_price(self):
		total = (self.price * self.weight) / 100
		return total

	def save(self, *args, **kwargs):
		self.total_price = round(float(self.calculate_price()), 2)
		super().save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Заказы'
		verbose_name = 'Заказ'
		ordering = ['my_order']

class Rubric(models.Model):
	name = models.CharField(max_length=100, db_index=True, verbose_name='Название')

	def __str__(self):
		return self.name[:25]

	class Meta(object):
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['name']

