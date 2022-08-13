from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Invite

# Create your views here.
#def home(request):
   # return render(request, "index.html")


class HomePageView(TemplateView):
    template_name = 'index.html'

class SearchResultsView(ListView):
    model = Invite
    template_name = 'results.html'
    context_object_name = "invites"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        invites = Invite.objects.filter(
            Q(nom__icontains=query) | Q(prenoms__icontains=query) | Q(table__icontains=query) | Q(numero__icontains=query)
        )
        return invites