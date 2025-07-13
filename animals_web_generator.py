import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")

def print_animals_overview(animals_data):
    """Prints name, diet, first location, and type for each animal (if available)."""
    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        type_ = characteristics.get("type")
        location = animal.get("locations", [None])[0]

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if location:
            print(f"Location: {location}")
        if type_:
            print(f"Type: {type_}")
        print()


print_animals_overview(animals_data)