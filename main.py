
from rembg import remove
from PIL import Image

input_path = 'scimmia.jpg'
output_path ='ttt.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)