from mongoengine import *

connect('test')


"""
This code is messed up. It's just a template for something I will be writing in the near future.

class Refs(Document):
    link = ListField()
    
class Keywords(Document):
    refkeys = DictField()

class Title(Document):
    name = StringField()

class Card(Document):
    card_object = GenericReferenceField()

refs = Refs(link=())
refs.save()

keywords = Keywords(refkeys={})
keywords.save()

Card(card_object=refs).save()
Card(card_object=keywords).save()
"""
