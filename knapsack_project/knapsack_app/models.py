from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    value = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = "knapsack_app"
