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
	nColors = 256
	image = Image.open(imageURL)
    matrixImage = image.load()
    matrixHeaps = Array()
    for i in range(m):
		for j in range(n):
			matrixHeaps[i][j] = Array(matrixImage[i][j])
	return matrixHeaps, alpha, dropTh, memTh, nIt1, kRange, nColors
	
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
    
def antMemory(matrixHeaps, position, antMem, memTh):
    '''
    Add the heap position of the actual heap to the ant memory if it is bigger than 
    any element(erase the smaller). If is not bigger, add the heap to the head of the
    most similar heap in a minimun condition. Return a boolen state wich information
    if you have added something to ant memory.
    '''
    actHeap = matrixHeaps[position[0], position[1]]
    minLength = len(matrixHeaps[position[0], position[1]])
    minSim = memTh
    changeCompleteHeap = 0
    addElement = 0
	for i in range(nColors):
		antHeap = antMem[i]
		if len(antHeap) < minLength:
			minLength = len(antHeap)
			heapToChange = antHeap
			changeCompleteHeap = 1
		else minSim > distanceFunc(actHeap[-1], antHeap[-1]):
			minSim = distanceFunc(actHeap[-1], antHeap[-1])
			heapToChange = antHeap
			addElement = 1
	if changeCompleteHeap:
		heapToChange = actHeap
	elif addElement:
		heapToChange.append(actHeap[-1])
	return changeCompleteHeap or addElement
		
    

def distanceFunc(pixelAct,pixelNeigh):
	'''
	Used for comparate pixels on the position of the ant memory and in the similarity function.
	'''
	return abs(pixelNeigh[0] - pixelAct[0]) + abs(pixelNeigh[1] - pixelAct[1]) + abs(pixelNeigh[2] - pixelAct[2])
	
def similarityFunc(matrixHeaps, position, alpha):
	'''
	Used for calculate the similarity between the pixel a pixel and his neighbours.
	'''
	sol = 0
	pixelAct = matrixHeaps[position[0]][position[1]][-1]
	for i in range(position[0]-1, position[0]+2):
		for j in range(position[1]-1, position[1]+2):
			if not (i==position[0] and j==position[1]):
			pixelNeigh = matrixHeaps[i][j][-1]
			sol+= (1-(distanceFunc(pixelAct,pixelNeigh)/alpha))
	return sol
	
def sameNeigh(matrixHeaps, position, dropTh,alpha):
    '''
    Check if the pixel in position is similar to his neighbours in a minimun condition.
    Return a boolean state to indicate if it is similar or not.
    '''
    droppedInImage = dropTh < similarityFunc(matrixHeaps, position, alpha)  
    return droppedInImage

def moveAndDropSimilarNeigh(matrixHeaps, position):
    '''
    Look for the most similar pixel near position and drop the pixel of position
    there.
    '''
    minDist = 765  #Maxmimum distance between two RGB pixels
    pixelAct = matrixHeaps[position[0]][position[1]][-1]
    for i in range(position[0]-1, position[0]+2):
		for j in range(position[1]-1, position[1]+2):
			if not (i==position[0] and j==position[1]):
			heapNeigh = matrixHeaps[i][j]
			actDis = distanceFunc(HeapAct[-1],HeadpSim[-1]):
			if minDist > actDis:
				minDist = actDis
				pixelSimPos = (i,j)
				HeadpSim = HeapNeigh
	heapSim.append(HeapAct.pop())
	return pixelSimPos

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
                droppedInImage = sameNeigh(matrixHeaps, position, alpha)
                if droppedInImage:
                    break
                else:
                    position = moveAndDropSimilarNeigh(position)

