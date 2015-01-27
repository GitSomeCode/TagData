from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length = 30, default = "", blank = False)
  count = models.IntegerField(default = 0, blank = False)
  relation = models.ManyToManyField("self", symmetrical = False, through ='TagRelation')
  tag_slug = models.SlugField(blank = False, default = "", unique = True)
  
  def __unicode__(self):
    return "%s" %(self.name[:24])
  
  def save(self, *args, **kwargs):
    if not self.id:
      self.tag_slug = slugify(self.name)
      
    super(Tag, self).save(*agrs, **kwargs)
    
  
class TagRelation(models.Model):
  tag_to = models.ForeignKey('Tag', blank = False, related_name = "tag_to")
  tag_from = models.ForeignKey('Tag', blank = False, related_name = "tag_from")
  metric = models.FloatField(default = 0.0000, blank = False)

  class Meta:
    unique_together = ('tag_to', 'tag_from')
  
  def __unicode__(self):
    return "%s" %(self.tag_to.name + " : " + self.tag_from.name)