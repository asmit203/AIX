from django.db import models


# create the model of the feature of model here
# write the name of variable of fields
class Feature(models.Model):
    experience=models.FloatField(default=0)
