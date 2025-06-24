import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()
        for row in reader:
            #brightness = calculate_brightness(f"{row['id']}.jpeg")
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)
            writer.writerow(row)
            """writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),
                }
            )"""





def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255
    return brightness


if __name__ == "__main__":
    main()
