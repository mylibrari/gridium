import requests
from bs4 import BeautifulSoup

base_url = "https://www.tide-forecast.com"
locations_list = ["Half-Moon-Bay-California", 
                  "Huntington-Beach", 
                  "Providence-Rhode-Island", 
                  "Wrightsville-Beach-North-Carolina"]

result = {}

for location in locations_list:
    url = f"{base_url}/locations/{location}/tides/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tides_table = soup.find_all("table", class_="tide-day-tides")
    tides_data = tides_table[0]
    tides_row = tides_data.find_all("tr")
    result[location] = {}
    for row in tides_row:
        if row.find("td", string="Low Tide"):
            low_tide_data = row.find_all("b")
            time = low_tide_data[0].text
            if "AM" in time:
                result[location]["sunrise_time"] = time
            else:
                result[location]["sunset_time"] = time
            tide_height = low_tide_data[1].text
            result[location]["height"] = tide_height

print(result)
