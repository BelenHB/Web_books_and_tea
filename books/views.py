from django.shortcuts import render, redirect

from .forms import BookForm, BookSearchForm
from .models import Book

# Create your views here.

# CRUD para models BOOK (LIBROS)

# Vista LIBROS (listado)
def book_list(request):
  books = Book.objects.all()
  
  return render(request, 'books/book_list.html', {'books':books})


# Vista CREACIÓN DE NUEVO LIBRO
def book_create(request):
  '''Permite ingresar objetos de clase Book (Libro) en la BD.
  Solicita título, autor y ISBN de la publicación'''
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      book = Book(title=data['title'], author=data['author'], isbn=data['isbn'])
      book.save()
      form = BookForm()
      print(book)
      return redirect('book_list')
  
  else:
    form = BookForm()
  
  return render(request, 'books/book_create.html', {'form':form})


# Vista EDITAR LIBRO
def book_update(request, id):
  '''Permite modificar objetos de clase Book (Libro) en la BD.
  Solicita título, autor y ISBN de la publicación'''
  book = Book.objects.get(id=id)
  
  if request.method == 'POST':
    form = BookForm(request.POST)
    
    if form.is_valid():
      data = form.cleaned_data
      book.title = data['title']
      book.author = data['author']
      book.isbn = data['isbn']
      book.save()
      form = BookForm()
      return redirect('book_list')
  else:
    form = BookForm(initial={'title': book.title,
                             'author': book.author,
                             'isbn': book.isbn})
    
  return render(request, 'books/book_update.html', {'form':form, 'book':book})


# Vista BORRAR LIBRO
def book_delete(request, id):
  '''Permite eliminar objetos de clase Book (Libro) en la BD.'''
  book = Book.objects.get(id=id)
  book.delete()
  
  return redirect('book_list')


# Vista de BUSCAR LIBRO
# Para buscar libros por palabra
def book_search(request):
  '''Realiza una búsqueda en la BD por palabra que se encuentre en el título
  del libro o en el autor'''
  books = []  #aquí se guardarán los resultados de la búsqueda
  data = request.GET.get('find_book', None)
  
  if data is not None:
    books = Book.objects.filter(title__icontains=data)| Book.objects.filter(author__icontains=data)
  searcher = BookSearchForm()

  return render(request, 'books/book_search.html', {'searcher':searcher, 'books':books})
 
 

