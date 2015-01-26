from django.test import TestCase
from tags.models import Tag, TagRelation
from main import *

# Create your tests here.
class ManageRelation(TestCase):
  def setup(self):
    pass
  
  def test_calc(self):
    exampleTuple = (("country", 20),("western", 30))
    percent = 0.1
    self.assertEqual(calc(exampleTuple,percent), ("country", "western", 0.175))
  
  
  def test_non_existing_relation(self):
    tag1_name = "dance"
    tag2_name = "pop"
    self.assertEqual(None, getRelation(tag1_name, tag2_name))
    
    
  def test_existing_relation(self):
    tag1 = Tag(name="rock", count=50)
    tag2 = Tag(name="acoustics", count=35)
    
    tag1.save()
    tag2.save()
    
    rel = TagRelation(tag_to=tag1, tag_from=tag2, metric=0.7657)
    rel.save()
    
    self.assertEqual(rel, getRelation(tag1.name, tag2.name))
  
  
  def test_basic(self):
    a = 1
    self.assertEqual(1, a)
  