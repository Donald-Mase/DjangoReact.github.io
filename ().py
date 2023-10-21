# coding: utf-8
from books.models import Books
obj =Books
obj.name = "ert"
obj.author = "Bob"
obj.description = "Braph"
obj.save()
get_ipython().run_line_magic('reset', '')
from books.models import Books
obj = Books
obj.name = "ert"
obj.author = "Bob"
obj.description = "Braph"
obj.save()
test.name
test = Books.objects.get(id=1)
test.name
obj =Books
obj.id =2
obj.name = "ert2"
obj.author = "Bob2"
obj.description = "Braphy"
obj.save()
obj.save()
