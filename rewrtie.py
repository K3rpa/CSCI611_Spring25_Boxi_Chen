import os
import random

IMAGES_DIR = "mtsd_v2_fully_annotated/images"
SPLITS_DIR = "mtsd_v2_fully_annotated/splits"

os.makedirs(SPLITS_DIR, exist_ok=True)

all_images = [os.path.join(IMAGES_DIR, f) for f in os.listdir(IMAGES_DIR) if f.endswith(".jpg")]

random.shuffle(all_images)

train_split = int(0.8 * len(all_images))
val_split = int(0.9 * len(all_images))

train_files = all_images[:train_split]
val_files = all_images[train_split:val_split]
test_files = all_images[val_split:]

for split_name, files in zip(["train", "val", "test"], [train_files, val_files, test_files]):
    split_path = os.path.join(SPLITS_DIR, f"{split_name}_full.txt")
    with open(split_path, "w", encoding="utf-8") as f:
        f.write("\n".join(files))
    print(f"Created {split_name}_full.txt with {len(files)} images")



