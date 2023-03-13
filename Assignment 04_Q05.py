file=open("books.txt","r")

bookList=file.readlines()

for books in bookList:
    books=books.strip()
    book,author=books.split(",")
    print(author + " , " + "['", book, "']" )
