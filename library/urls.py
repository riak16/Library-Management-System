from django.conf.urls import include, url
import patterns
from django.contrib import admin
from library_app import views
# from library_app.views import periods, periods_show, remove_instance

# urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns =[
#public urls
    url(r'^$',views.home, name='home'),
    url(r'^about/$',views.about, name='about'),
    url(r'^sign_in/$',views.sign_in, name='sign_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^logout/$', views.logout_view, name='logout'),


#only for authorized users
    url(r'^my_quotations/$',  views.user_quotations, name='user_quotations'),

    #books
    url(r'^books/$',  views.books, name='books'),
    url(r'^books/show/(?P<book_id>\w{0,5})/$',  views.books_show, name='books_show'),
    url(r'^books/borrow/(?P<book_id>\w{0,5})/$',  views.borrow_book, name='borrow_book'),
    url(r'^books/return/(?P<book_id>\w{0,5})/$',  views.return_book, name='return_book'),

    #authors
    url(r'^authors/$',  views.authors, name='authors'),
    url(r'^authors/show/(?P<author_id>\w{0,5})/$',  views.authors_show, name='authors_show'),

    #users
    url(r'^change_password/$',  views.change_password, name='change_password'),
    url(r'^users/$',  views.search_users, name='search_users'),
    url(r'^users/(?P<action>\d{1})/(?P<username>\w{0,30})/$',  views.user_connect, name='user_connect'),
    url(r'^users/(?P<username>\w{0,30})/$',  views.user, name='user'),
    url(r'^useredit/$', views.useredit, name='useredit'),

    #publishers
    url(r'^publishers/$',  views.publishers, name='publishers'),
    url(r'^publishers/show/(?P<publisher_id>\w{0,5})/$',  views.publishers_show, name='publishers_show'),

    #periods
    url(r'^periods/$', views.periods, name='periods'),
    url(r'^periods/show/(?P<period_id>\w{0,5})/$', views.periods_show, name='periods_show'),

    #CRUD
    url(r'^(?P<what>\w{1,10})/new/$', views.create_instance, name='new'),
    url(r'^(?P<what>\w{1,10})/edit/(?P<id_obj>\d{1,10})$',  views.edit_instance, name='edit'),
    url(r'^(?P<what>\w{1,10})/remove/(?P<id_obj>\d{1,10})$',  views.remove_instance, name='remove'),

    url(r'^admin/', include(admin.site.urls)),

    #facebook
    # url(r'^fandjango/', include('fandjango.urls')),
    url(r'^fb/(?P<what>\w{1,10})$',  views.fb_sign_up, name='fb_sign_up'),
]
# )

#static files
# urlpatterns += patterns('django.contrib.staticfiles.views',
#         url(r'^static/(?P<path>.*)$', 'serve'),
#     )
