from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField
from django_google_maps import fields as map_fields


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser):
        if not email:
            raise ValueError('user must have email address')
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          )
        # We check if password has been given
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


# We change following functions signature to allow "No password"
    def create_user(self, username, email, password=None):
        return self._create_user(username, email, password, False, False)

    def create_superuser(self, username, email, password=None):
        user = self._create_user(username, email, password, True, True)
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, username=None, **extra_fields):
    #     user = self._create_user(email, username, True, True, **extra_fields)
    #     user.save(using=self._db)
    #     return user


class TUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, default='0')
    email = models.EmailField(('email address'), unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tutor_profile/', default='default.png')
    phone_number = models.IntegerField(blank=True, null=True)
    is_tutee = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('teacher status', default=False)
    year = models.IntegerField(blank=True, null=True)
    subjects = models.CharField(max_length=500, default="")
    bio = models.TextField(default=' ')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class TutorPosting(models.Model):
    email = models.EmailField(('email address'), unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tutor_profile/', default='image3.PNG')
    phone_number = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    
    AAA = 'African American and African Studies' 
    ASL = 'American Sign Language Program'
    AAS = 'American Studies'
    ANTH = 'Anthropology'
    ARCH = 'Archaeology'
    ART = 'Art'
    ASTR = 'Astronomy'
    BIOE = 'Bioethics'
    BIOL = 'Biology'
    CHEM = 'Chemistry'
    CLSC = 'Classics' 
    CSC = 'Cognitive Science'
    CPLT = 'Comparative Literature'
    CWP = 'Creative Writing Program'
    DIS = 'Disability Studies'
    DRMA = 'Drama'
    EAST = 'East Asian Languages, Literatures & Cultures'
    ECON = 'Economics'
    ENGL = 'English'
    ENVI = 'Environmental Sciences'
    ENTP = 'Environmental Thought & Practice'
    EURO = 'European Studies'
    FREN = 'French'
    GSD = 'Global Studies'
    HIST = 'History'
    JWS = 'Jewish Studies'
    LAS = 'Latin American Studies'
    LNGS = 'Linguistics'
    MATH = 'Mathematics' 
    MDST = 'Media Studies'
    MEDV = 'Medieval Studies'
    MIAP = 'Mellon Indigenous Arts Program'
    MESA = 'Middle Eastern & South Asian Languages & Cultures'
    MUSI = 'Music'
    NEUR = 'Neuroscience'
    PHIL = 'Philosophy'
    PHYS = 'Physics'
    PST = 'Political and Social Thought'
    PPL = 'Political Philosophy, Policy & Law'
    PLT = 'Politics'
    PSYC = 'Psychology'
    RELG = 'Religious Studies'
    SLAV = 'Slavic Languages & Literatures'
    SOC = 'Sociology'
    SPAN = 'Spanish, Italian & Portuguese'
    STAT = 'Statistics'
    WGS = 'Women, Gender & Sexuality'
    WRP = 'Writing & Rhetoric Program'
    NA = ' '

    DEPARTMENTS_UVA = ( 
        (AAA, 'African American and African Studies'), 
        (ASL, 'American Sign Language Program'),
        (AAS, 'American Studies'),
        (ANTH, 'Anthropology'),
        (ARCH, 'Archaeology'),
        (ART, 'Art'),
        (ASTR, 'Astronomy'),
        (BIOE, 'Bioethics'),
        (BIOL, 'Biology'),
        (CHEM, 'Chemistry'),
        (CLSC, 'Classics'), 
        (CSC, 'Cognitive Science'),
        (CPLT, 'Comparative Literature'),
        (CWP, 'Creative Writing Program'),
        (DIS, 'Disability Studies'),
        (DRMA, 'Drama'),
        (EAST, 'East Asian Languages, Literatures & Cultures'),
        (ECON, 'Economics'),
        (ENGL, 'English'), 
        (ENVI, 'Environmental Sciences'),
        (ENTP, 'Environmental Thought & Practice'),
        (EURO, 'European Studies'),
        (FREN, 'French'),
        (GSD, 'Global Studies'),
        (HIST, 'History'),
        (JWS, 'Jewish Studies'),
        (LAS, 'Latin American Studies'),
        (LNGS, 'Linguistics'),
        (MATH, 'Mathematics'), 
        (MDST, 'Media Studies'),
        (MEDV, 'Medieval Studies'),
        (MIAP, 'Mellon Indigenous Arts Program'),
        (MESA, 'Middle Eastern & South Asian Languages & Cultures'),
        (MUSI, 'Music'),
        (NEUR, 'Neuroscience'),
        (PHIL, 'Philosophy'),
        (PHYS, 'Physics'),
        (PST, 'Political and Social Thought'),
        (PPL, 'Political Philosophy, Policy & Law'), 
        (PLT, 'Politics'),
        (PSYC, 'Psychology'),
        (RELG, 'Religious Studies'),
        (SLAV, 'Slavic Languages & Literatures'),
        (SOC, 'Sociology'),
        (SPAN, 'Spanish, Italian & Portuguese'),
        (STAT, 'Statistics'),
        (WGS, 'Women, Gender & Sexuality'),
        (WRP, 'Writing & Rhetoric Program'),
        (NA, 'n/a'))

    first_major = models.CharField(max_length=50, choices=DEPARTMENTS_UVA, default=NA)
    second_major = models.CharField(max_length=50, choices=DEPARTMENTS_UVA, default=NA)
    bio = models.TextField(default=' ')
    USER_CHOICES = (
        (1, 'Tutor'),
        (2, 'Tutee'),
        (3, 'Tutor and Tutee'),
    )
    user_type = models.PositiveIntegerField(
        choices=USER_CHOICES, default=1)

class Profile(models.Model):
    user = models.OneToOneField(TUser, on_delete=models.CASCADE)
    first_name = TUser.firstname
    last_name = TUser.lastname
    image = models.ImageField(default='default.png',
                              upload_to='profile_pictures')
    email = TUser.email
    phone_number = TUser.phone_number

    FIRST = 'First Year'
    SECOND = 'Second Year'
    THIRD = 'Third Year'
    FOURTH = 'Fourth Year'
    YEAR_CHOICES = (
        (FIRST, 'First Year'),
        (SECOND, 'Second Year'),
        (THIRD, 'Third Year'),
        (FOURTH, 'Fourth Year'),
    )
    year = models.CharField(max_length=15, choices=YEAR_CHOICES, default=FIRST)

    USER_CHOICES = (
        (1, 'Tutor'),
        (2, 'Tutee'),
        (3, 'Tutor and Tutee'),
    )
    user_type = models.PositiveIntegerField(
        choices=USER_CHOICES, default=1)

    AAA = 'African American and African Studies' 
    ASL = 'American Sign Language Program'
    AAS = 'American Studies'
    ANTH = 'Anthropology'
    ARCH = 'Archaeology'
    ART = 'Art'
    ASTR = 'Astronomy'
    BIOE = 'Bioethics'
    BIOL = 'Biology'
    CHEM = 'Chemistry'
    CLSC = 'Classics' 
    CSC = 'Cognitive Science'
    CPLT = 'Comparative Literature'
    CWP = 'Creative Writing Program'
    DIS = 'Disability Studies'
    DRMA = 'Drama'
    EAST = 'East Asian Languages, Literatures & Cultures'
    ECON = 'Economics'
    ENGL = 'English'
    ENVI = 'Environmental Sciences'
    ENTP = 'Environmental Thought & Practice'
    EURO = 'European Studies'
    FREN = 'French'
    GSD = 'Global Studies'
    HIST = 'History'
    JWS = 'Jewish Studies'
    LAS = 'Latin American Studies'
    LNGS = 'Linguistics'
    MATH = 'Mathematics' 
    MDST = 'Media Studies'
    MEDV = 'Medieval Studies'
    MIAP = 'Mellon Indigenous Arts Program'
    MESA = 'Middle Eastern & South Asian Languages & Cultures'
    MUSI = 'Music'
    NEUR = 'Neuroscience'
    PHIL = 'Philosophy'
    PHYS = 'Physics'
    PST = 'Political and Social Thought'
    PPL = 'Political Philosophy, Policy & Law'
    PLT = 'Politics'
    PSYC = 'Psychology'
    RELG = 'Religious Studies'
    SLAV = 'Slavic Languages & Literatures'
    SOC = 'Sociology'
    SPAN = 'Spanish, Italian & Portuguese'
    STAT = 'Statistics'
    WGS = 'Women, Gender & Sexuality'
    WRP = 'Writing & Rhetoric Program'
    NA = '  '

    DEPARTMENTS_UVA = ( 
        (AAA, 'African American and African Studies'), 
        (ASL, 'American Sign Language Program'),
        (AAS, 'American Studies'),
        (ANTH, 'Anthropology'),
        (ARCH, 'Archaeology'),
        (ART, 'Art'),
        (ASTR, 'Astronomy'),
        (BIOE, 'Bioethics'),
        (BIOL, 'Biology'),
        (CHEM, 'Chemistry'),
        (CLSC, 'Classics'), 
        (CSC, 'Cognitive Science'),
        (CPLT, 'Comparative Literature'),
        (CWP, 'Creative Writing Program'),
        (DIS, 'Disability Studies'),
        (DRMA, 'Drama'),
        (EAST, 'East Asian Languages, Literatures & Cultures'),
        (ECON, 'Economics'),
        (ENGL, 'English'), 
        (ENVI, 'Environmental Sciences'),
        (ENTP, 'Environmental Thought & Practice'),
        (EURO, 'European Studies'),
        (FREN, 'French'),
        (GSD, 'Global Studies'),
        (HIST, 'History'),
        (JWS, 'Jewish Studies'),
        (LAS, 'Latin American Studies'),
        (LNGS, 'Linguistics'),
        (MATH, 'Mathematics'), 
        (MDST, 'Media Studies'),
        (MEDV, 'Medieval Studies'),
        (MIAP, 'Mellon Indigenous Arts Program'),
        (MESA, 'Middle Eastern & South Asian Languages & Cultures'),
        (MUSI, 'Music'),
        (NEUR, 'Neuroscience'),
        (PHIL, 'Philosophy'),
        (PHYS, 'Physics'),
        (PST, 'Political and Social Thought'),
        (PPL, 'Political Philosophy, Policy & Law'), 
        (PLT, 'Politics'),
        (PSYC, 'Psychology'),
        (RELG, 'Religious Studies'),
        (SLAV, 'Slavic Languages & Literatures'),
        (SOC, 'Sociology'),
        (SPAN, 'Spanish, Italian & Portuguese'),
        (STAT, 'Statistics'),
        (WGS, 'Women, Gender & Sexuality'),
        (WRP, 'Writing & Rhetoric Program'),
        (NA, 'n/a'))

    first_major = models.CharField(max_length=50, choices=DEPARTMENTS_UVA, default=NA)
    second_major = models.CharField(max_length=50, choices=DEPARTMENTS_UVA, default=NA)
    bio = models.TextField(default=' ')

    def __str__(self):
        return "%s's profile" % self.user

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Reviews(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #This would be what a tutee would rate a tutor?
    Zero = '0'
    One = '1'
    Two = '2'
    Three = '3'
    Four = '4'
    Five = '5'
    YEAR_CHOICES = (
        (Zero, "No Rating"),
        (One, 'One Star'),
        (Two, 'Two Stars'),
        (Three, 'Three Stars'),
        (Four, 'Four Stars'),
        (Five, 'Five Stars'),
    )
    rating = models.CharField(max_length=3, choices=YEAR_CHOICES, default=Zero)

    #This would be what a tutee would rate a tutor?
    reviews = models.TextField(default= ' ')




#profile signal
@receiver(post_save, sender=TUser)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Request(models.Model):
    sender = models.ForeignKey(
        TUser, models.SET_NULL, related_name="TUser_sender", blank=True, null=True)
    recipient = models.ForeignKey(
        TUser, models.SET_NULL, related_name="TUser_recipient", blank=True, null=True)
    subject = models.CharField(max_length=500, default="")
    description = models.CharField(max_length=500, default="")
    address = map_fields.AddressField(max_length=200, default="164 McCormick Rd, Charlottesville, VA 22903")
    geolocation = map_fields.GeoLocationField(max_length=100,default="")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)


#https://www.twilio.com/blog/2018/05/build-chat-python-django-applications-programmable-chat.html
class Room(models.Model):
    """Represents chat rooms that users can join"""
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    slug = models.CharField(max_length=50)
    validUser1 = models.CharField(default="all",max_length=30)
    validUser2 = models.CharField(default="all",max_length=30)
    latitude = models.FloatField(default=38.036460)
    longitude = models.FloatField(default=-78.506080)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name