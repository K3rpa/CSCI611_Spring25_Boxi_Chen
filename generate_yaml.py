import json

with open("class_id_map.json", "r", encoding="utf-8") as f:
    class_id_map = json.load(f)

yaml_content = f"""train: /home/bchen/csci611/CSCI611_Spring25_Boxi_Chen/mtsd_v2_fully_annotated/splits/train_full.txt
val: /home/bchen/csci611/CSCI611_Spring25_Boxi_Chen/mtsd_v2_fully_annotated/splits/val_full.txt
test: /home/bchen/csci611/CSCI611_Spring25_Boxi_Chen/mtsd_v2_fully_annotated/splits/test_full.txt

nc: {len(class_id_map)}
names: {json.dumps(list(class_id_map.keys()), indent=4)}
"""

with open("my_dataset.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_content)

print(f"success: my_dataset.yaml")
