from django.db import models

# Create your models here.
# class Product(models.Model):
#     t = models.CharField(max_length=100,null=True,blank=True)
#     def __str__(self):
#         return self.t

Label=(
    ("New","New"),
    ("Top","Top"),
    ("Trending","Trending"),
    ("Sensitive","Sensitive"),
    ("Old","Old"),
    ("Covid", "Covid"),
)
Category=(
    ("Art","Art"),
    ("Magazine","Magazine"),
    ("Business","Business"),
    ("Politics","Politics"),
    ("Sports","Sports"),
    ("Travel","Travel"),
    ("Food","Food"),
    ("Crime","Crime"),
    ("Covid","Covid"),
    ("Health","Health"),
    ("Photography","Photography"),
    ("Technology","Technology"),
    ("Other","Other"),

)
class News(models.Model):
    title = models.CharField(max_length=1200,null=True,blank=True)
    description = models.CharField(max_length=111000,null=True,blank=True)
    image = models.ImageField(upload_to="images/newsimages",null=True,blank=True)
    category = models.CharField(max_length=100, null=True, blank=True, choices=Category,default="Other")
    label = models.CharField(max_length=100, null=True, blank=True, choices=Label)
    publish_date_byus = models.DateTimeField(null=True,blank=True)
    held_date = models.DateTimeField(null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    journalist = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,null=True,blank=True,default='India')
    image2 = models.ImageField(upload_to="images/newsimages", null=True, blank=True)
    description2 = models.CharField(max_length=111000, null=True, blank=True)
    image3 = models.ImageField(upload_to="images/newsimages", null=True, blank=True)
    description3 = models.CharField(max_length=111000, null=True, blank=True)

    # video = models.FileField(upload_to="news/uploads/videos/newsvideos",null=True,blank=True)
    class Meta:
        verbose_name ="News"
        verbose_name_plural ="News"
    def __str__(self):
        b= str(self.publish_date_byus)
        if self.journalist:
            return self.journalist +" "+ b +" "+ self.title +"  "+ self.country +" " + self.state
        else:
            return b + " " + self.title
