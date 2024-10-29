from django.contrib.auth.models import User
from django.db import models



from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.exceptions import ValidationError

# Offensive words list and validator function
OFFENSIVE_WORDS = [
    'fuck', 'myr', 'suck',
    'insult', 'vulgar', 'profanity',
    'damn', 'cunt','bitch', 'crap', 'bastard', 'asshole',
    # Add other words...
]

def validate_offensive_content(text):
    """Raises ValidationError if text contains offensive words."""
    for word in OFFENSIVE_WORDS:
        if word.lower() in text.lower():
            raise ValidationError(f'The text contains offensive content: "{word}"')

class Comment(models.Model):
    petition = models.ForeignKey('Petition', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Custom validation to check for offensive content in the comment body."""
        validate_offensive_content(self.body)

    def save(self, *args, **kwargs):
        """Override save to ensure clean() is called on each save."""
        self.clean()  # This will run the validate_offensive_content check
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment by {self.author} on {self.created_at}"

# Petition model
class Petition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    signatures = models.ManyToManyField(User, related_name='signed_petitions', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    image = models.ImageField(upload_to='petitions/', blank=True, null=True)

    def __str__(self):
        return self.title

    def signature_count(self):
        """Returns the number of signatures for this petition."""
        return self.signatures.count()

    def clean(self):
        # Validate for offensive content in the title and description
        validate_offensive_content(self.title)
        validate_offensive_content(self.description)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

# Comment model


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
    


