from django.contrib.auth import get_user_model
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView

from category_shop.models import Category
from color_shop.models import ClotheColor
from product_shop.models import Product
from shopping_bag_shop.forms import ShoppingBagForm
from shopping_bag_shop.models import ShoppingBag, ShoppingBagDetail
from size_shop.models import ClotheSize

User = get_user_model()


class ProductList(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context


class ProductListByOrder(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        sort = self.kwargs.get('sort')
        products = Product.objects.order_by(sort)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context


class ProductListByColor(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(color__title=self.kwargs.get('color'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context


class ProductListBySize(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(size__title=self.kwargs.get('size'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context


def single_product_view(request, pk):
    product = Product.objects.get(id=pk)
    relative_products = Product.objects \
                            .filter(category__in=product.category.all()) \
                            .annotate(same_category_count=Count('category')) \
                            .exclude(id=pk).order_by('-same_category_count', 'sold')[:4]

    shop_form = ShoppingBagForm(request.POST or None)
    shop_form.fields['color'].choices = [(color.id, color.title) for color in product.color.all()]
    shop_form.fields['size'].choices = [(size.id, size.title) for size in product.size.all()]
    if request.method == 'POST':
        if request.user.is_authenticated:
            if shop_form.is_valid():
                count = shop_form.cleaned_data['count']
                color_id = shop_form.cleaned_data['color']
                size_id = shop_form.cleaned_data['size']
                color = ClotheColor.objects.get(id=color_id)
                size = ClotheSize.objects.get(id=size_id)
                user_id = request.user.id
                user_shopping_bag = ShoppingBag.objects.filter(user_id=user_id, finished=False).first()
                if not user_shopping_bag:
                    user = User.objects.get(id=user_id)
                    user_shopping_bag = ShoppingBag.objects.create(user=user)
                shopping_bag_detail = ShoppingBagDetail.objects.create(
                    shopping_bag=user_shopping_bag,
                    count=count,
                    color=color,
                    size=size,
                    product=product
                )
                url = reverse('single_product', kwargs={'pk': product.id})
                return redirect(url)
            else:
                print(shop_form.errors)
        else:
            return redirect('login')
    context = {
        'product': product,
        'shop_form': shop_form,
        'relative_products': relative_products
    }
    return render(request, 'product_shop/single_product.html', context)


class SearchProductView(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        search_word = self.request.GET.get('search').strip()
        if search_word:
            products = Product.objects.filter(title__icontains=search_word)
            return products
        else:
            product = Product.objects.all()
            return product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context


class SpecialProductViews(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(special=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context


class NewProductsView(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context


class MostPopularProducts(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all().order_by('-sold')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['sizes'] = ClotheSize.objects.all()
        context['colors'] = ClotheColor.objects.all()
        return context
