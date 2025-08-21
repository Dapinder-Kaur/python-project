from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://jsonplaceholder.typicode.com/"
ALL_JSON = "/posts"

printer = PrettyPrinter()

def get_data():
    data = get(BASE_URL + ALL_JSON).json()
    return data

def get_post_by_id(post_id):
    data = get_data()
    number = data[post_id]
    id = number['id']
    title = number['title']
    return id, title

def print_post(idd):
    id, title = get_post_by_id(idd)
    print("Post ID: " + str(id))
    print("Title: " + title)

if __name__ == "__main__":
    print_post(5)



