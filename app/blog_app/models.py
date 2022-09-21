from django.db import models


class PostCategory(models.Model):
    title = models.CharField(verbose_name="Категория", max_length=20)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

  
class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    # ForeignKey-внешний ключ; on_delete=models.CASCADE-каскадное удаление
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name="Категория")
    post_img = models.ImageField(verbose_name="Фото новости", upload_to="post/%Y/%m/%d/")
    text = models.TextField(verbose_name="Текст")
    created_time = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_time = models.DateField(verbose_name="Дата обновления", auto_now=True)
    is_published = models.BooleanField(verbose_name="Опубликовать", default=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
