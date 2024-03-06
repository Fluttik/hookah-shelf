from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
MAX_CHAR_LENGTH = 100


class Lines(models.Model):
    """Модель линеек табака."""
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name='lines',
        verbose_name='Компания'
    )

    name = models.CharField(
        verbose_name='Линейка',
        max_length=MAX_CHAR_LENGTH,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Линейка'
        verbose_name_plural = 'Линейки'

    def __str__(self):
        return self.name


class Company(models.Model):
    """Модель табачных компаний."""
    name = models.CharField(
        verbose_name='Название компании',
        max_length=MAX_CHAR_LENGTH,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Tobacco(models.Model):
    """Модель табака."""
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name='Компания'
    )
    tobacco_line = models.ForeignKey(
        Lines,
        on_delete=models.CASCADE,
        verbose_name='Линейка',
    )
    name = models.CharField(
        verbose_name='Наименование',
        max_length=MAX_CHAR_LENGTH,
    )
    flavor = models.ManyToManyField(
        'Flavor',
        related_name='tobacco',
        db_index=True,
        verbose_name='Аромат',
    )
    strength = models.ForeignKey(
        'Strength',
        on_delete=models.CASCADE,
        verbose_name='Крепкость',
    )
    description = models.TextField(
        verbose_name='Описание табака',
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['company', 'tobacco_line', 'name'],
            name='tobacco_unique'
            )]
        ordering = ('company', 'tobacco_line', 'name')
        verbose_name = 'Табак'
        verbose_name_plural = 'Табаки'

    def __str__(self):
        return self.name


class Flavor(models.Model):
    """Модель ароматов табака."""
    name = models.CharField(
        verbose_name='Аромат',
        max_length=MAX_CHAR_LENGTH,
        unique=True,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Аромат'
        verbose_name_plural = 'Ароматы'

    def __str__(self):
        return self.name


class Strength(models.Model):
    """Модель крепости табака."""
    name = models.CharField(
        verbose_name='Крепкость',
        max_length=MAX_CHAR_LENGTH,
        unique=True,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Крепость'
        verbose_name_plural = 'Крепость'

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Модель для избранных табаков."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )
    tobacco = models.ForeignKey(
        Tobacco,
        on_delete=models.CASCADE,
        verbose_name='Избранный табак',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Mixes(models.Model):
    """Модель для миксов из несольких табаков."""
    author = models.ForeignKey(
        User,
        related_name='mix',
        verbose_name='Автор микса',
        on_delete=models.CASCADE,
        db_index=True,
    )
    name = models.CharField(
        verbose_name='Микс',
        max_length=MAX_CHAR_LENGTH,
        unique=True,
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    tobaccos = models.ManyToManyField(
        Tobacco,
        through='MixesTobacco',
        db_index=True,
    )

    class Meta:
        verbose_name = 'Микс'
        verbose_name_plural = 'Миксы'


class MixesTobacco(models.Model):
    """Модель для связи миксов с табаком и его количеством."""
    mix = models.ForeignKey(
        Mixes,
        on_delete=models.CASCADE,
        related_name='mix_tobacco',
        verbose_name='Микс',
        help_text='Микс',
    )
    tobacco = models.ForeignKey(
        Tobacco,
        on_delete=models.CASCADE,
        verbose_name='Табак',
        help_text='Табак',
    )
    amount = models.PositiveSmallIntegerField(verbose_name='Процент')

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
