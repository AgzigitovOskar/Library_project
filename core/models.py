from django.db import models


class Reader(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    phone = models.CharField('№ телефона', max_length=20)
    is_active = models.BooleanField('Активен', default=True)
    active_books = models.ManyToManyField('Book', blank=True, verbose_name="Взятые книги")
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    edited_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"


class Book(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    description = models.TextField('Описание', null=True, blank=True)
    sheets = models.PositiveSmallIntegerField('Кол-во страниц')
    quantity = models.PositiveSmallIntegerField('Кол-во шт.', default=0)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    edited_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return f"{self.author.name[0].title()}.{self.author.surname} - {self.title}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Author(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    photo = models.ImageField(null=True, blank=True, upload_to='author_fotos/', verbose_name="Фотография")
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    edited_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
