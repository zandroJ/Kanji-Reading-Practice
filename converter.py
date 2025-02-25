import csv
import json

# File paths
input_file = "young.txt"  
output_file = "kanji_data1.json"

# Read the cleaned Anki export
kanji_list = []
with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter="\t")
    next(reader)  # Skip header if there's any

    for row in reader:
        if len(row) >= 3:  # Ensure there are enough columns
            kanji = row[0].strip()  # Kanji
            reading = row[1].strip()  # Reading
            meaning = row[2].strip()  # Meaning
            kanji_list.append({"kanji": kanji, "reading": reading, "meaning": meaning})

# Save as JSON
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(kanji_list, json_file, ensure_ascii=False, indent=4)

print("✅ Kanji data saved as kanji_data.json")
