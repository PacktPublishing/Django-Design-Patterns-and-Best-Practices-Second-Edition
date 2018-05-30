from django.urls import path
from . import views

app_name = 'formschapter'

urlpatterns = [
    path(r'forms/',
         views.FormView.as_view(),
         name="forms"),

    path('cbv-form/',
         views.ClassBasedFormView.as_view(),
         name="cbv-form"),

    path('gfv-form/',
         views.GenericFormView.as_view(),
         name="gfv-form"),


    path('newsletter-form/',
         views.NewsletterView.as_view(),
         name="newsletter-form"),


    path('impdates/<int:pk>/',
         views.ImpDateDetail.as_view(),
         name="impdate_detail"),

    path('impdates/create/',
         views.ImpDateCreate.as_view(),
         name="impdate_create"),

    path('impdates/<int:pk>/edit/',
         views.ImpDateUpdate.as_view(),
         name="impdate_update"),

    path('impdates/<int:pk>/delete/',
         views.ImpDateDelete.as_view(),
         name="impdate_delete"),

    path('impdates/',
         views.ImpDateList.as_view(),
         name="impdate_list"),
]
