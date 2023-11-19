from django.db import models

class FilesAdmin(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define the primary key
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.file_name
