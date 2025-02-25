import json

# Your JSON list
data = [ {
    "kanji": "本屋",
    "reading": "honya",
    "meaning": "bookstore"
  },
  {
    "kanji": "八百屋",
    "reading": "yaoya",
    "meaning": "vegetable store"
  },
  {
    "kanji": "そば屋",
    "reading": "sobaya",
    "meaning": "soba restaurant"
  },
  {
    "kanji": "たばこ屋",
    "reading": "tabakoya",
    "meaning": "cigarette shop"
  },
  {
    "kanji": "茶",
    "reading": "cha",
    "meaning": "tea(plain form)"
  },
  {
    "kanji": "お茶",
    "reading": "ocha",
    "meaning": "tea but polite form"
  },
  {
    "kanji": "茶わん",
    "reading": "chawan",
    "meaning": "ricebowl"
  },
  {
    "kanji": "未来",
    "reading": "mirai",
    "meaning": "future"
  },
  {
    "kanji": "週末",
    "reading": "shuumatsu",
    "meaning": "weekend"
  },
  {
    "kanji": "料理",
    "reading": "ryouri",
    "meaning": "cooking"
  },
  {
    "kanji": "無理",
    "reading": "muri",
    "meaning": "impossible"
  },
  {
    "kanji": "無くす",
    "reading": "nakusu",
    "meaning": "get rid of"
  },
  {
    "kanji": "無くなる",
    "reading": "nakunaru",
    "meaning": "disappear, run short, get lost"
  },
  {
    "kanji": "作文",
    "reading": "sakubun",
    "meaning": "essay"
  },
  {
    "kanji": "用いる",
    "reading": "mochiiru",
    "meaning": "make use of"
  },
  {
    "kanji": "用事",
    "reading": "youji",
    "meaning": "errands"
  },
  {
    "kanji": "消える",
    "reading": "be",
    "meaning": "extinguished disappear"
  },
  {
    "kanji": "消しゴム",
    "reading": "keshigomu",
    "meaning": "eraser"
  },
  {
    "kanji": "売れる",
    "reading": "ureru",
    "meaning": "sell, be in demand"
  },
  {
    "kanji": "売り場",
    "reading": "uriba",
    "meaning": "ales floor/department"
  },
  {
    "kanji": "店員",
    "reading": "tenin",
    "meaning": "clerk, salesperson"
  },
  {
    "kanji": "味",
    "reading": "aji",
    "meaning": "taste"
  },
  {
    "kanji": "売店",
    "reading": "baiten",
    "meaning": "booth/store"
  },
  {
    "kanji": "商品",
    "reading": "shouhin",
    "meaning": "goods"
  },
  {
    "kanji": "作品",
    "reading": "sakuhin",
    "meaning": "work of art/piece"
  },
  {
    "kanji": "販売",
    "reading": "hanbai",
    "meaning": "sale/selling"
  },
  {
    "kanji": "二階",
    "reading": "nikai",
    "meaning": "second floor/upstairs"
  },
  {
    "kanji": "段階",
    "reading": "dankai",
    "meaning": "stage"
  },
  {
    "kanji": "階段",
    "reading": "kaidan",
    "meaning": "steps/flight of stairs"
  },
  {
    "kanji": "段々",
    "reading": "dandan",
    "meaning": "gradually/one after another"
  },
  {
    "kanji": "値段",
    "reading": "nedan",
    "meaning": "price"
  },
  {
    "kanji": "価格",
    "reading": "kakaku",
    "meaning": "price/cost"
  },
  {
    "kanji": "合格",
    "reading": "goukaku",
    "meaning": "passing an examination"
  },
  {
    "kanji": "夏休み",
    "reading": "natsuyasumi",
    "meaning": "summer vacation"
  },
  {
    "kanji": "冬休み",
    "reading": "fuyuyasumi",
    "meaning": "winter vacation"
  },
  {
    "kanji": "四季",
    "reading": "shiki",
    "meaning": "four season"
  },
  {
    "kanji": "暑さ",
    "reading": "atsusa",
    "meaning": "summer heat"
  },
  {
    "kanji": "熱",
    "reading": "netsu",
    "meaning": "fever/heat"
  },
  {
    "kanji": "寒さ",
    "reading": "samosa",
    "meaning": "coldness/cold"
  }
]
# Remove duplicates based on the "kanji" field
unique_data = []
seen_kanji = set()
duplicates = []

for entry in data:
    kanji = entry["kanji"]
    if kanji not in seen_kanji:
        unique_data.append(entry)
        seen_kanji.add(kanji)
    else:
        duplicates.append(entry)  # Log duplicates for verification

# Save the unique data to a JSON file in compact format
output_file = "unique_data_compact.json"
with open(output_file, "w", encoding="utf-8") as f:
    for i, entry in enumerate(unique_data):
        json.dump(entry, f, ensure_ascii=False, separators=(",", ":"))
        if i < len(unique_data) - 1:  # Add a comma unless it's the last entry
            f.write(",\n")
        else:
            f.write("\n")

# Save duplicates to a separate file for verification
duplicates_file = "duplicates_log.json"
with open(duplicates_file, "w", encoding="utf-8") as f:
    json.dump(duplicates, f, ensure_ascii=False, indent=2)

print(f"Unique data saved to {output_file}.")
print(f"Duplicates logged to {duplicates_file}.")