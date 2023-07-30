from django.db import models

from core.validators import RussianPhoneValidator, BookNegativeSheetsValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    edited_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    # inv_number = models.IntegerField('Инв.номер', blank=True)
    title = models.CharField('Название', max_length=50)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    description = models.TextField('Описание', null=True, blank=True)
    sheets = models.PositiveSmallIntegerField('Кол-во страниц', default=0, validators=[BookNegativeSheetsValidator()])
    # quantity = models.PositiveIntegerField('Кол-во шт.', default=0)
    quantity = models.PositiveSmallIntegerField('Кол-во шт.', default=0)

    def __str__(self):
        return f"{self.author.name[0].title()}.{self.author.surname} - {self.title}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Author(BaseModel):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    photo = models.ImageField('Фотография', upload_to='author_fotos/')

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        unique_together = ('name', 'surname')


class Reader(BaseModel):
    # class Status(models.TextChoices):
    #     is_active = 'активен'
    #     not_active = 'не активен'

    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    # phone = PhoneNumberField(unique=True, null=False, blank=False)
    phone = models.CharField('№ телефона', max_length=20, validators=[RussianPhoneValidator()])
    # status = models.CharField(max_length=10, choices=Status.choices, default=Status.is_active)
    # is_active = models.CharField('Активен', max_length=10, choices=Status.choices, default=Status.is_active)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    active_books = models.ManyToManyField(Book, blank=True, verbose_name="Взятые книги")

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
