from PIL import Image, ImageFilter 

def initialize(imageURL):
    '''
    Data initializing. 
    Variables:
		alpha: Influence of similarity for the ant to drops the element.
		dropTh: Drop threshold. Minimum threshold for dropping a pixel 
		on the image.
		memTh: Memory threshold. Minimum threshold for dropping a pixel 
		which position is stored on the ant memory.
		x: Percent of the longest path in the image that may be analized
		y: Percent of total number of pixels that will be analized.
		nIt1: Number of pixel that will be analized. 
		kRange: Longest path for a single ant to look over. 
    '''
	alpha = 1
	dropTh= 0.6
	memTh= 35
	x = 20 
	y = 10
	n = matrixImage.size[0]
	m = matrixImage.size[1]
	nIt1 = m*n*Y/100 
	kRange =(m+n)*x/100
	image = Image.open(imageURL)
    matrixImage = image.load()
    matrixHeaps = Array()
    for i in range(m):
		for j in range(n):
			matrixHeaps[i][j] = Array(matrixImage[i][j])
	return matrixHeaps, alpha, dropTh, memTh, nIt1, kRange
	
def pixelSelect(matrixHeaps):
    '''
    Select a random position with a unless a pixel in his heap.
    '''
    n = matrixHeaps.size[0]-1
    m = matrixHeaps.size[1]-1
    i = random.randint(0,n)
    j = random.randint(0,m)
    while not matrixHeaps[i][j]:
		i = random.randint(0,n)
		j = random.randint(0,m)
	position = (i,j)
    return position
    
def antMemory(position):
    '''
    Add the heap position of the actual heap to the ant memory if it is bigger than 
    any element(erase the smaller). If is not bigger, add the heap to the head of the
    most similar heap in a minimun condition. Return a boolen state wich information
    if you have added something to ant memory.
    '''

def sameNeigh(position):
    '''
    Check if the pixel in position is similar to his neighbourhood in a minimun condition.
    Return a boolean state to indicate if it is similar or not.
    '''

def moveAndDropSimilarNeigh(position):
    '''
    Look for the most similar pixel near position and drop the pixel of position
    there.
    '''

def antPalette(nIt1,kRange):
    '''
    Reduction of color palette in image based on ant colony
    '''
    initialize(imageURL)
    for i in range(nIt1):
        position = pixelSelect()
        droppedInAnt = antMemory(position)
        if not droppedInAnt:
            for j in range(kRange):
                droppedInImage = sameNeigh(position)
                if droppedInImage:
                    break
                else:
                    position = moveAndDropSimilarNeigh(position)

