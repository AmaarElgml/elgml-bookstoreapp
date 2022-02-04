from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from storeapp.models import Book, News, Author, AppAdmin
from storeapp.serializer import BookSerializer, AuthorSerializer, NewsSerializer, AppAdminSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    # def create(self, request, *arg, **kwarg):
    #     authors_list = []
    #     for row in request.data:
    #         author = Author.objects.create(name=row["name"], image=row["image"], booksNum=row["booksNum"])
    #         author.save()
    #         serializer = AuthorSerializer(author)
    #         authors_list.append(serializer)
    #     return Response(authors_list)


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    # def create(self, request, *arg, **kwarg):
    #     books_list = []
    #     for row in request.data:
    #         book = Book.objects.create(name=row["name"], author=row["author"], background=row["background"],
    #                                    price=row["price"], poster=row["poster"], category=row["category"])
    #         book.save()
    #         serializer = BookSerializer(book)
    #         books_list.append(serializer)
    #     return Response(books_list)


class NewsViewSet(viewsets.ModelViewSet):
    model = News
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    # def create(self, request, *arg, **kwarg):
    #     news_list = []
    #     for row in request.data:
    #         new = News.objects.create(title=row["title"], body=row["body"], date=row["date"], type=row["type"])
    #         new.save()
    #         serializer = NewsSerializer(new)
    #         news_list.append(serializer)
    #     return Response(news_list)


class AppAdminViewSet(viewsets.ModelViewSet):
    model = AppAdmin
    serializer_class = AppAdminSerializer
    queryset = AppAdmin.objects.all()

    # def create(self, request, *arg, **kwarg):
    #     appadmins_list = []
    #     for row in request.data:
    #         appadmins = AppAdmin.objects.create(name=row["name"], image=row["image"], role=row["role"],
    #                                             email=row["email"],
    #                                             password=row["password"], phoneNumber=row["phoneNumber"],
    #                                             online=row["online"])
    #         appadmins.save()
    #         serializer = AppAdminSerializer(appadmins)
    #         appadmins_list.append(serializer)
    #     return Response(appadmins_list)
