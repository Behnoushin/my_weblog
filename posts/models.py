from django.db import models

class Post (models.Model):
    title =models.CharField(max_length=80)
    text =models.TextField(blank = True)
    is_enable =models.BooleanField(default=False)
    publish_time =models.DateField(null=True, blank = True)
    create_time =models.DateTimeField(auto_now_add=True)
    update_time =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        #return self.title
        return '{}-{}'.format(self.pk , self.title)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    text =models.TextField()
    create_time =models.DateTimeField(auto_now_add=True)
    update_time =models.DateTimeField(auto_now=True)