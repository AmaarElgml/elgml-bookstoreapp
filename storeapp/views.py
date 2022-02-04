from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from storeapp.models import Book, News, Author, AppAdmin
from storeapp.serializer import BookSerializer, AuthorSerializer, NewsSerializer, AppAdminSerializer


class AuthorListGenerics(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorPKGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksListGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class BooksPKGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class NewsViewSet(viewsets.ModelViewSet):
    model = News
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def create(self, request, *arg, **kwarg):
        # batch_size = 500
        # for row in request.data:
        #     news = News()
        #     news.title = row["title"]
        #     news.body = row["title"]
        #     news.date = row["title"]
        #     news.type = row["title"]
        # News.objects.bulk_create(news_list, batch_size)

        news_list = []
        for row in request.data:
            new = News.objects.create(title=row["title"], body=row["body"], date=row["date"], type=row["type"])
            new.save()
            serializer = NewsSerializer(new)
            news_list.append(serializer)
        return Response(news_list)

    # def get_serializer(self, *args, **kwargs):
    #     if 'data' in kwargs:
    #         data = kwargs['data']
    #
    #         if isinstance(data, list):
    #             kwargs['many'] = True
    #
    #     return super().get_serializer(*args, **kwargs)


# class NewsListGenerics(generics.ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#
#
# class NewsPKGenerics(generics.RetrieveUpdateDestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


class AppAdminListGenerics(generics.ListCreateAPIView):
    queryset = AppAdmin.objects.all()
    serializer_class = AppAdminSerializer


class AppAdminPKGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppAdmin.objects.all()
    serializer_class = AppAdminSerializer
