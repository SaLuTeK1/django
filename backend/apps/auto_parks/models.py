from django.db import models


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=30)
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name='auto_parks')