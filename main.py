class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # 初始状态为可借

    def __str__(self):
        status = "可借" if self.available else "已借出"
        return f"《{self.title}》- {self.author}（ISBN：{self.isbn}）[{status}]"


class User:
    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.borrowed_books = []  # 存储已借书籍对象

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"用户：{self.name}（卡号：{self.card_id}），已借书籍：{borrowed_titles if borrowed_titles else '无'}"


class Library:
    def __init__(self):
        self.books = []  # 存储图书馆的书籍
        self.users = []  # 存储图书馆的用户

    # 添加书籍到图书馆
    def add_book(self, book):
        self.books.append(book)

    # 添加用户到图书馆
    def add_user(self, user):
        self.users.append(user)

    # 检查书籍是否可借
    def is_book_available(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.available
        return False  # 书籍不存在

    # 借书功能
    def borrow_book(self, user_card_id, book_isbn):
        # 找到用户
        user = next((u for u in self.users if u.card_id == user_card_id), None)
        if not user:
            return "用户不存在"
        
        # 找到书籍
        book = next((b for b in self.books if b.isbn == book_isbn), None)
        if not book:
            return "书籍不存在"
        
        # 检查是否可借
        if not book.available:
            return "书籍已借出"
        
        # 执行借书
        book.available = False
        user.borrowed_books.append(book)
        return f"成功借出《{book.title}》给用户{user.name}"

    # 还书功能
    def return_book(self, user_card_id, book_isbn):
        # 找到用户
        user = next((u for u in self.users if u.card_id == user_card_id), None)
        if not user:
            return "用户不存在"
        
        # 找到用户已借的该书籍
        book = next((b for b in user.borrowed_books if b.isbn == book_isbn), None)
        if not book:
            return "用户未借此书"
        
        # 执行还书
        book.available = True
        user.borrowed_books.remove(book)
        return f"用户{user.name}成功归还《{book.title}》"# 在这里编写代码
