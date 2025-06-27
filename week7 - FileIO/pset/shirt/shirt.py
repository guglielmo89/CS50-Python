from PIL import Image, ImageOps
import sys

FORMATS = ["jpeg", "jpg", "png"]


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].lower().split(".")[1] not in FORMATS or sys.argv[2].lower().split(".")[1] not in FORMATS:
        sys.exit("Invalid output")
    elif sys.argv[1].lower().split(".")[1] != sys.argv[2].lower().split(".")[1]:
        sys.exit("Input and output have different extensions")

    try:
       with Image.open(f"{sys.argv[1]}") as img, Image.open("shirt.png") as tshirt :
           img = ImageOps.fit(img, (tshirt.size[0], tshirt.size[1]))
           img.paste(tshirt, (0,0), tshirt)
           img.save(f"{sys.argv[2]}")
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
