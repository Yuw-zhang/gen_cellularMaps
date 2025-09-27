from utils import *

def get_mag(oslide, mask):
    """
    :param oslide: whole slide image
    :param mask: Tumor-TIL mask
    :return: magnification value
    """

    # get oslide width and height

    owidth, oheight = oslide.dimensions

    # get mask width and height
    mask = np.array(mask)
    mheight, mwidth = mask.shape[0], mask.shape[1]
    
    # get PROPERTY_NAME_OBJECTIVE_POWER
    mpp = int(oslide.properties[openslide.PROPERTY_NAME_OBJECTIVE_POWER])

    # extract the magnification
    if mpp == 40:
        mag = max(round(owidth / mwidth), round(oheight / mheight))
    elif mpp == 20:
        # mag = 2 * max(round(owidth / mwidth), round(oheight / mheight))
        mag = 0.925 * max(round(owidth / mwidth), round(oheight / mheight))
    else:
        print('mpp error.')
    
    return mag

def norm_loc(contour_loc, mag):
    """
    :param contour_loc: the contour polygons for one cell
    :param mag: magnification
    :return: the list of resized contour polygons for each cell
    """
    contour_loc = list(map(lambda loc: np.round(np.array(literal_eval(loc)) / mag), contour_loc))

    return contour_loc

def mode_loc(norm_loc):
    """
    :param norm_loc: normalized contour polygons which were already divided by the magnification
    :return: the list of contour polygons which are the mode value for each cell
    """
    for i in range(len(norm_loc)):
        norm_loc[i] = stats.mode(norm_loc[i])[0][0]

    return norm_loc

