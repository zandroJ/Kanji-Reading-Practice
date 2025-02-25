import json

# Load the JSON file
with open("kanji_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract only the kanji characters
kanji_list = [entry["kanji"] for entry in data]

# Save the filtered kanji list to a new file
with open("kanji_only.json", "w", encoding="utf-8") as output_file:
    json.dump(kanji_list, output_file, ensure_ascii=False, indent=2)

print("Filtered kanji list saved to kanji_only.json")
