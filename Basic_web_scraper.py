import requests
from bs4 import BeautifulSoup

def web_scrape(url):
    # Sending a GET request to the website
    response=requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parsing the HTML content of the page where soup is a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the title of the page
        title = soup.title.string if soup.title else 'No title found'
        print(f"Title: {title}")

        # Printing the link of the page
        print(f"Link: {url}")

        # Printing the entire HTML content
        print(soup.prettify())

    else:
        print(f'Failed to retrieve the web page. Status code: {response.status_code}')
    
    # URL of the website to scrape
    #we can use any website ,here i used gfg for demonstration of code
    url = 'https://www.geeksforgeeks.org/' 
    
    web_scrape(url)
    

