from django.db import models

class Organization(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.name}'

class Batch(models.Model):
    name=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    total_students=models.IntegerField()
    active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.name}"


class Feedback(models.Model):
    kbefore=models.IntegerField()
    kafter=models.IntegerField()
    communication=models.IntegerField()
    content=models.IntegerField()
    handson=models.IntegerField()
    interaction=models.IntegerField()
    speed=models.IntegerField()
    rating=models.IntegerField()
    feedback=models.TextField()
    suggestions=models.TextField(blank=True)
    submitted_at=models.DateTimeField(auto_now_add=True)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)


