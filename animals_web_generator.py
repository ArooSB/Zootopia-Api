import data_fetcher

def serialize_animal(animal_obj):
    """
    Serializes a single animal object into HTML format.

    Parameters
    ----------
    animal_obj : dict
        A dictionary containing details about an animal.

    Returns
    -------
    str
        An HTML string representing the animal's details in list item format.
    """
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"].upper()}</div>\n'

    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += (
            f'<div class="card__text"><strong>Diet:</strong> '
            f'{animal_obj["characteristics"]["diet"]}</div>\n'
        )

    if "locations" in animal_obj and animal_obj["locations"]:
        output += (
            f'<div class="card__text"><strong>Location:</strong> '
            f'{", ".join(animal_obj["locations"])}</div>\n'
        )

    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += (
            f'<div class="card__text"><strong>Type:</strong> '
            f'{animal_obj["characteristics"]["type"]}</div>\n'
        )

    if "description" in animal_obj:
        output += (
            f'<div class="card__text">{animal_obj["description"]}</div>\n'
        )

    if "average_lifespan" in animal_obj:
        output += (
            f'<div class="card__text"><strong>Average Lifespan:</strong> '
            f'{animal_obj["average_lifespan"]} years</div>\n'
        )

    if "habitat" in animal_obj:
        output += (
            f'<div class="card__text"><strong>Habitat:</strong> '
            f'{animal_obj["habitat"]}</div>\n'
        )

    output += "</li>\n"
    return output

def generate_html(data, animal_name):
    """
    Generates HTML content based on a list of animal data.

    Parameters
    ----------
    data : list
        A list of dictionaries, each representing an animal's details.
    animal_name : str
        The name of the animal being searched.

    Returns
    -------
    str
        An HTML string containing all animal details, or a message if no data
        is present.
    """
    if not data:
        return (
            f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>\n"
        )

    output = ""
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output

def generate_full_html(output_path, animals_data, animal_name):
    """
    Reads the HTML template and replaces the placeholder with serialized
    animal data.

    Parameters
    ----------
    output_path : str
        The path to the HTML template file.
    animals_data : list
        A list of dictionaries, each representing an animal's details.
    animal_name : str
        The name of the animal being searched.

    Returns
    -------
    str
        A complete HTML string with the template and animal data merged.
    """
    with open(output_path, "r") as file:
        template = file.read()

    animal_details = generate_html(animals_data, animal_name)
    html_content = template.replace("__REPLACE_ANIMALS_INFO__", animal_details)

    return html_content

def overwrite_html(output_path, html_content):
    """
    Overwrites the HTML template file with updated content.

    Parameters
    ----------
    output_path : str
        The path to the HTML template file to be overwritten.
    html_content : str
        The new HTML content to write into the template file.
    """
    with open(output_path, "w") as file:
        file.write(html_content)
    print(f"Written HTML content to {output_path}")

def main():
    """
    Main function to interact with the user, fetch animal data, and generate
    the website.
    """
    animal_name = input("Enter the name of an animal: ").strip()
    if not animal_name:
        print("Animal name cannot be empty. Exiting.")
        return

    animals_data = data_fetcher.fetch_data(animal_name)
    html_content = generate_full_html(
        "animals_template.html", animals_data, animal_name
    )
    overwrite_html("animals_template.html", html_content)
    print("Website was successfully generated in the file animals_template.html.")

if __name__ == "__main__":
    main()
