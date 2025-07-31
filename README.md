# My Zootopia

This project is a simple Python application that fetches animal data from an external API and generates a static HTML website to display the results. 
It serves as a practical example for working with APIs, handling JSON data, and generating web content using Python.

## Features
	-	Retrieves animal information using the API Ninjas animal API
	-	Dynamically generates an HTML page based on user input
	-	Displays data such as taxonomy, location, diet, and type
	-	Handles cases where the animal is not found

## Installation
	1.	Clone the repository:
git clone https://github.com/v58822/My-Zootopia.git
cd My-Zootopia

	2.	Install the required Python packages:
pip install -r 
requirements.txt

	3.	Set up your environment variables:
Create a .env file in the project root directory and add your API key:
API_KEY=your_api_key_here

## Usage

To run the project, execute the following command:

python animals_web_generator.py

You will be prompted to enter an animal name. 
The script will then fetch the data and generate an animals.html file with the results. 
If no matching animal is found, the page will display an appropriate message.

## Project Structure
	-	data_fetcher.py: Handles the API request and returns animal data
	-	animals_web_generator.py: Main script that generates the HTML output
	-	animals_template.html: HTML template file with a placeholder for dynamic content
	-	.env: Stores the API key (should not be committed)
	-	requirements.txt: List of required Python packages
