from django.db import models

# Create your models here.
class TicketBook(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False, verbose_name='Email Address', help_text='Enter a valid email address.')
    countryName = models.CharField(max_length=100, blank=False, null=False, verbose_name='Write your country name')
    pfrom = models.CharField(max_length=100, blank=False, null=False, verbose_name='Write your depature airport name')
    pto = models.CharField(max_length=100, blank=False, null=False, verbose_name='Write your arriavle airport name')
    depatureDate = models.DateTimeField(verbose_name='Departure Date')
    returnDate = models.DateField(verbose_name='Return Date')
    OPTIONS = (
        ('oneway', 'Oneway'),
        ('roundway', 'Round'),
    )

    chosen_option = models.CharField(
        choices=OPTIONS,
        max_length=20,
    )
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}         Email: {self.email}"
    


