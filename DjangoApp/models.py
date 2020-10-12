from django.db import models

class table1(models.Model):

    PROJECTS_ENROLLED = (
        ('p1', 'Project1'),
        ('p2', 'Project2'),
        ('p3', 'Project3'),
        ('p4', 'Project4'),
    )
    #help_text: provides a text label for HTML forms
    #verbose_name: provides human-readable name for the field
    field1 = models.IntegerField('user Id',primary_key = True)
    field2 = models.CharField('user Name', max_length = 20)
    field3 = models.CharField('project', max_length = 200, help_text = 'Select Project', choices = PROJECTS_ENROLLED)
    # list_display = ('user_name', 'user_name', 'user_name')
    # fields = ['user_id', ('user_name', 'user_name')]
    
    # list_filter = ('user id')

    #EmailField: used to store and validate email addresses.
    #FileField and ImageField: used to upload files and images respectively. 
    #AutoField: special type of IntegerField that automatically increments.
    
    #ForeignKey: specify a one-to-many relationship to another database model.
    #ManyToManyField: specify a many-to-many relationship 

    #method __str__() is used to return a human-readable string for each object
    def __str__(self):
        return f'{self.field1} , {self.field2} , {self.field3}'

    #def get_absolute_url(self):


    # metadata: used to control default ordering of records
    # class Meta:
    # ordering = ['field1','-field2'] #minus symbol (-) to reverse the sorting order.

    # Define the admin class
    # @admin.register(table2)
    # class AuthorAdmin(admin.ModelAdmin):
    #     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

class viewnotes(models.Model):
    noteid = models.AutoField(primary_key=True)
    notes = models.CharField('notes', max_length = 200)
    def __str__(self):
        return self.notes
 
