try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Pillow is not installed. Please install it with 'pip/pip3 install Pillow'"
    )

img = Image.open("assets/bg.jpeg")


def draw(text: str, x: int, y: int):
    global img
    image_drawed = ImageDraw.Draw(img)
    font = ImageFont.truetype("assets/ARIAL.ttf", 100)
    image_drawed.text((x, y), text=text, fill=0, font=font)
    img.resize((3060, 1440)).save("assets/out.png")


def main(*args):
    draw(args[0], 60, 96)
    draw(f"ID: {args[1]}", 60, 186)
    draw(f"Valid until {args[2]}", 60, 276)
    draw(args[3], 60, 396)


if __name__ == "__main__":
    name = input("Full Name: ")
    id = input("Random ID ( 6 digits ): ")
    date = input("Valid until ( MM/YYYY ): ")
    school = input("School ( near your area ): ")
    main(name, id, date, school)

    img = Image.open("assets/out.png")
    img.show()