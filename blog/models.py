from django.db import models

class Post(models.Model):
	STATUS = (
		('POST','Terbitkan'),
		('PANDING','Tunda'),
	)
	
	judul = models.CharField(max_length=255)
	isi = models.TextField()
	tgl_post = models.DateTimeField(auto_now_add=True)
	kategori = models.ForeignKey('Kategori')
	status = models.CharField(max_length=10,choices=STATUS,default='POST')
	
class Kategori(models.Model):
	ENABLE = (
		('AKTIF','Aktif'),
		('TIDAK_AKTIF','Tidak Aktif'),
	)
	
	nama = models.CharField(max_length=255)
	status = models.CharField(max_length=12,choices=ENABLE,default='AKTIF')
	
	def __unicode__(self):
		return self.nama

class Komentar(models.Model):
	nama = models.CharField(max_length=255)
	email = models.EmailField()
	website = models.URLField()
	posting = models.ForeignKey('Post')
	komentar = models.TextField()
	tgl_komentar = models.DateTimeField(auto_now_add=True)
