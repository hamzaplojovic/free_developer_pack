try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    raise ModuleNotFoundError("Pillow is not installed. Please install it with 'pip/pip3 install Pillow'")

img = Image.open("assets/bg.jpeg")

def draw(text:str, x:int, y:int):
    global img
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assets/ARIAL.ttf", 100)
    draw.text((x, y), text=text, fill=0, font=font)
    img.save("assets/out.jpg")

def main(*args):
    draw(args[0], 60, 96)
    draw(f"ID: {args[1]}", 60, 186)
    draw(f"Valid until {args[2]}", 60, 276)
    draw(args[3], 60, 396)

if __name__ == "__main__":
    # name = input("Full Name: ")
    # id = input("Random ID ( 6 digits ): ")
    # date = input("Valid until ( MM/YYYY ): ")
    # school = input("School ( near your area ): ")

    main("Ajsa Besirovic", "880007", "08/2023", "Bratstvo Elementary School")

    img = Image.open("assets/out.jpg")
    img.show()