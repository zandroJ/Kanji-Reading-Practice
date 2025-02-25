import json

# Input text
data = """
本屋 honya bookstore
八百屋 yaoya vegetable store
そば屋 sobaya soba restaurant
たばこ屋 tabakoya cigarette shop
茶 cha tea(plain form)
お茶 ocha tea but polite form
茶わん chawan ricebowl
未来 mirai future
週末 shuumatsu weekend
料理 ryouri cooking
無理 muri impossible
無くす nakusu get rid of
無くなる nakunaru disappear, run short, get lost
作文 sakubun essay
用いる mochiiru  make use of
用事 youji errands
消える be extinguished disappear
消しゴム keshigomu eraser
交通費 koutsuhi
売れる ureru sell, be in demand
売り場 uriba ales floor/department
店員 tenin clerk, salesperson
味 aji taste
売店 baiten booth/store
商品 shouhin goods
作品 sakuhin work of art/piece
販売 hanbai sale/selling
二階 nikai second floor/upstairs
段階 dankai stage
階段 kaidan steps/flight of stairs
段々 dandan gradually/one after another
値段 nedan price
価格 kakaku price/cost
合格 goukaku passing an examination
夏休み natsuyasumi summer vacation
冬休み fuyuyasumi winter vacation
四季 shiki four season
暑さ atsusa summer heat
熱 netsu fever/heat
寒さ samosa coldness/cold
"""

# Output file
output_file = "dataset.json"

# Process the data
lines = data.strip().split("\n")  # Split into lines
dataset = []

for line in lines:
    parts = line.strip().split(maxsplit=2)  # Split into kanji, reading, and meaning
    if len(parts) == 3:  # Ensure there are exactly 3 parts
        kanji, reading, meaning = parts
        dataset.append({"kanji": kanji,"reading": reading, "meaning": meaning})

# Write to the output file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"Dataset saved to {output_file}.")