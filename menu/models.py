from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='food_images/%Y/%m/%d', blank=True)

    '''
    class meta method dispaly image on menu page order by name.
    '''
    class Meta:
        ordering = ['name']
        # indexes = [
        #     models.Index(fields=['name'])
        # ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:food_list_by_category',
                       args=[self.id, self.slug])


class FoodItem(models.Model):
    category = models.ForeignKey(Menu,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='food_images/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['name']
    #     indexes = [
    #         models.Index(fields=['id', 'slug']),
    #         models.Index(fields=['name']),
    #         models.Index(fields=['-created']),
    #     ]
    class Meta:
        ordering = ['name']
        # indexes = [
        #     models.Index(fields=['name']),
        # ]

    def __str__(self):
        return self.name
    
# Table created to store user details along with food details

class UserDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    table_number = models.IntegerField(default=None, blank=True, null=True)
    food_details = models.CharField(max_length=500, default=None, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10,
                                decimal_places=2, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)