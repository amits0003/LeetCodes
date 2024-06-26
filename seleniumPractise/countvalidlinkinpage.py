import requests
from bs4 import BeautifulSoup


def check_link(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False


def main():
    # URL of the webpage you want to check
    url = 'https://www.google.com/'  # Replace with your target URL

    # Send a request to fetch the content of the page
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links in the page
    links = soup.find_all('a')
    total_links = len(links)
    valid_links = 0
    invalid_links = 0

    # Check each link
    for link in links:
        href = link.get('href')
        if href:
            if href.startswith('http') or href.startswith('https'):
                if check_link(href):
                    valid_links += 1
                else:
                    invalid_links += 1

    # Print the results
    print(f"Total Links: {total_links}")
    print(f"Valid Links: {valid_links}")
    print(f"Invalid Links: {invalid_links}")


if __name__ == '__main__':
    main()
