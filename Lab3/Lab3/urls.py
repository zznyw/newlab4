from django.conf.urls import patterns, include, url
from django.contrib import admin
#from book.views import hello
#admin.autodiscover()
from book import views
#from book.views import current_datetime
urlpatterns = patterns('',
                        ('^AuthorSearch/$',views.Author_search),
                        ('^book_info/$',views.book_info),
                        ('^delete/$',views.delete),
						('^addbook/$',views.addbook),
					#	('^delete/$',views.delete),

    url(r'^admin/', include(admin.site.urls)),
)
