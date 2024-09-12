Django Meta Options Explanations
================================

1. `db_table`:
   This option is used to specify a custom name for the database table associated with a Django model.
   ye Data Base ka Table Name Change Karne ke Kamm Ayta ha

   Example:

   .. code-block:: python

      class Book(models.Model):
          class Meta:
              db_table = 'my_custom_table_name'


2. `ordering`:
   This option is used to define the default ordering of the records when you query the model.
   Ye Price ko ordering Karne ke Kamm Ayta ha

   Example:

   .. code-block:: python

      class Book(models.Model):
          price = models.DecimalField(max_digits=10, decimal_places=2)
          
          class Meta:
              ordering = ['price']


3. `verbose_name` and `verbose_name_plural`:
   These options are used to define a more human-readable name for the model and its plural form.
   if in Django DataBase Name: Books it change into Book Using verbose_name or verbose_name_prural

   Example:

   .. code-block:: python

      class Book(models.Model):
          class Meta:
              verbose_name = 'Book'
              verbose_name_plural = 'Books'


4. `unique_together`:
   This option is used to enforce that a combination of fields must be unique across the database table.
   Ager Data Base pe same Nmae Ha to ye or Dubara ager wahi name ka kuch v create kare to wo Nhi Karne dega

   Example:

   .. code-block:: python

      class Student(models.Model):
          name = models.CharField(max_length=100)
          age = models.IntegerField()
          
          class Meta:
              unique_together = ('name', 'age')


5. `index_together`:
   This option is used to create a composite index on multiple fields, which can optimize queries that filter on those fields together.
   
   iska matlan ye ha ki ager me index_together = [('college', 'gender'),] ye do rakhdo to gender male rakhdu to har male 1 puree line pe ayege

   Example:

   .. code-block:: python

      class Student(models.Model):
          college = models.ForeignKey(Collage, on_delete=models.CASCADE)
          gender = models.CharField(max_length=10)
          
          class Meta:
              index_together = [('college', 'gender')]

6. `abstract`:
    This option is used to define a model as abstract. An abstract model is not created as a database table. Instead, it serves as a base class from which other models can inherit fields and methods.
           
    Example:
           
    .. code-block:: python
           
        class BaseModel(models.Model):
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
           
        class Meta:
        abstract = True
           
    class Book(BaseModel):
        title = models.CharField(max_length=100)
           
    class Author(BaseModel):
        name = models.CharField(max_length=100)
           
In this example, `BaseModel` is an abstract model that provides `created_at` and `updated_at` fields to any model that inherits from it, like `Book` and `Author`. However, `BaseModel` itself will not create a corresponding database table.

            