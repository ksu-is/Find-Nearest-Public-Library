import requests
from bs4 import BeautifulSoup

def get_nearest_library(zip_code):
    # Construct the request payload
    payload = {'zipCode': zip_code, 'miles': '10', 'searchType': 'zipcode'}
    
    # Send the request and get the response
    response = requests.post('https://pines.georgialibraries.org/pinesLocator/search.do', data=payload)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Parse the response HTML to get the name and address of the nearest library
    name = soup.find('div', {'class': 'name'}).text.strip()
    address = soup.find('div', {'class': 'address'}).text.strip()
    
    return name, address

def recommend_book(genre):
    # Get the top New York Times bestsellers list for the given genre
    url = f'https://www.nytimes.com/books/best-sellers/{genre}-paperback-books/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Parse the response HTML to get the title and author of the first book on the list
    title = soup.find('h3', {'class': 'css-5pe77f e1voiwgp0'}).text.strip()
    author = soup.find('p', {'class': 'css-hjukut e1wijjv30'}).text.strip()
    
    return title, author


# Welcome the user
print("Welcome to the book recommendation system!\n")

# Display the top 5 most common book genres
print("Here are the top 5 most common book genres:")
print("1. Fiction")
print("2. Nonfiction")
print("3. Mystery")
print("4. Romance")
print("5. Sci-Fi/Fantasy")

while True:
    # Get user input for genre
    genre_choice = input("\nEnter the number corresponding to the genre you are interested in (Or enter 'exit' to quit): ")
    
    if genre_choice == 'exit':
        break
    
    # Map genre_choice to the corresponding genre
    genre_map = {
        '1': 'fiction',
        '2': 'nonfiction',
        '3': 'mystery',
        '4': 'romance',
        '5': 'science-fiction-and-fantasy'
    }
    
    genre = genre_map.get(genre_choice)
    
    if genre is None:
        print("\nInvalid choice. Please choose a number between 1 and 5.")
        continue
    
    # Recommend a book from the top New York Times bestsellers list for the given genre
    try:
        title, author = recommend_book(genre)
        print(f"\nBased on the current top New York Times bestsellers in {genre.capitalize()}, we recommend '{title}' by {author}.")
        
        # Ask if the user wants to check the availability of the recommended book at the local library
        check_availability = input("Would you like to see if the book is available at the nearest library? (y/n) ").lower()
        
        if check_availability == 'y':
            # Get user input for zip code
            zip_code = input("What is your zip code? ")
            
            # Check if the recommended book is available at the nearest library
            name, address = get_nearest_library(zip_code)
            book_title = title.replace("'", "\\'")  # Escape single quotes in the book title for the URL
            search_url =
