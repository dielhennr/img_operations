from PIL import Image
import sys



def main():

    if len(sys.argv) < 2:
        print ("You must supply a file name as an argument when running this program.")
        sys.exit(2)

    inputImage = sys.argv[1]

    inputImage = Image.open(inputImage)

    imageWidth, imageHeight = inputImage.size
    option = int(input("Editing menu\n1 for Copy image\n2 for flipping image vertically\n3 for flipping image horixontally\n" +
        "4 for lightening the image\n5 for darkening the image\n6 for horizontal scroll\n7 for vertical scroll\n"+
        "8 for greyscale\n9 for rotate\n10 for swap corners\n11 for blur\n12 for scale\n:: "))

    while (option > 12 or option < 1) and option != -1:
        option = int(input("Please enter a number between 1 and 10 based on what you want to do with your image, -1 to quit\n::"))

    if option == -1:
        print("Thanks have a good day.")  

    elif option == 1:
        copyImage(inputImage, imageWidth, imageHeight)

    elif option == 2:
        flip_vert(inputImage, imageWidth, imageHeight)

    elif option == 3:
        flip_horiz(inputImage,imageWidth, imageHeight)

    elif option == 4:
        amount = float(input("Enter a number between 0 and 1: "))
        lighten_image(inputImage, imageWidth, imageHeight, amount)

    elif option == 5:
        amount = float(input("Enter a number between 0 and 1: "))
        darken_image(inputImage, imageWidth, imageHeight, amount)

    elif option == 6:
        num_pixels = int(input("Enter a number of pixels you want to scroll horizontally.\n" +
        "The picture is " + str(imageWidth) + " pixels wide::"))
        while num_pixels > imageWidth:
            num_pixels -= imageWidth
        horizontal_scroll(inputImage, imageWidth, imageHeight, num_pixels)

    elif option == 7:
        num_pixels = int(input("Enter a number of pixels you want to scroll vertically.\n" +
        "The picture is " + str(imageHeight) + " pixels high::"))
        while num_pixels > imageHeight:
            num_pixels -= imageHeight
        vertical_scroll(inputImage, imageWidth, imageHeight, num_pixels)

    elif option == 8:
        make_greyscale(inputImage, imageWidth, imageHeight)

    elif option == 9:
        rotate(inputImage, imageWidth, imageHeight)

    elif option == 10:
        swap_corners(inputImage, imageWidth, imageHeight)

    elif option == 11:
        blur(inputImage, imageWidth, imageHeight)

    elif option == 12:
        scalar = int(input("Enter an integer scalar value\n:: "))
        scale_image(inputImage, imageWidth, imageHeight, scalar)


# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("copy.png")

def flip_vert(inputImage, imageWidth, imageHeight):
    vert_output = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            new_height = imageHeight - (j+1)
            vert_output.putpixel((i, new_height), pixelColors)

    vert_output.save("verticalflip.png")

def flip_horiz(inputImage, imageWidth, imageHeight):
    horiz_output = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            new_width = imageWidth - (i + 1)
            horiz_output.putpixel((new_width, j), pixelColors)

    horiz_output.save("horizontalflip.png")

def lighten_image(inputImage, imageWidth, imageHeight, amount):
    lighten_image_output = Image.new('RGB', (imageWidth,imageHeight), 'white')
    
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            new_red = ((1-amount)*pixelColors[0]) + amount*255
            new_green = ((1-amount)*pixelColors[1]) + amount*255
            new_blue = ((1-amount)*pixelColors[2]) + amount*255
            new_pixelColors = (int(new_red), int(new_green), int(new_blue))
            lighten_image_output.putpixel((i,j), new_pixelColors)

    lighten_image_output.save('lighter.png')

def darken_image(inputImage, imageWidth, imageHeight, amount):
    darken_image_output = Image.new('RGB', (imageWidth,imageHeight), 'white')
    
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            new_red = ((1-amount)*pixelColors[0])
            new_green = ((1-amount)*pixelColors[1]) 
            new_blue = ((1-amount)*pixelColors[2]) 
            new_pixelColors = (int(new_red), int(new_green), int(new_blue))
            darken_image_output.putpixel((i,j), new_pixelColors)

    darken_image_output.save('darker.png')

def horizontal_scroll(inputImage, imageWidth, imageHeight, num_pixels):
    horizontal_scroll_output = Image.new('RGB', (imageWidth,imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            new_position = i + (num_pixels-1)
            
            #Avoid imageWidth because it doesn't refer to a position.
            #Last x coordinate is imageWidth - 1
            if new_position < imageWidth:
                horizontal_scroll_output.putpixel((new_position, j), pixelColors)

            elif new_position > imageWidth:
                new_position -= (imageWidth + 1)
                horizontal_scroll_output.putpixel((new_position,j), pixelColors)
                

    horizontal_scroll_output.save('horizontalscroll.png')

def vertical_scroll(inputImage, imageWidth, imageHeight, num_pixels):
    vertical_scroll_output = Image.new('RGB', (imageWidth,imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            new_position = j + (num_pixels-1)

            #Avoid imageHeight
            if new_position < imageHeight:
                vertical_scroll_output.putpixel((i, new_position), pixelColors)

            elif new_position > imageHeight:
                new_position -= (imageHeight + 1)
                vertical_scroll_output.putpixel((i, new_position), pixelColors)


    vertical_scroll_output.save('verticalscroll.png')

def make_greyscale(inputImage, imageWidth, imageHeight):
    make_greyscale_output = Image.new('RGB', (imageWidth,imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            greyscale = int((pixelColors[0] * 0.3) + (pixelColors[1]* 0.59) + (pixelColors[2]* 0.11))
            
            new_pixelColors = (greyscale, greyscale, greyscale)
            make_greyscale_output.putpixel((i,j), new_pixelColors)

    make_greyscale_output.save('greyscale.png')

def rotate(inputImage, imageWidth, imageHeight):
    rotate_output = Image.new('RGB', (imageHeight, imageWidth), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))

            #Need to flip across y axis of image before flipping the coordinates
            new_height = imageWidth - (i + 1)

                                            ###Flip coordinates
            rotate_output.putpixel((j, new_height), pixelColors)


    rotate_output.save('rotate.png')

def swap_corners(inputImage, imageWidth, imageHeight):
    swap_corners_output = Image.new('RGB', (imageWidth,imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))

            cut_height = imageHeight//2
            cut_width = imageWidth//2

            if j < cut_height:
                new_height = j + cut_height

            ### >= to remove whitespace, accounting for when j - cutwidth = 0
            elif j >= cut_height:
                new_height = j - cut_height

            if i < cut_width:
                new_width = i + cut_width

            ### >= to remove whitespace, accounting for when i - cutwidth = 0
            elif i >= cut_width:
                new_width = i - cut_width


            swap_corners_output.putpixel((new_width, new_height), pixelColors)

    swap_corners_output.save('swapcorners.png')


def blur(inputImage, imageWidth, imageHeight):
    blur_output = Image.new('RGB', (imageWidth, imageHeight), 'white')
    
    for i in range(imageWidth):
        for j in range(imageHeight):
            avg_red = 0
            avg_green = 0
            avg_blue = 0
            counter = 0
            for a in range(-1, 2):
                for b in range(-1,2):
                    if (i + a >= 0) and (j + b >= 0) and (j + b <= imageHeight - 1) and (i + a <= imageWidth-1):
                        counter +=1
                        old_colors = inputImage.getpixel((i+a, j+b))

                        avg_red += old_colors[0]
                        avg_green += old_colors[1]
                        avg_blue += old_colors[2]

            avg_colors = ((avg_red//counter, avg_green//counter, avg_blue//counter))

            blur_output.putpixel((i,j), avg_colors)

    blur_output.save('blurred.png')


def scale_image(inputImage, imageWidth, imageHeight, scalar):
    scale_image_output = Image.new('RGB', (imageWidth*scalar, imageHeight*scalar),'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            for new_x_pix in range(scalar):
                for new_y_pix in range(scalar):
                    print(scalar*i + new_x_pix, " ", scalar*j + new_y_pix)
                    pixel_position = (scalar*i + new_x_pix, scalar*j + new_y_pix)
                    pixelColors = inputImage.getpixel((i,j))

                    scale_image_output.putpixel(pixel_position, pixelColors)

    scale_image_output.save('scaled.png')



main()

