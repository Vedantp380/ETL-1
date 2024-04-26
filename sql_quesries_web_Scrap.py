import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.yellowpages.com/bartlesville-ok/restaurants'
response = requests.get(url, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the div with class 'search-results organic'
    search_results_div = soup.find('div', class_='search-results organic')
    if search_results_div:
        data = []
        # Find all the divs with class 'v-card'
        restaurant_divs = search_results_div.find_all('div', class_='v-card')
        for restaurant_div in restaurant_divs:
            # Find the anchor tag with class 'business-name' inside each restaurant div
            business_name_anchor = restaurant_div.find('a', class_='business-name')
            if business_name_anchor:
                restaurant_name = business_name_anchor.text.strip()
                # Find the div with class 'adr' for the address
                address_div = restaurant_div.find('div', class_='adr')
                if address_div:
                    # Extract the street address and locality
                    street_address = address_div.find('div', class_='street-address').text.strip()
                    locality = address_div.find('div', class_='locality').text.strip()
                    # Find the phone number
                    phone_number = restaurant_div.find('div', class_='phones').text.strip()
                    data.append({'Restaurant Name': restaurant_name, 'Street Address': street_address, 'Locality': locality, 'Phone Number': phone_number})

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(data)
        print(df)
    else:
        print('Div with class "search-results organic" not found.')
else:
    print('Failed to fetch the webpage.')
