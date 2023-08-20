from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Store, Category, Ages, GenderType
from .forms import NewPostForm


def index_store(request):

    o_l = Store.objects.all().order_by("-date")
    # o_l = stores.objects.filter(available=True).order_by("-update")
    # o_l = stores.available_post.all()

    cat = Category.objects.all()

    gender_type = GenderType.objects.all()

    age = Ages.objects.all()

    """" pagination """
    page = request.GET.get('page')
    paginator = Paginator(o_l, 3)

    try:
        store = paginator.page(page)
    except EmptyPage:
        store = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        store = paginator.page(1)

    context = {"stores": store,
               "cats": cat,
               "gender_types": gender_type,
               "ages": age}

    return render(request,
                  'Store/storesIndex.html',
                  context)


def detail_stores(request, category, slug):
    # store = Stores.objects.get(category__name=category, slug=slug)
    store = get_object_or_404(Store, category__name=category, slug=slug)

    return render(request,
                  'Store/storesDetail.html',
                  {"store": store})


def share_post(request, category, slug):
    store_share = get_object_or_404(Store, category__name=category, slug=slug)

    print(store_share.get_absolute_url())

    return render(request,
                  "ToysStore/share_form.html",
                  {"store_share": store_share})


def send_post(request, category, slug):
    p = get_object_or_404(Store, category__name=category, slug=slug)
    from_ = request.POST.get("form")
    to_ = request.POST.get("to")
    caption = request.POST.get("caption")

    send_mail(subject=p.name,
              from_email=from_,
              recipient_list=[to_, ],
              fail_silently=False,
              message=caption + f"read this article at http://127.0.0.1:8000/{p.get_absolute_url()}")

    return redirect("StoreApp:index")


@login_required(login_url="account:login")
def create_new_post(request):
    if request.method == "POST":
        form = NewPostForm(data=request.POST)
        if form.is_valid():
            post = form.save(comit=True, request=request)
            post.save()

            return redirect("StoreApp:index")

    else:
        form = NewPostForm()

    return render(request,
                  "Store/create_new_post.html",
                  {"form": form})
