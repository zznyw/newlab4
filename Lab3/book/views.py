from django.shortcuts import render_to_response
from book.models import Book, Author
#from django.http import HttpResponse

def Author_search(request):
    
    if 'author_name' in request.GET:
        search_name = request.GET['author_name']
        if not search_name:
             return render_to_response('search_author.html',{'error': 'Please input name!'})
        else:
            for temp_author in Author.objects.all():
                if cmp(search_name,temp_author.Name)==0:
                    books=[]
                    for temp_book in Book.objects.all():
                        if cmp(temp_author,temp_book.AuthorID)==0:
                            books.append(temp_book)
                    return render_to_response('search_author.html', {'Author':search_name, 'right':'Find the author', 'count':len(books), 'books': books})
                    
                else:
                    continue
            return render_to_response('search_author.html',{'error': 'NO this author!', 'Author':search_name})
    return render_to_response('search_author.html')       
            
def book_info(request):
    temp_ISBN = request.GET['ISBN']
    book_info = Book.objects.get(ISBN=temp_ISBN)
    Author_info = book_info.AuthorID
    return render_to_response('book_info.html', {'book_info': book_info, 'Author_info': Author_info})

def delete(request):
    del_ISBN = request.GET['ISBN']
#    temp_AuthorID = request.GET['AuthorID']
    del_book = Book.objects.get(ISBN=del_ISBN)
    temp_AuthorID=del_book.AuthorID
    name = del_book.AuthorID.Name
    del_book.delete()
    books=[]
    for temp_book in Book.objects.all():
        if cmp(temp_AuthorID,temp_book.AuthorID)==0:
            books.append(temp_book)
    return render_to_response('search_author.html', {'Author':name, 'right':'Find the author', 'count':len(books), 'books': books})   
def addbook(request):
	if 'addsub' in request.GET:
		temp_add = request.GET['addsub']
	if 'again' in request.GET:
		again = request.GET['again']
	if 'add_Author' in request.GET:
		add_Author = request.GET['add_Author']
	if temp_add:
		add_ISBN = request.GET['ISBN']
		add_Title = request.GET['Title']
		add_Name = request.GET['Author_name']
		add_Publisher = request.GET['Publisher']
		add_PublishDate = request.GET['PublishDate']
		add_Price = request.GET['Price']
		if not add_ISBN:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_book':'书籍信息：'})
		if not add_Title:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_book':'书籍信息：'})
		if not add_Name:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_book':'书籍信息：'})
		if not add_Publisher:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_book':'书籍信息：'})
		if not add_PublishDate:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_book':'书籍信息：'})
		if not add_Price:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_book':'书籍信息：'})
		for temp_author in Author.objects.all():
			if(add_Name,temp_author.Name)==0:
				p = Book( ISBN = add_ISBN, Title = add_Title, AuthorID = temp_author, Publisher = add_Publisher, PublishDate = add_PublishDate, Price = add_Price)
				p.save()
				return render_to_response('addbook.html',{'ret': '已添加书籍!', 'add_book':'书籍信息：'})
		return render_to_response('addbook.html',{'ret':'No this author', 'add_author':'作者信息：'})
		
	if add_Author:
		add_AuthorName = request.GET['Name']
		add_AuthorID = request.GET['AuthorID']
		add_Age = request.GET['Age']
		add_Country = request.GET['Country']
		if not add_AuthorName:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_author':'作者信息：'})
		if not add_AuthorID:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_author':'作者信息：'})
		if not add_Age:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_author':'作者信息：'})
		if not add_Country:
			return render_to_response('addbook.html',{'ret': '请输入完整信息!', 'add_author':'作者信息：'})
		k = Author(AuthorID = add_AuthorID, Name = add_Name, Age = add_Age, Country = add_Country)
		k.save()
		return render_to_response('addbook.html',{'ret': '已添加作者!', 'add_book':'书籍信息：'})
	if again:
		return render_to_response('addbook.html',{'add_book':'书籍信息：'})
	return render_to_response('addbook.html',{'add_book':'书籍信息：'})