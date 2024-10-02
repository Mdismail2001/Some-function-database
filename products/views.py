from django.shortcuts import render
from .models import Product,Category
from django.db.models import Avg, Count

def view(request):
    products = Product.objects.all().order_by('price').select_related("category")
    
    categorys=( Category.objects.all()
               .annotate(product_count=Count("product"))
               .prefetch_related("product_set") )
    
    # # terminal a print kore dekhar jonno 
    # for product in products:     
    #     print(product, product.category)
    # for category in categorys:
    #     print(category,category.product_set.all())
    
    # aggregate = kono kisor average ber korar jonno 
    # annoate epecific kno field ar data janar jonno like how many products in every category  
    # optimigation , database a query set komanor jonno use kora hoy forward ar jonno select_related reverse ar jonno prefetch_related
    
    
    price_avg = products.aggregate(Avg("price"))['price__avg']
    # print(price_avg)
    
    
    
    return render(request, 'views.html', {'products': products,'categorys': categorys, 'avg_price': price_avg})  
