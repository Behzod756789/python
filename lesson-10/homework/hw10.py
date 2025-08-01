from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} - {self.description} (Due: {self.due_date.date()}) [{status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def list_incomplete(self):
        return [str(task) for task in self.tasks if not task.completed]


def todo_cli():
    todo = ToDoList()
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. List All Tasks\n4. List Incomplete Tasks\n5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(Task(title, description, due_date))
        elif choice == '2':
            title = input("Task Title to complete: ")
            if not todo.complete_task(title):
                print("Task not found.")
        elif choice == '3':
            for task in todo.list_tasks():
                print(task)
        elif choice == '4':
            for task in todo.list_incomplete():
                print(task)
        elif choice == '5':
            break

# Homework 2: Simple Blog System
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.created_at.strftime('%Y-%m-%d %H:%M')})\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return [str(post) for post in self.posts]

    def posts_by_author(self, author):
        return [str(p) for p in self.posts if p.author == author]

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content

    def latest_posts(self, count=3):
        return [str(p) for p in sorted(self.posts, key=lambda x: x.created_at, reverse=True)[:count]]


def blog_cli():
    blog = Blog()
    while True:
        print("\n1. Add Post\n2. List All Posts\n3. Show by Author\n4. Delete Post\n5. Edit Post\n6. Latest Posts\n7. Exit")
        choice = input("Choose: ")
        if choice == '1':
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == '2':
            for post in blog.list_posts():
                print(post)
        elif choice == '3':
            author = input("Author: ")
            for post in blog.posts_by_author(author):
                print(post)
        elif choice == '4':
            title = input("Post title to delete: ")
            blog.delete_post(title)
        elif choice == '5':
            title = input("Post title to edit: ")
            new_content = input("New content: ")
            blog.edit_post(title, new_content)
        elif choice == '6':
            for post in blog.latest_posts():
                print(post)
        elif choice == '7':
            break

# Homework 3: Simple Banking System
class Account:
    def __init__(self, acc_no, holder_name, balance=0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"{self.acc_no} - {self.holder_name}: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_no] = account

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)


def bank_cli():
    bank = Bank()
    while True:
        print("\n1. Add Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transfer\n6. Exit")
        choice = input("Choose: ")
        if choice == '1':
            acc_no = input("Account Number: ")
            name = input("Account Holder: ")
            bank.add_account(Account(acc_no, name))
        elif choice == '2':
            acc_no = input("Account Number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_no)
            if acc:
                acc.deposit(amount)
        elif choice == '3':
            acc_no = input("Account Number: ")
            amount = float(input("Amount: "))
            acc = bank.get_account(acc_no)
            if acc:
                if not acc.withdraw(amount):
                    print("Insufficient funds.")
        elif choice == '4':
            acc_no = input("Account Number: ")
            acc = bank.get_account(acc_no)
            if acc:
                print(acc)
        elif choice == '5':
            from_acc = bank.get_account(input("From Account: "))
            to_acc = bank.get_account(input("To Account: "))
            amount = float(input("Amount: "))
            if from_acc and to_acc:
                if not from_acc.transfer(amount, to_acc):
                    print("Transfer failed. Not enough balance.")
        elif choice == '6':
            break

