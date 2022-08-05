from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filterd_img = img.convert('L')
filterd_img.save('./pokedex/pikachu_gray.jpg')
