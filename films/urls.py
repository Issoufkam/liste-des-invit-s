from django.urls import path
from .views import SearchResultsView, HomePageView
urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
    #path("projects/", views.projects, name="projects"),
    #path("contact/", views.contact, name="contact"),
]