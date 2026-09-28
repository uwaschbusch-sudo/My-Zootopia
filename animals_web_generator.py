import json


def load_data(file_path):
    """Lädt eine JSON-Datei und gibt deren Inhalt zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def print_animal(animal):
    """Gibt Name, Diet, erste Location und Type eines Tieres aus.

    Felder, die nicht vorhanden sind, werden übersprungen.
    """
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    if "name" in animal:
        print(f"Name: {animal['name']}")
    if "diet" in characteristics:
        print(f"Diet: {characteristics['diet']}")
    if locations:
        print(f"Location: {locations[0]}")
    if "type" in characteristics:
        print(f"Type: {characteristics['type']}")
    print()


def main():
    """Liest die Tierdaten aus der JSON-Datei und gibt sie aus."""
    animals_data = load_data("animals_data.json")
    for animal in animals_data:
        print_animal(animal)


if __name__ == "__main__":
    main()
    