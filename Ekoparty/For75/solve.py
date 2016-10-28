from PIL import Image

img = Image.new( 'RGB', (8, 1875), "black") # create a new black image
pixels = img.load() # create the pixel map
fname = "output.txt"
with open(fname) as f:
    content = f.readlines()
tmpI = 0
tmpK = 0
for i in content:
	result = i.split(" ")
	tmpK = 0
	for i in result:
		if len(i) == 4:
			pixels[tmpK,tmpI]= int(i,16)

			tmpK = tmpK + 1	
	tmpI = tmpI + 1
	'''
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 1)
        '''

img.show()