from django.db import models

# Create your models here.
class Proizvod(models.Model):
	Ime = models.CharField(max_length=20)
	Kod = models.CharField(max_length=20)
	Cijena = models.CharField(max_length=20)

	def __repr__(self):
		return self.Ime+'   '+self.Cijena

class Mjesec(models.Model):
	Oznaka = models.CharField(max_length=10)

	def __repr__(self):
		return self.Oznaka

class Kupac(models.Model):
	Ime = models.CharField(max_length=20)
	Prezime = models.CharField(max_length=20)

	def __repr__(self):
		return self.Ime+' '+self.Prezime

class Popis(models.Model):
	BrojRacuna = models.CharField(max_length=10)
	Kupac = models.ForeignKey(Kupac, on_delete = models.CASCADE)
	Mjesec = models.ForeignKey(Mjesec, on_delete = models.PROTECT)
	Proizvodi = models.ManyToManyField(Proizvod)

	def __repr__(self):
		return '{} ({} {})'.format(self.BrojRacuna, self.Kupac.Ime, self.Kupac.Prezime)
