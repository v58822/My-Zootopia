import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")


def print_animals_overview(animals_data):
    """Generates an HTML block for each animal as <li> with styled title and text."""
    output = ""
    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        type_ = characteristics.get("type")
        location = animal.get("locations", [None])[0]

        output += '<li class="cards__item">\n'
        if name:
            output += f'  <div class="card__title">{name}</div>\n'
        output += '  <p class="card__text">\n'
        if diet:
            output += f'    <strong>Diet:</strong> {diet}<br/>\n'
        if location:
            output += f'    <strong>Location:</strong> {location}<br/>\n'
        if type_:
            output += f'    <strong>Type:</strong> {type_}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'
    return output


if __name__ == "__main__":
  animals_data = load_data("animals_data.json")
  animals_text = print_animals_overview(animals_data)

  with open("animals_template.html", "r") as f:
    template_html = f.read()

  final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_text)

  with open("animals.html", "w") as f:
    f.write(final_html)