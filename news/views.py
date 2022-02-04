from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# -2022.01.24 park_jong_won
import logging
logger = logging.getLogger('news')


# Create your views here.
def index(req):
    raw = f"select ns_id, ns_content from N_summarization where ns_id = 3"
    NC = N_summarization.objects.raw(raw)
    # ns = NC[0].ns_content

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        
        logger.info(f"index POST log test => [scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
        # logger.info(f"index POST log test")
    else:
        logger.info("index GET log test")

    query = "select n.n_id, p_id, cd_id, n_title, nd_img, n_input, o_link, nso_id, nso_content from News n inner join N_summarization_one nso on n.n_id = nso.n_id"
    news_list = News.objects.raw(query) #models.py Board 클래스의 모든 객체를 board_list에 담음
    # news_list 페이징 처리
    page = req.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    # return render(req, "index.html", {'banner': ns})
    return render(req, "index.html", {'page_obj':page_obj, 'news_list':news_list})


# def i_sum(req):
#     raw = f"select ns_id, ns_content from N_summarization where ns_id = 9"
#     NC = N_summarization.objects.raw(raw)
#     ns = NC[0].ns_content

#     return render(req, "index.html", {'i_sum': ns})

# def i_sum2(req):
#     raw = f"select ns_id, ns_content from N_summarization where ns_id = 5"
#     NC = N_summarization.objects.raw(raw)
#     ns = NC[0].ns_content

#     return render(req, "index.html", {'i_sum2': ns})

# def i_sum3(req):
#     raw = f"select ns_id, ns_content from N_summarization where ns_id = 7"
#     NC = N_summarization.objects.raw(raw)
#     ns = NC[0].ns_content

#     return render(req, "index.html", {'i_sum3': ns})        


def author(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "author.html", context=context)


def politics(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "politics.html", context=context)


def post(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "post.html", context=context)


def business(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "business.html", context=context)


def sports(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "sports.html", context=context)


def art(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "art.html", context=context)


def world(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "world.html", context=context)


def travel(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "travel.html", context=context)


def contactus(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "contactus.html", context=context)


def banner1(req):
    raw = f"select nc_id, n_content from N_content where nc_id = 1"
    NC = N_content.objects.raw(raw)
    ns = NC[0].n_content
    return render(req, 'banner1.html', {'banner1': ns})


def banner2(req):
    raw = f"select nc_id, n_content from N_content where nc_id = 1"
    NC = N_content.objects.raw(raw)
    ns = NC[1].n_content
    return render(req, 'banner1.html', {'banner2': ns})


def banner3(req):
    raw = f"select nc_id, n_content from N_content where nc_id = 1"
    NC = N_content.objects.raw(raw)
    ns = NC[2].n_content
    return render(req, 'banner1.html', {'banner3': ns})
