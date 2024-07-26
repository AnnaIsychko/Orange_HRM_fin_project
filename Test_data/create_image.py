from PIL import Image, ImageDraw

# Создайте новое изображение с белым фоном
width, height = 200, 200
image = Image.new('RGB', (width, height), color='white')

# Нарисуйте что-то на изображении
draw = ImageDraw.Draw(image)
draw.text((50, 50), "Hello, World!", fill='black')

# Сохраните изображение в формате JPG
image.save('example_image.jpg')
