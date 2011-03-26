from django.forms import ModelForm
from blog.models import Kategori

class KategoriForm(ModelForm):
	
	class Meta:
		model = Kategori
