from django.contrib.auth.models import User
from django.db import models

class Petition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    signatures = models.ManyToManyField(User, related_name='signed_petitions', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    image = models.ImageField(upload_to='petitions/', blank=True, null=True)  # Add this line

    def __str__(self):
        return self.title

    def signature_count(self):
        """Returns the number of signatures for this petition."""
        return self.signatures.count()




class Signature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    petition = models.ForeignKey(Petition, related_name='signature_entries', on_delete=models.CASCADE)  # Change related_name
    signed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'petition')

    def __str__(self):
        return f"{self.user.username} signed '{self.petition.title}'"



class Complaint(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

