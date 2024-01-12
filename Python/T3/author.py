class Libaray:
    def __init__(self):
        self.author=""
        self.publisher=""
        self.name=""

    def add_book(self):
        self.author=input("Enter Author Name : ")
        self.publisher=input("Enter Publisher Name : ")
        self.name=input("Enter Name : ")

    def display(self):
        print("Book Name : ",self.name)
        print("Book Author Name : ",self.author)
        print("Book Publisher Name : ",self.publisher)

my_book=[]
ch='y'
while ch=='y':
    print("1. Add Book ")
    print("2. Display Book ")
    choice=int(input("Enter Choice : "))
    if choice==1:
        book=Libaray()
        book.add_book()
        my_book.append(book)
    elif choice==2:
        for i in my_book:
            i.display()
    else:
        print("Invalid Choice")
        break
        
        
