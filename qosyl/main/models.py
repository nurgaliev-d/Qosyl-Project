from django.contrib.auth.models import User
from django.db import models

# UserProfile model
class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    interests = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"

# Organization model
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(UserProfile, related_name='subscribed_organizations')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Publication model
class Publication(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='publications/')
    topic = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserProfile, related_name='liked_publications')
    posted_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
