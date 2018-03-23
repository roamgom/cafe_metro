from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    LINE_CHOICES = (
        (2, '2호선'),
    )

    line = models.PositiveSmallIntegerField(max_length=1, choices=LINE_CHOICES)
    name = models.CharField(max_length=80)
    # location = models.IntegerField()


class Cafe(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    # remind about the value for GPS
    location = models.CharField()
    # average star depend on Review model
    latest_review_uploaded_time = models.DateTimeField(null=True)

    score = models.PositiveSmallIntegerField()
    # run function without call()

    # @property
    # happen when get called like get_score
    def get_score(self):
        if self.latest_review_uploaded_time == self.review_set.latest().upload_time:
            return self.score
        self.score = sum(list(map(lambda x: x.star, self.review_set.all()))) / self.review_set.count()
        self.save()
        return self.score


class CafeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(Cafe)


class Review(models.Model):
    id = models.ManyToManyField(CafeUser)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    upload_time = models.TimeField(auto_now_add=True)
    # use decimal instead of float field
    # use decimal in currency etc.
    star = models.PositiveSmallIntegerField()
    review = models.TextField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.cafe.latest_review_uploaded_time = self.upload_time
        # call save from models.Model save before overriding
        super(Review).save(force_insert=False, force_update=False, using=None,
                           update_fields=None)
