from PIL import Image, ImageFilter

img = Image.open('pokedex/pikachu.jpg')
filterd_img = img.convert('L')
img.save('pokedex/pikachu_gray.jpg', 'JPEG')
