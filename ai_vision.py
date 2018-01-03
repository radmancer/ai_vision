from PIL import Image #osx way of importing Image
#import Image
################################################################################
#                                   Functions                                  #
################################################################################
#This function is incomplete.
#It needs to return or otherwise do something more
#interesting than print the RGB values of each pixel.
def TraverseImage(ImgName):
    img = Image.open(ImgName)
    ImgWidth = img.size[0]
    ImgHeight = img.size[1]
    #loaded image object into memory.
    pixels = img.load()
    for y in range(ImgHeight):
        for x in range(ImgWidth):
            #pixelColor = img.getpixel((x, y)) #the slow method.
            pixelColor = pixels[x, y]
            print pixelColor

#Scans from left to right, top to bottom for pixels of a desired color,
#once found, the pixel's coordinate is returned.
def PixelScan(PixelColor):
    for j in range(ImageHeight):        
        for i in range(ImageWidth):
            if(ImageArray[i, j]  == PixelColor):
                return (i, j)

    print "No pixel found!"

#Searches for the next pixel in the shape's hull
#based on what cycle algorithm is being used.
#NOTE: The kernel should be scanned in an H pattern.
#      (i, j) - Sobel Pixel
#      (i +- 1, j +-1) - Kernel
def CycleSearch(Algorithm, Point, PixelColor):
    i = Point[0]
    j = Point[1]

    #See "Algorithm1.png" for more details.
    if(Algorithm == 1):
        if(ImageArray[i, j - 1] == PixelColor):
            HullStack.append((i, j - 1))
            return

        if(ImageArray[i - 1, j - 1] == PixelColor):
            HullStack.append((i - 1, j - 1))
            return

        if(ImageArray[i - 1, j] == PixelColor):
            HullStack.append((i - 1, j))
            return

        if(ImageArray[i - 1, j + 1] == PixelColor):
            HullStack.append((i - 1, j + 1))
            return

        if(ImageArray[i, j + 1] == PixelColor):
            HullStack.append((i, j + 1))
            return

        if(ImageArray[i + 1, j + 1] == PixelColor):
            HullStack.append((i + 1, j + 1))
            return

        if(ImageArray[i + 1, j] == PixelColor):
            HullStack.append((i + 1, j))
            return

        if(ImageArray[i + 1, j - 1] == PixelColor):
            HullStack.append((i + 1, j - 1))
            return

    #See "Algorithm2.png" for more details.
    if(Algorithm == 2):
        if(ImageArray[i - 1, j] == PixelColor):
            HullStack.append((i - 1, j))
            return

        if(ImageArray[i - 1, j + 1] == PixelColor):
            HullStack.append((i - 1, j + 1))
            return

        if(ImageArray[i, j + 1] == PixelColor):
            HullStack.append((i, j + 1))
            return

        if(ImageArray[i + 1, j + 1] == PixelColor):
            HullStack.append((i + 1, j + 1))
            return

        if(ImageArray[i + 1, j] == PixelColor):
            HullStack.append((i + 1, j))
            return

        if(ImageArray[i + 1, j - 1] == PixelColor):
            HullStack.append((i + 1, j - 1))
            return

        if(ImageArray[i, j - 1] == PixelColor):
            HullStack.append((i, j - 1))
            return

        if(ImageArray[i - 1, j - 1] == PixelColor):
            HullStack.append((i - 1, j - 1))
            return

    #See "Algorithm3.png" for more details.
    if(Algorithm == 3):
        if(ImageArray[i, j + 1] == PixelColor):
            HullStack.append((i, j + 1))
            return

        if(ImageArray[i + 1, j + 1] == PixelColor):
            HullStack.append((i + 1, j + 1))
            return

        if(ImageArray[i + 1, j] == PixelColor):
            HullStack.append((i + 1, j))
            return
        
        if(ImageArray[i + 1, j - 1] == PixelColor):
            HullStack.append((i + 1, j - 1))
            return

        if(ImageArray[i, j - 1] == PixelColor):
            HullStack.append((i, j - 1))
            return

        if(ImageArray[i - 1, j - 1] == PixelColor):
            HullStack.append((i - 1, j - 1))
            return

        if(ImageArray[i - 1, j] == PixelColor):
            HullStack.append((i - 1, j))
            return

        if(ImageArray[i - 1, j + 1] == PixelColor):
            HullStack.append((i - 1, j + 1))
            return

    #See "Algorithm4.png" for more details.
    if(Algorithm == 4):
        if(ImageArray[i + 1, j] == PixelColor):
            HullStack.append((i + 1, j))
            return

        if(ImageArray[i + 1, j - 1] == PixelColor):
            HullStack.append((i + 1, j - 1))
            return

        if(ImageArray[i, j - 1] == PixelColor):
            HullStack.append((i, j - 1))
            return

        if(ImageArray[i - 1, j - 1] == PixelColor):
            HullStack.append((i - 1, j - 1))
            return

        if(ImageArray[i - 1, j] == PixelColor):
            HullStack.append((i - 1, j))
            return

        if(ImageArray[i - 1, j + 1] == PixelColor):
            HullStack.append((i - 1, j + 1))
            return

        if(ImageArray[i, j + 1] == PixelColor):
            HullStack.append((i, j + 1))
            return

        if(ImageArray[i + 1, j + 1] == PixelColor):
            HullStack.append((i + 1, j + 1))
            return

    print "No pixel in that color range was found!"
    
    return

#Switches the cycle algorithm used based on the pixel color that is
#directly left, below, right, or above the current point.
def SwitchAlgorithm(Point, PixelColor):
    global Algorithm
    i = Point[0]
    j = Point[1]

    #The pixel above the current point is not black.
    if(ImageArray[i, j - 1] != PixelColor):
        Algorithm = 1
        return

    #The pixel to the left of the current point is not black.
    if(ImageArray[i - 1, j] != PixelColor):
        Algorithm = 2
        return

    #The pixel below the current point is not black.
    if(ImageArray[i, j + 1] != PixelColor):
        Algorithm = 3
        return

    #The pixel to the right of the current point is not black.
    if(ImageArray[i + 1, j] != PixelColor):
        Algorithm = 4
        return

#Draws any set of points as a 2d polygon.
def DrawShape(Array, Color):
    draw = ImageDraw.Draw(image)

    for i in range(len(Array)):
        if(i == len(Array) - 1):
            break;
        draw.line([Array[i], Array[i + 1]], Color)

    draw.line([Array[-1], Array[0]], Color)

    del draw
    
    image.save("output.png")

#Top left corner of the bounding box.
def BoundingBoxTopLeft():
    X = []
    Y = []

    for i in range(len(HullStack)):
        X.append(HullStack[i][0])

    for i in range(len(HullStack)):
        Y.append(HullStack[i][1])

    return (min(X), min(Y))

#Bottom left corner of the bounding box.
def BoundingBoxBottomLeft():
    X = []
    Y = []

    for i in range(len(HullStack)):
        X.append(HullStack[i][0])

    for i in range(len(HullStack)):
        Y.append(HullStack[i][1])

    return (min(X), max(Y))

#Bottom right corner of the bounding box.
def BoundingBoxBottomRight():
    X = []
    Y = []

    for i in range(len(HullStack)):
        X.append(HullStack[i][0])

    for i in range(len(HullStack)):
        Y.append(HullStack[i][1])

    return (max(X), max(Y))

#Top right corner of the bounding box.
def BoundingBoxTopRight():
    X = []
    Y = []

    for i in range(len(HullStack)):
        X.append(HullStack[i][0])

    for i in range(len(HullStack)):
        Y.append(HullStack[i][1])

    return (max(X), min(Y))

def arcsin(n):
    #converts n from degrees to radians
    n = n * math.pi/180
    return math.asin(n) * 180/math.pi

def sin(n):
    #converts n from degrees to radians
    n = n * math.pi/180
    return math.sin(n)

def cos(n):
    #converts n from degrees to radians
    n = n * math.pi/180
    return math.cos(n)

def tan(n):
    #converts n from degrees to radians
    n = n * math.pi/180
    return math.tan(n)