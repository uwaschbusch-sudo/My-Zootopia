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
    """Erzeugt den Text für ein Tier (Name, Diet, erste Location, Type).

    Felder, die nicht vorhanden sind, werden übersprungen.
    """
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    output = ""
    if "name" in animal:
        output += f"Name: {animal['name']}\n"
    if "diet" in characteristics:
        output += f"Diet: {characteristics['diet']}\n"
    if locations:
        output += f"Location: {locations[0]}\n"
    if "type" in characteristics:
        output += f"Type: {characteristics['type']}\n"
    return output


def build_animals_output(animals_data):
    """Erzeugt einen String mit den Daten aller Tiere.

    Zwischen zwei Tieren steht eine Leerzeile.
    """
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal) + "\n"
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
