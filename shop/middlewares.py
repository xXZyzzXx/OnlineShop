from .models import Category


def shop_context_processor(request):
    context = {'categs': Category.objects.all(), 'all': ''}
    if 'page' in request.GET:
        page = request.GET['page']
        if page != '1':
            if context['all']:
                context['all'] += '&page=' + page
            else:
                context['all'] = '?page=' + page
    return context
