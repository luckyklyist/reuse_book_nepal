from django.urls import path
from .views import index,book_detail,sell_book,user_profile,create_user_profile,edit_ads,delete_ads,buy_books,search_books,reply_post
urlpatterns = [
    path('',index,name="home"),
    path('buybooks',buy_books,name="buybooks"),
    path('book/<str:slug>',book_detail,name="book"),
    path('reply_que_book/<str:slug>',reply_post,name="reply"),
    path('sellbook',sell_book,name="sellbook"),
    path('profile/<str:slug>',user_profile,name="profile"),
    path('profileform',create_user_profile,name="profileform"),
    path('edit_ads/<str:slug>',edit_ads,name="editads"),
    path('edit_ads/<str:slug>',edit_ads,name="editads"),
    path('del_ads/<str:slug>',delete_ads,name="delads"),
    path('search',search_books,name="searchbooks"),
    
]

