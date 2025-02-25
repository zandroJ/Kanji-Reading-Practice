# Input and output file paths
input_file = "yasui.txt"  # Replace with your input file path
output_file = "cleaned_output.txt"  # Replace with your desired output file path

# Set to track seen kanji
seen_kanji = set()

# Open the input file and process it
with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

# Write cleaned data to the output file
with open(output_file, "w", encoding="utf-8") as outfile:
    for line in lines:
        # Extract the kanji (first part before "=")
        kanji = line.split("=")[0].strip()
        
        # If the kanji hasn't been seen before, write the line to the output file
        if kanji not in seen_kanji:
            outfile.write(line)
            seen_kanji.add(kanji)

print(f"Cleaned data saved to {output_file}.")