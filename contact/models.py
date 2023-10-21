from django.db import models

# Create your models here.
class contact(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.TextField(blank=False, null=False, max_length= 300)
    Email = models.EmailField(blank=False, null=False)
    Subject = models.TextField(blank=False, null=False, max_length= 300)
    Message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now= True)

    def serialize(self):
        return {
            "id" : self.id,
            "Name": self.Name,
            "Subject": self.Subject,
            "Message": self.Message,
            "created_at": self.created_at
        }

