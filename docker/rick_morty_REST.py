import requests
from flask import Flask, jsonify,  render_template_string
import json


app = Flask(__name__)

API_URL = "https://rickandmortyapi.com/api"

# Function to generate an HTML table to display character data

def generate_html(characters):
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rick and Morty Characters</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f4f4f4;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }
            th, td {
                padding: 8px 12px;
                text-align: left;
                border: 1px solid #ddd;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            img {
                max-width: 100px;
                height: auto;
            }
        </style>
    </head>
    <body>
        <h1>Rick and Morty Characters</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Origin</th>
                    <th>Image</th>
                </tr>
            </thead>
            <tbody>
    '''
    # Add each character to the HTML table
    for character in characters:
        html_content += f'''
               <tr>
                   <td>{character['Name']}</td>
                   <td>{character['Location']}</td>
                   <td><img src="{character['Image link']}" alt="{character['Name']}"></td>
               </tr>
           '''

    # Closing the table and HTML
    html_content += '''
               </tbody>
           </table>
       </body>
       </html>
       '''

    return html_content


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
    search_list = []
    data = fetch_data('character/?status=Alive&species=Human')

    for character in data['results']:
        origin_name = character['origin']['name']
        if origin_name and origin_name.startswith('Earth'):
            data_list = {
                'Name': character['name'],
                'Location': character['origin']['name'],
                'Image link': character['image']
            }
            search_list.append(data_list)

    if search_list:
        return search_list
    return []

# get data fron the api

@app.route('/characters', methods=['GET'])
def get_characters():
    # search_list = []
    search_data = retrive_data()

    return jsonify(search_data)


# /healthcheck endpoint to check if the service is up
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"}), 200

@app.route('/htmlversion', methods=['GET'])
def htmlversion():
    # Main script to fetch the data and display it in HTML

    characters = retrive_data()

    if characters:
        # Generate HTML content
        html_content = generate_html(characters)

        # Return HTML content as part of the API response
        return render_template_string(html_content)  # Use Flask's render_template_string to return the HTML directly
    else:
        # If no data is available, return an error message in HTML
        return render_template_string("""
               <html>
                   <body>
                       <h1>No character data available.</h1>
                   </body>
               </html>
           """), 404  # Return a 404 if no characters are available

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)