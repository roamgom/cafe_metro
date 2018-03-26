from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    LINE_CHOICES = (
        (2, '2호선'),
    )

    line = models.PositiveSmallIntegerField(choices=LINE_CHOICES)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Cafe(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)

    # remind about the value for GPS
    location = models.CharField(max_length=300)
    # average star depend on Review model
    latest_review_uploaded_time = models.DateTimeField(null=True)

    score = models.FloatField(default=0)

    # run function without call()

    # @property
    # get cafe average score by review stars
    def get_score(self):
        if self.latest_review_uploaded_time == self.review_set.latest(field_name='upload_time'):
            return self.score
        # self.latest_review_uploaded_time = self.review_set.latest().upload_time
        self.score = round(sum(list(map(lambda x: x.star, self.review_set.all()))) / self.review_set.count(), 1)
        super(Cafe, self).save()
        return self.score

    def __str__(self):
        return self.name


class CafeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(Cafe)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    # star rank between 1-5
    STAR_CHOICES = tuple((i, str(i)) for i in range(1, 6))

    user = models.ForeignKey(CafeUser, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now=True)
    # use decimal instead of float field
    # use decimal in currency etc.
    star = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    title = models.CharField(max_length=200, default='')
    review = models.TextField()

    def save(self, *args, **kwargs):
        self.cafe.latest_review_uploaded_time = self.upload_time
        # call save from models.Model save before overriding
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('upload_time',)
