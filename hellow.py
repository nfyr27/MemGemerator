from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
top_text = input("Верхний текст: ")
bottom_text = input("Нижний текст: ")
print("Список картинок: ")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = input("Номер картинки: ")

if image_number == "1":
    file_name = "Кот в ресторане.png"
elif image_number == "2":
    file_name = "Кот в очках.png"

image = Image.open(file_name)
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("impact.ttf", 70)

width, height = image.size

draw.text((width // 2, 10), top_text, font=font, anchor="mt", stroke_fill="black", stroke_width=5)
draw.text((width // 2, height - 10), bottom_text, font=font, anchor="mb", stroke_fill="black", stroke_width=5)

image.save("result.png")
