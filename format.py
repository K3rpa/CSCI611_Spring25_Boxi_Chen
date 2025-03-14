import os
import json

ANNOTATIONS_DIR = "mtsd_v2_fully_annotated/annotations"
LABELS_DIR = "mtsd_v2_fully_annotated/labels"

os.makedirs(LABELS_DIR, exist_ok=True)

class_labels = set()
for json_file in os.listdir(ANNOTATIONS_DIR):
    if json_file.endswith(".json"):
        with open(os.path.join(ANNOTATIONS_DIR, json_file), "r", encoding="utf-8") as f:
            data = json.load(f)
            for obj in data.get("objects", []):
                class_labels.add(obj["label"])

class_id_map = {label: idx for idx, label in enumerate(sorted(class_labels))}
with open("class_id_map.json", "w", encoding="utf-8") as f:
    json.dump(class_id_map, f, indent=4)

print(class_id_map)

def convert_bbox(width, height, bbox):
    x_min, y_min, x_max, y_max = bbox["xmin"], bbox["ymin"], bbox["xmax"], bbox["ymax"]
    x_center = (x_min + x_max) / 2 / width
    y_center = (y_min + y_max) / 2 / height
    w = (x_max - x_min) / width
    h = (y_max - y_min) / height
    return x_center, y_center, w, h

for json_file in os.listdir(ANNOTATIONS_DIR):
    if json_file.endswith(".json"):
        with open(os.path.join(ANNOTATIONS_DIR, json_file), "r", encoding="utf-8") as f:
            data = json.load(f)
        
        width, height = data["width"], data["height"]
        yolo_annotations = []
        
        for obj in data.get("objects", []):
            label = obj["label"]
            if label not in class_id_map:
                continue  
            class_id = class_id_map[label]
            bbox = obj["bbox"]
            x_center, y_center, w, h = convert_bbox(width, height, bbox)
            yolo_annotations.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

        yolo_txt_file = os.path.join(LABELS_DIR, json_file.replace(".json", ".txt"))
        with open(yolo_txt_file, "w", encoding="utf-8") as f:
            f.write("\n".join(yolo_annotations))

print("done")
