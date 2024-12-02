from Book import Book

def sortbyYear():
    for position in range (len(books)-1,-1,-1):
        maxindex=position
        for j in range(position):
            if books[maxindex].getYear()<books[j].getYear():
                maxindex=j
        temp=books[maxindex]
        books[maxindex]=books[position]
        books[position]=temp
        

books=[]
for i in range(5):
    bookno=input("Enter a book number: ")
    title=input("title: ")
    year=int(input("Year: "))
    book= Book(bookno, title, year)

    books.append(book)

SortByYear(books)
print("The book list sorted by year: ")
for book in books:
    print(book.__str__())
    