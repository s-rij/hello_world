# functions for cropping

# define a function for cropping from top left corner
def crop_image_topleft(im, crop_size: int, loc_x=None, loc_y=None):
    """Crops a square part of the image from the top left corner given a starting location and crop size."""
    if loc_x < 0:
        loc_x = 0
    elif loc_x > im.shape[0]:
        loc_x = im.shape[0]
    else:
        loc_x = loc_x
    
    if loc_y < 0:
        loc_y = 0
    elif loc_y > im.shape[1]:
        loc_y = im.shape[1]
    else:
        loc_y = loc_y

    return im[loc_x:crop_size + loc_x ,loc_y:crop_size + loc_y,:]


# define another function for cropping from a given center (including automatic center)
def crop_image_center(im, crop_size: int, loc_x=None, loc_y=None, auto_center = False):
    """Crops a square part of the image from the center given a location and crop size."""
    s = int(crop_size / 2)
    height, width = im.shape[0], im.shape[1]
    start_x, end_x  = 0, height 
    start_y, end_y = 0, width
    
    if auto_center:
        start_x, end_x = int(height/2) - s, int(height/2) + s
        start_y, end_y = int(width/2)- s, int(width/2) + s
    else:
        if (loc_x - s) >= 0:
            start_x = loc_x - s
        if (loc_x + s) <= height:
            end_x = loc_x + s
        if (loc_y - s) >= 0:
            start_y = loc_y - s
        if (loc_y + s) <= width:
            end_y = loc_y + s

    return im[start_x:end_x, start_y:end_y ,:]


# define another function for cropping given its mask
def crop_image_mask(im, mask):
    """Crops an image to the bounding box of the mask."""
    xs = mask.max(axis=1)
    ys = mask.max(axis=0)
    found_x1, found_x2 = False, False
    found_y1, found_y2 = False, False

    for i in range(len(xs)):
        if (xs[i] == 1) and (not found_x1):
            x1 = i
            found_x1 = True
        if (xs[len(xs)-1 - i] == 1) and (not found_x2):
            x2 = len(xs) -1- i
            found_x2 = True
        if found_x1 and found_x2:
            break

    for j in range(len(ys)):
        if (ys[j] == 1) and (not found_y1):
            y1 = j
            found_y1 = True
        if (ys[len(ys)-1 - j] == 1) and (not found_y2):
            y2 = len(ys) -1- j
            found_y2 = True
        if found_y1 and found_y2:
            break
    
    return im[x1:x2, y1:y2, :]