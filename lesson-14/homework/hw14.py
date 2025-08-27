import json

with open("students.json") as f:
    students = json.load(f)

for student in students["students"]:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

{
    "students": [
        {"name": "Ali", "age": 20, "grade": "A"},
        {"name": "Laylo", "age": 22, "grade": "B"}
    ]
}
import requests

API_KEY = "your_api_key_here"  # register & get your free API key
city = "Tashkent"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error fetching data:", data)



import json

def load_books():
    try:
        with open("books.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"books": []}

def save_books(data):
    with open("books.json", "w") as f:
        json.dump(data, f, indent=4)

def add_book(title, author):
    books = load_books()
    books["books"].append({"title": title, "author": author})
    save_books(books)

def update_book(old_title, new_title, new_author):
    books = load_books()
    for book in books["books"]:
        if book["title"] == old_title:
            book["title"] = new_title
            book["author"] = new_author
    save_books(books)

def delete_book(title):
    books = load_books()
    books["books"] = [b for b in books["books"] if b["title"] != title]
    save_books(books)

add_book("1984", "George Orwell")
update_book("1984", "Animal Farm", "George Orwell")
delete_book("Animal Farm")


{
    "books": [
        {"title": "Python Basics", "author": "John Doe"}
    ]
}


import requests
import random

API_KEY = "your_omdb_api_key_here"

def get_movies_by_genre(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"
    response = requests.get(url).json()
    return response.get("Search", [])

genre = input("Enter a movie genre (e.g. Action, Comedy, Drama): ")
movies = get_movies_by_genre(genre)

if movies:
    movie = random.choice(movies)
    print(f"🎬 Recommended: {movie['Title']} ({movie['Year']})")
else:
    print("No movies found for this genre.")
