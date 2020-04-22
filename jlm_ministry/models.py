from django.db import models
from embed_video.fields import EmbedVideoField

class Pastors(models.Model):
    image = models.ImageField(upload_to='media/photos/', null=True,
            blank=True)
    full_name = models.CharField(max_length=250)
    LEVEL = (
            ('Senior Resident Pastor', 'Senior Resident Pastor'),
            ('Assistant Resident Pastor', 'Assistant Resident Pastor'),
            ('Pastor', 'Pastor'),
    )
    level = models.CharField(max_length=100, choices=LEVEL, default='level')
    BRANCH = (
            ('Main branch', 'Main branch'),
            ('Kitengela branch', 'Kitengela branch'),
            ('Kibera branch', 'Kibera branch'),
    )
    branch = models.CharField(max_length=100, choices=BRANCH, default='branch')
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name

    def save_full_name(self):
        self.save()

    def save_branch(self):
        self.save()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all(cls):
        Pastors = cls.objects.all()
        return pastors

class Leadership(models.Model):
    image = models.ImageField(upload_to='media/photos/', null=True, blank=True)
    full_name = models.CharField(max_length=250)
    LEVEL = (
            ('Senior Pastor', 'Senior Pastor'),
            ('Pastor', 'Pastor'),
            ('Bishop', 'Bishop'),
    )
    level = models.CharField(max_length=100, choices=LEVEL, default='level')
    BRANCH = (
            ('Bishop of jlm ministries', 'Bishop of jlm ministries'),
            ('Chairman of jlm ministries', 'Chairman of jlm ministries'),
            ('Kibera branch', 'Kibera branch'),
            ('Jlm ministries', 'Jlm ministries'),
    )
    branch = models.CharField(max_length=100, choices=BRANCH, default='branch')
    message = models.CharField(max_length=150)
    biograpgy = models.CharField(max_length=1000, default='biograpgy')

    def __str__(self):
        return self.full_name

    def save_full_name(self):
        self.save()

    def save_branch(self):
        self.save()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

# model for ushering Department
class Ushering(models.Model):
    image = models.ImageField(upload_to='media/photos/')
    full_name = models.CharField(max_length=250)

    LEVEL = (
            ('Head usher', 'Head Usher'),
            ('Usher', 'Usher'),
    )
    level = models.CharField(max_length=100, choices=LEVEL, default='level')
    BRANCH = (
            ('Main branch', 'Main branch'),
            ('Kitengela branch', 'Kitengela branch'),
            ('Kibera branch', 'Kibera branch'),
    )
    branch = models.CharField(max_length=100, choices=BRANCH, default='branch')

    def __str__(self):
        return self.full_name

    def save_full_name(self):
        self.save()

    def save_image(self):
        self.save()

    def save_branch(self):
        self.save()

# model for transport Department
class Transport(models.Model):
    image = models.ImageField(upload_to='media/photos/')
    full_name = models.CharField(max_length=250)
    BRANCH = (
            ('Main branch', 'Main branch'),
            ('Kitengela branch', 'Kitengela branch'),
            ('Kibera branch', 'Kibera branch'),
    )
    branch = models.CharField(max_length=100, choices=BRANCH, default='branch')

    def __str__(self):
        return self.full_name

    def save_full_name(self):
        self.save()

    def save_image(self):
        self.save()

    def save_branch(self):
        self.save()

# model for worshipper Department
class Worshipper(models.Model):
    image = models.ImageField(upload_to='media/photos/')
    full_name = models.CharField(max_length=250)

    LEVEL = (
            ('Head Worshipper', 'Head Worshipper'),
            ('Worshipper', 'Worshipper'),
    )
    level = models.CharField(max_length=100, choices=LEVEL, default='level')
    BRANCH = (
            ('Main branch', 'Main branch'),
            ('Kitengela branch', 'Kitengela branch'),
            ('Kibera branch', 'Kibera branch'),
    )
    branch = models.CharField(max_length=100, choices=BRANCH, default='branch')

    def __str__(self):
        return self.full_name

    def save_full_name(self):
        self.save()

    def save_image(self):
        self.save()

    def save_branch(self):
        self.save()

# model for worshipper Department
class Media(models.Model):
    image = models.ImageField(upload_to='media/photos/')
    full_name = models.CharField(max_length=250)

    LEVEL = (
            ('Media', 'Media'),
    )
    level = models.CharField(max_length=100, choices=LEVEL, default='level')
    BRANCH = (
            ('Main branch', 'Main branch'),
            ('Kitengela branch', 'Kitengela branch'),
            ('Kibera branch', 'Kibera branch'),
    )
    branch = models.CharField(max_length=100, choices=BRANCH, default='branch')

    def __str__(self):
        return self.full_name

    def save_full_name(self):
        self.save()

    def save_image(self):
        self.save()

    def save_branch(self):
        self.save()


# model for worshipper Department
class Deacon(models.Model):
    image = models.ImageField(upload_to='media/photos/')
    full_name = models.CharField(max_length=250)
    LEVEL = (
            ('Deacon', 'Deacon'),
            ('Deaconnes', 'Deaconnes'),
    )
    level = models.CharField(max_length=100, choices=LEVEL, default='level')
    BRANCH = (
            ('Main branch', 'Main branch'),
            ('Kitengela branch', 'Kitengela branch'),
            ('Kibera branch', 'Kibera branch'),
    )
    branch = models.CharField(max_length=100, choices=BRANCH, default='branch')

    def __str__(self):
        return self.full_name

    def save_full_name(self):
        self.save()

    def save_image(self):
        self.save()

    def save_branch(self):
        self.save()
