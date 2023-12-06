from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_register = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Product(models.Model):
    """
    В этом примере, я добавил поле `likes`, которое является полем ManyToMany к модели `User`, чтобы отслеживать, какие пользователи поставили лайк продукту.
    Метод `user_has_liked` проверяет, лайкнул ли конкретный пользователь продукт. Метод `toggle_like` добавляет или удаляет лайк в зависимости от того, был ли лайк от данного пользователя.
    Также, в методе `save`, я обновляю поле `counter_like` при каждом сохранении объекта `Product` так, чтобы оно всегда отражало актуальное количество лайков.
    Теперь, когда вы используете `toggle_like`, это будет добавлять или удалять лайк в зависимости от текущего состояния, и пользователь сможет поставить только один лайк на продукт.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_publication = models.DateTimeField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True)
    total_view = models.IntegerField(editable=False, default=0)
    likes = models.ManyToManyField(CustomUser, related_name='liked_products', blank=True)

    def user_has_liked(self, user):
        """
        Проверка, лайкнул ли пользователь этот продукт
        """
        return self.likes.filter(id=user.id).exists()

    def toggle_like(self, user):
        """
        Добавление/удаление лайка от пользователя
        """
        if self.user_has_liked(user):
            self.likes.remove(user)
        else:
            self.likes.add(user)

    def save(self, *args, **kwargs):
        """
        Сохранение объекта и обновление счетчика лайков при изменении
        """
        self.counter_like = self.likes.count()
        super().save(*args, **kwargs)

    def counter_view(self):
        self.total_view += 1
        self.save()

