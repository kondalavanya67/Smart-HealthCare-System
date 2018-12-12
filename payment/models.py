from django.db import models

# Create your models here.


class bank(models.Model):
	bank_name = models.CharField(max_length=40)
	bank_id = models.CharField(max_length=10)
	def __str__(self):
		return self.bank_name

class bank_customer(models.Model):
	CARD_TYPE_CHOICES = (
			('Visa','Visa'),
			('Rupay','Rupay'),
			('Master Card','Master Card'),
		)
	Bank = models.ForeignKey(bank, on_delete=models.SET_NULL, null=True)
	customer_name = models.CharField(max_length=20)
	card_no = models.CharField(max_length=20)
	card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES)
	card_cvv = models.IntegerField()
	bank_balance = models.FloatField(default=3000)

	def __str__(self):
		return self.customer_name


class OnlinePayment(models.Model):
	transaction_id = models.CharField(max_length=20)
	amount_paid = models.IntegerField()
	customer = models.ForeignKey(bank_customer, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.transaction_id
