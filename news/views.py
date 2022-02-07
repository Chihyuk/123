from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from .models import *

# -2022.01.24 park_jong_won
import logging
logger = logging.getLogger('news')


# Create your views here.

def log(req):
    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        
        logger.info(f"index POST log test => [scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
        # logger.info(f"index POST log test")
    else:
        logger.info("index GET log test")


def want_category(c_id):
    query = f"""
        select n.n_id, p_id, n.cd_id, n_title, nd_img, n_input, o_link, nso_id, nso_content, c_id 
        from News n 
        inner join N_summarization_one nso on n.n_id = nso.n_id 
        inner join N_category_detail det on n.cd_id = det.cd_id
        where c_id = {c_id}"""
    return query

def find_cat(c_id):
    query = f"""
    select c_id, c_name from N_category
    """
    return query

class ArticleListView(TemplateView):
    template_name = 'autopage.html'
    c_id = 100
    query = want_category(c_id)
    cat_query = find_cat(c_id)
    news_list = News.objects.raw(query)
    category = N_Category.objects.raw(cat_query)

    def get(self, req, *args, **kwargs):
        print(req.GET)
        page = req.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
        paginator = Paginator(self.news_list, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
        page_obj = paginator.page(page)

        ctx = {
            'category' : self.category,
            'page_obj': page_obj,
            'news_list' : self.news_list
        }

        return self.render_to_response(ctx)

    def get_queryset(self):
        if not self.query:
            self.query = News.objects.all()
        return self.query
    
    
def test(req):
    log(req)
    query = want_category(100)
    news_list = News.objects.raw(query) #models.py Board 클래스의 모든 객체를 board_list에 담음

    # news_list100 페이징 처리
    page = req.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(news_list, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    testhtml = testHTML(page_obj, news_list)


    return render(req, "test.html", {'page_obj100':page_obj, 'news_list100':news_list, 'testhtml':testhtml})





def index(req):

    log(req)
    query100 = want_category(100)
    news_list100 = News.objects.raw(query100) #models.py Board 클래스의 모든 객체를 board_list에 담음
    query101 = want_category(101)
    news_list101 = News.objects.raw(query101) 
    query102 = want_category(102)
    news_list102 = News.objects.raw(query102) 
    query103 = want_category(103)
    news_list103 = News.objects.raw(query103) 
    query104 = want_category(104)
    news_list104 = News.objects.raw(query104) 
    query105 = want_category(105)
    news_list105 = News.objects.raw(query105) 

    # news_list100 페이징 처리
    page100 = req.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator100 = Paginator(news_list100, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj100 = paginator100.page(page100) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    page101 = req.GET.get('page', '1')
    paginator101 = Paginator(news_list101, '10')
    page_obj101 = paginator101.page(page101)

    page102 = req.GET.get('page', '1')
    paginator102 = Paginator(news_list102, '10')
    page_obj102 = paginator102.page(page102)

    page103 = req.GET.get('page', '1')
    paginator103 = Paginator(news_list103, '10')
    page_obj103 = paginator103.page(page103)

    page104 = req.GET.get('page', '1')
    paginator104 = Paginator(news_list104, '10')
    page_obj104 = paginator104.page(page104)

    page105 = req.GET.get('page', '1')
    paginator105 = Paginator(news_list105, '10')
    page_obj105 = paginator105.page(page105)

    return render(req, "index.html", {'page_obj100':page_obj100, 'news_list100':news_list100, 'page_obj101':page_obj101, 'news_list101':news_list101, 'page_obj102':page_obj102, 'news_list102':news_list102, 'page_obj103':page_obj103, 'news_list103':news_list103, 'page_obj104':page_obj104, 'news_list104':news_list104, 'page_obj105':page_obj105, 'news_list105':news_list105})


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
