# setting
# ELASTICSEARCH_DSL = {
#     'default': {
#         'hosts': ['http://localhost:9200'],
#         'verify_certs': False
#     },
# }
#  "django_elasticsearch_dsl",

#  python .\manage.py search_index #this cmd is for u check what inside your elastic search
# CommandError: No action specified. Must be one of '--create','--populate', '--delete' or '--rebuild' .

from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry
from .models import Products,Brand

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    brand_names = fields.ObjectField(properties={
        'brand_name': fields.KeywordField(),
    })
    brand_names=fields.ObjectField(property={
        'brand_name':fields.KeywordField(),
    })
    class Django:
        model = Products
        fields = [
            'Title',
            'Description',
            'Category',
            'Price', 
            'brand',
            'SKU',
        ]