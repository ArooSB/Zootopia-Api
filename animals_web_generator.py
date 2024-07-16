import data_fetcher


def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"].upper()}</div>\n'

    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'<div class="card__text"><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</div>\n'

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'<div class="card__text"><strong>Location:</strong> {", ".join(animal_obj["locations"])}</div>\n'

    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'<div class="card__text"><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</div>\n'

    if "description" in animal_obj:
        output += f'<div class="card__text">{animal_obj["description"]}</div>\n'

    if "average_lifespan" in animal_obj:
        output += f'<div class="card__text"><strong>Average Lifespan:</strong> {animal_obj["average_lifespan"]} years</div>\n'

    if "habitat" in animal_obj:
        output += f'<div class="card__text"><strong>Habitat:</strong> {animal_obj["habitat"]}</div>\n'

    output += "</li>\n"
    return output


def generate_html(data):
    if not data:
        return "<h2>The animal you searched for does not exist.</h2>\n"

    output = ""
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    print(f"Generated HTML for animals: {output}")
    return output


def generate_full_html(output_path, animals_data):
    with open(output_path, "r") as file:
        template = file.read()
        print(f"Template content before replacement:\n{template}")

    animal_details = generate_html(animals_data)
    print(f"Animal details to be replaced:\n{animal_details}")

    html_content = template.replace("__REPLACE_ANIMALS_INFO__", animal_details)
    print(f"Template content after replacement:\n{html_content}")

    return html_content


def overwrite_html(output_path, html_content):
    with open(output_path, "w") as file:
        file.write(html_content)
    print(f"Written HTML content to {output_path}")


def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    if animals_data:
        html_content = generate_full_html("animals.html", animals_data)
        overwrite_html("animals.html", html_content)
        print("Website was successfully generated to the file animals.html.")
    else:
        print(f"No data fetched for {animal_name}. Exiting without generating website.")


if __name__ == "__main__":
    main()
