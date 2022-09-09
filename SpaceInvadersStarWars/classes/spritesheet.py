
# This class handles sprite sheets
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)
#
import pygame

class SpriteSheet(object):
    def __init__(self, filename):
          self.sheet = pygame.image.load(filename).convert()

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)



'''
class SpriteSheet():

    def __init__(self, filename, o_rows, o_cols, rows, cols, p_rows, p_cols):
        """SpriteSheet Contructor"""
        self.image = pg.image.load(filename).convert_alpha()
        self.o_rows = o_rows  # Number of rows of options in sprite total
        self.o_cols = o_cols  # Number of cols of options in sprite total
        self.rows = rows  # Number of rows for sprite chosen
        self.cols = cols  # Number of cols for sprite chosen
        self.p_rows = p_rows  # Row number of chosen sprite in sheet
        self.p_cols = p_cols  # Column number of chosen sprite in sheet

        self.totalCellCount = cols * rows  # Total cells in the specific sprite option chosen

        self.option_w = self.image.get_rect().width / self.o_cols  # Width of particular option in sheet
        self.option_h = self.image.get_rect().height / self.o_rows  # Height of particular option in sheet

        self.offset_x = self.option_w * p_cols  # Offset the X based on which option in the sheet
        self.offset_y = self.option_h * p_rows  # Offset the Y based on which option in the sheet

        self.init_rect = pg.Rect(0, 0, self.option_w,
                                 self.option_h)  # Form initial rectangle (before we break it up into cells)

        self.w = self.cellWidth = self.init_rect.width / cols
        self.h = self.cellHeight = self.init_rect.height / rows

        # Get a list of (X,Y) coordinates of each cell in the sprite sheet with associated heights/widths
        # self.cells = list([((index % cols * self.w) + self.offset_x , (index / cols * self.h) + self.offset_y, self.w, self.h) for index in range(self.totalCellCount)])
        # self.cells = list([((index % cols * self.w), (index % rows * self.h), self.w, self.h) for index in range(self.totalCellCount)])

        self.cells = []
        myCounter = 0

        for ry in range(0, rows):
            for rx in range(0, cols):
                self.cells.append(
                    ((myCounter % cols * self.w) + self.offset_x, (ry * self.h) + self.offset_y, self.w, self.h))
                myCounter += 1
                # print(self.cells)

    def draw(self, cellIndex=0, x=25, y=25):
        self.rect = pg.Rect(x, y, self.w, self.h)  # Form rectangle around cell
        # pg.draw.rect(screen,(100,100,100),self.rect,0) #debug, show rectangles
        screen.blit(self.image, (x, y), self.cells[cellIndex])

'''