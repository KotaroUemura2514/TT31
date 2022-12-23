from django.shortcuts import render, redirect
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView,)
from.models import Book, Like
from django.urls import reverse,reverse_lazy


class ListBookView(ListView):
    object_list = Book.objects.order_by('id').reverse()
    template_name='book/Diary.html'
    model=Book 
    
    # object_list = Book.objects.order_by('id')
    # return render(request, 'book/Diary.html', {'object_list':object_list})


class DetailBookView(DetailView):
    template_name='book/book_detail.html'
    model=Book

class Toukou(CreateView):
    template_name = 'book/toukou.html'
    model = Book
    fields = ('title','text')
    success_url = reverse_lazy('list-book')

class Delete(DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')


class Update(UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ('title', 'text')
    success_url = reverse_lazy('list-book')

    
# def index_view(request):
#     object_list = Book.objects.order_by('id')
#     return render(request, 'book/Diary.html', {'object_list':object_list})

def like_post(request):
    user = request.user
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book_obj = Book.objects.get(id=book_id)

        if user in book_obj.liked.all():
            book_obj.liked.remove(user)
        else:
            book_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, book_id=book_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('posts:post-list')

def posts_view(request):
    qs = Book.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user': user,
    }

    return render(request, 'book/Dairy.html', context)