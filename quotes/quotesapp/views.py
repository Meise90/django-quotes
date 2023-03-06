from django.shortcuts import render, redirect
from quotesapp.models import Quote

# Create your views here.

def quote_create_view(request):

    if request.method == "GET":
        return render(
            request,
            'quotesapp/create_quote.html'
        )

    if request.method == "POST":

        quote = request.POST.get('quote')

        if quote:
            Quote.objects.create(content=quote)

        return redirect('quotesapp:quote-list-view')


def quote_list_view(request):

    quotes = Quote.objects.all()

    return render(
        request,
        'quotesapp/quotes_list.html',
        context={
            'quotes': quotes,
        }
    )

def quote_detail_view(request, quote_id):

    quote = Quote.objects.get(id=quote_id)

    return render(
        request,
        'quotesapp/quote_view.html',
        context={
            'quote': quote,
        }
    )

def quote_update_view(request, quote_id):

    quote = Quote.objects.get(id=quote_id)

    if request.method == "GET":
        return render(
            request,
            'quotesapp/update_quote.html',
            context={
                'quote': quote
            }
        )

    if request.method == "POST":

        new_quote = request.POST.get('quote')

        if new_quote:
            quote.content = new_quote
            quote.save()

        return redirect('quotesapp:quote-list-view')


def quote_delete_view(request, quote_id):

    quote = Quote.objects.get(id=quote_id)

    if request.method == "GET":
        return render(
            request,
            'quotesapp/delete_quote.html',
            context={
                'quote': quote,
            }
        )

    if request.method == "POST":

        quote.delete()

        return redirect('quotesapp:quote-list-view')