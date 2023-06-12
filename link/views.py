from django.shortcuts import render
from .models import Link
from .serializers import LinkSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class LinkView(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer



def data_grid_view(request):
    links = Link.objects.all()
    per_page = 10
    paginator = Paginator(links, per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    
    context = {
        'links': page,
        'currentPage': page.number,
        'totalPages': paginator.num_pages,
    }
    return render(request, 'data_grid.html', context)
