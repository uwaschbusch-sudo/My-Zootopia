# Bonus - Improved HTML & CSS

import json

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """Lädt eine JSON-Datei und gibt deren Inhalt zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_text_file(file_path):
    """Liest eine Textdatei und gibt ihren Inhalt als String zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_text_file(file_path, content):
    """Schreibt den übergebenen String in eine Textdatei."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def serialize_animal(animal):
    """Erzeugt für ein Tier eine HTML-Karte mit Titel und Detailliste. """
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__list">\n'
    if "diet" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Diet:</strong> {characteristics['diet']}</li>\n"
    if locations:
        output += f"      <li class=\"card__list-item\"><strong>Location:</strong> {locations[0]}</li>\n"
    if "type" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Type:</strong> {characteristics['type']}</li>\n"
    if "lifespan" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Lifespan:</strong> {characteristics['lifespan']}</li>\n"
    if "color" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Color:</strong> {characteristics['color']}</li>\n"
    if "skin_type" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Skin Type:</strong> {characteristics['skin_type']}</li>\n"
    output += "    </ul>\n"
    output += "  </div>\n"

    output += "</li>\n"
    return output


def build_animals_output(animals_data):
    """Erzeugt einen HTML-String mit einer Karte pro Tier."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    """Füllt das HTML-Template mit den Tierdaten und schreibt animals.html."""
    animals_data = load_data("animals_data.json")
    template = read_text_file("animals_template.html")

    animals_output = build_animals_output(animals_data)
    html_content = template.replace(PLACEHOLDER, animals_output)

    write_text_file("animals.html", html_content)


if __name__ == "__main__":
    main()