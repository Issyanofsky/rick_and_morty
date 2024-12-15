import requests
import csv

API_URL = "https://rickandmortyapi.com/api"
search_list = []

#define and check URL
def fetch_data(endpoint):
    url = f"{API_URL}/{endpoint}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data from {url}")
        return None

# rerive data origin = Earth, status = alive, species = Human
def retrive_data():
    data = fetch_data('character/?status=Alive&species=Human')
    if data:
        return data['results']
    return []

# export to scv file
def export_to_csv():
    try:
        with open('characters.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Location', 'Image Link']) # Titles

            if search_list:
                for character in search_list:
                    name = character['Name']
                    location = character['Location']
                    image_link = character['Image link']

                    # Write each character's data to the CSV
                    writer.writerow([name, location, image_link])

        print("Data has been written to characters.csv.")
    except PermissionError:
        # Handle file being open or locked
        print("Error: The file is currently open or locked by another process. Please close it and try again.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

def main():
    print("ISSY")

    srearch_data = retrive_data()

    for s_data in srearch_data:
        origin_name = s_data['origin']['name']
        if origin_name and origin_name.startswith('Earth'):
            data_list = {
                'Name': s_data['name'],
                'Location': s_data['location']['name'],
                'Image link': s_data['url']
            }
            search_list.append(data_list)
    export_to_csv()

if __name__ == "__main__":
    main()