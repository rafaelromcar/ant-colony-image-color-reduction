def initialize():
    '''
    Data initializing. 
    '''

def pixelSelect():
    '''
    Select a random position with a unless a pixel in his heap.
    '''

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
    initialize()
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

