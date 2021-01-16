from django.db import models


class CategoryFeature(models.Model):
    category = models.ForeignKey("shop.Category", verbose_name='Категория', on_delete=models.CASCADE)
    feature_name = models.CharField(verbose_name='Имя ключа для категории', max_length=50)
    feature_filter_name = models.CharField(verbose_name='Имя для фильтра', max_length=50)
    unit = models.CharField(max_length=50, verbose_name='Единица измерения', null=True, blank=True)

    class Meta:
        unique_together = ('category', 'feature_name', 'feature_filter_name')
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return f"{self.category.title} | {self.feature_name}"


class FeatureValidator(models.Model):
    category = models.ForeignKey("shop.Category", verbose_name='Категория', on_delete=models.CASCADE)
    feature_key = models.ForeignKey(CategoryFeature, verbose_name='Ключ характеристики', on_delete=models.CASCADE)
    valid_feature_value = models.CharField(max_length=100, verbose_name='Валидное значение')

    class Meta:
        verbose_name = 'Валидатор'
        verbose_name_plural = 'Валидаторы'

    def __str__(self):
        return f"Категория {self.category.title} | " \
               f"Характеристика {self.feature_key.feature_name} | " \
               f"Валидное значение {self.valid_feature_value}"


class ProductFeatures(models.Model):
    product = models.ForeignKey("shop.Product", verbose_name='Товар', on_delete=models.CASCADE)
    feature = models.ForeignKey(CategoryFeature, verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.CharField(max_length=255, verbose_name='Значение')

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'

    def __str__(self):
        return f"Товар - {self.product.title} | " \
               f"{self.feature.feature_name} | " \
               f"Значение - {self.value}"
