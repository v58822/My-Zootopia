import data_fetcher


def serialize_animal(animal):
    """Returns the HTML string for a single animal entry."""
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")
    location = animal.get("locations", [None])[0]

    output = '<li class="cards__item">\n'
    if name:
        output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    if diet:
        output += f"    <strong>Diet:</strong> {diet}<br/>\n"
    if location:
        output += f"    <strong>Location:</strong> {location}<br/>\n"
    if type_:
        output += f"    <strong>Type:</strong> {type_}<br/>\n"
    output += "  </p>\n"
    output += "</li>\n"
    return output


def print_animals_overview(animals_data):
    """Generates HTML list items for all animals using serialize_animal()."""
    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


if __name__ == "__main__":
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    if animals_data != []:
        animals_text = print_animals_overview(animals_data)
    else:
        animals_text = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    with open("animals_template.html", "r") as f:
        template_html = f.read()

    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    with open("animals.html", "w") as f:
        f.write(final_html)
