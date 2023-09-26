from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category
from django.db.models import Q
from carts.models import CartItem
from carts.views import _cart_id
from orders.models import OrderProduct
from .models import ReviewRating
from .forms import ReviewForm, ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        "products":  paged_products,
        'product_count': product_count
    }
    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(
            request), product=single_product).exists()
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(
                user=request.user, product_id=single_product.id).exists()
        except Exception:
            orderproduct = None
    else:
        orderproduct = None
    reviews = ReviewRating.objects.filter(
        product_id=single_product.id, status=True)
    context = {
        "single_product": single_product,
        "in_cart": in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    products = Product.objects.none()
    product_count = 0
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, "store/store.html", context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(
                request, "Thank you! Your review has been updated.")
            return redirect(url)
        except Exception:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(
                    request, "Thank you! Your review has been submitted.")
                return redirect(url)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Product added successfully.")
            return redirect("products")
    else:
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, "store/add_product.html", context)


def products(request):
    products_list = Product.objects.all()
    context = {
        "products_list": products_list,
    }
    return render(request, "store/products_list.html", context)


@login_required(login_url='login')
def Edit_product(request, pk):
    product = None
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        messages.error(request, "Category not found.")
        return redirect("categorie")
        pass

    if request.method == "POST":
        product_form = ProductForm(
            request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Your Category has been updated.")
            return redirect("products")
    else:
        form = ProductForm(instance=product)

    context = {
        "form": form,
        "product": product,
    }
    return render(request, 'store/edit_product.html', context)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect("products")

    context = {
        "product": product,
    }
    return render(request, "store/delete_product.html", context)
