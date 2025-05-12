from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import gettext_lazy as _

from color_shop.models import ClotheColor
from product_shop.models import Product
from size_shop.models import ClotheSize

User = get_user_model()


class ShoppingBag(models.Model):
    shipping_cost = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_bag')
    created_at = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    post_code = models.IntegerField(null=True, blank=True)
    finished = models.BooleanField(default=False)

    @property
    def total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += (item.count * item.product.price)
        return total_price

    def save(self, *args, **kwargs):
        if self.__class__.objects.filter(finished=False).exclude(pk=self.id).exists():
            return
        else:
            return super().save(*args, **kwargs)


class ShoppingBagDetail(models.Model):
    color = models.ForeignKey(ClotheColor, on_delete=models.CASCADE, related_name='color')
    size = models.ForeignKey(ClotheSize, on_delete=models.CASCADE, related_name='size')
    count = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True, blank=True)
    shopping_bag = models.ForeignKey(ShoppingBag, on_delete=models.CASCADE, related_name='items')

    @property
    def price(self):
        return self.product.price * self.count


OSTAN_CHOICES = [
    ('کرمان', 'کرمان'),
    ('سیستان و بلوچستان', 'سیستان و بلوچستان'),
    ('خراسان جنوبی', 'خراسان جنوبی'),
    ('فارس', 'فارس'),
    ('خراسان رضوی', 'خراسان رضوی'),
    ('اصفهان', 'اصفهان'),
    ('سمنان', 'سمنان'),
    ('یزد', 'یزد'),
    ('هرمزگان', 'هرمزگان'),
    ('خوزستان', 'خوزستان'),
    ('آذربایجان شرقی', 'آذربایجان شرقی'),
    ('آذربایجان غربی', 'آذربایجان غربی'),
    ('کردستان', 'کردستان'),
    ('مرکزی', 'مرکزی'),
    ('خراسان شمالی', 'خراسان شمالی'),
    ('لرستان', 'لرستان'),
    ('کرمانشاه', 'کرمانشاه'),
    ('مازندران', 'مازندران'),
    ('بوشهر', 'بوشهر'),
    ('زنجان', 'زنجان'),
    ('گلستان', 'گلستان'),
    ('ایلام', 'ایلام'),
    ('همدان', 'همدان'),
    ('اردبیل', 'اردبیل'),
    ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'),
    ('قزوین', 'قزوین'),
    ('کهگیلویه و بویراحمد', 'کهگیلویه و بویراحمد'),
    ('گیلان', 'گیلان'),
    ('تهران', 'تهران'),
    ('قم', 'قم'),
    ('البرز', 'البرز'),
]


class ShoppingBagShippingDetail(models.Model):
    first_name = models.CharField(verbose_name=_('نام'), max_length=50)
    last_name = models.CharField(verbose_name=_('نام خانوادگی'), max_length=50)
    phone = models.CharField(verbose_name=_('شماره تماس'), max_length=20)
    email = models.EmailField(verbose_name=_('ایمیل'), )
    address = models.TextField(verbose_name=_('آدرس'))
    post_code = models.CharField(verbose_name=_('کد پستی'), max_length=30)
    ostan = models.CharField(verbose_name=_('استان'), max_length=60, choices=OSTAN_CHOICES)
    city = models.CharField(verbose_name=_('شهر'), max_length=30)
    shopping_bag = models.OneToOneField(
        ShoppingBag, verbose_name=_('سبد خرید'),
        related_name='shipping_detail',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.email}-address'
