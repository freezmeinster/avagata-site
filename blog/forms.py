from django.forms import ModelForm
from blog.models import Kategori,Post

class KategoriForm(ModelForm):
	
	class Meta:
		model = Kategori

class PostForm(ModelForm):
	
	class Meta:
		model = Post
