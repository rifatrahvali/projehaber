from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.




# - Kategori
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True,blank=True,editable=False)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
            return self.title
    
# - Haber 
class News(models.Model):
    title = models.CharField(max_length=200,verbose_name = "Haber Başlığı")
    image = models.ImageField(upload_to='news',verbose_name = "Haber Görseli")
    context = RichTextField(verbose_name = "Haber Makalesi")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name = "Haber Kategorisi")
    publishDate = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200,verbose_name = "Haber Etiketi")
    views = models.IntegerField(default=0,verbose_name = "Haber Görüntülenme Sayısı")
    slug = models.SlugField(max_length=200,unique=True,blank=True,editable=False)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(News,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


# - Galeri
class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider')


# - iletişim
class Contact(models.Model):
    fullName = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
# - hakkımızda
class About(models.Model):
    title = models.CharField(max_length=200)
    context = RichTextField()
# - Duyurular
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    slug = models.SlugField(max_length=200,blank=True,editable=False)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Notice,self).save(*args, **kwargs)

# - Ayarlar
class Settings(models.Model):
    logo1 = models.ImageField(upload_to='dimg',null=True, blank=True)
    logo2 = models.ImageField(upload_to='dimg',null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    phone = models.CharField(max_length=15)
    phoneMobile = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=10)
    facebookUrl = models.URLField(max_length=255)
    twitterUrl = models.URLField(max_length=255)
    instagramUrl = models.URLField(max_length=255)
    youtubeUrl = models.URLField(max_length=255)
