from utils import *


def genHoverCellMatrix_20X(mod_loc, mask, cellType, diameterList):
    """
    :param mod_loc: the list of contour polygons representing the mode value for each cell
    :param mask_path: the tumor-til mask path
    :param cellType: [5 types] neoplastic, inflammatory, connective, necrosis, and non-neoplastic
    :return: *typeTumor_matrix, *typeLymph_matrix, *typeTILs_matrix
    """


    mask = np.array(mask)
    shape = mask.shape[:2]

    # Pre-allocate matrices
    main_array = np.full(shape, np.nan)
    main_neo = np.full(shape, np.nan)
    main_inflam = np.full(shape, np.nan)
    main_connec = np.full(shape, np.nan)
    main_dead = np.full(shape, np.nan)
    main_epi = np.full(shape, np.nan)

    # Define valid mask colors
    valid_mask_colors = np.array([[192, 192, 192], [255, 255, 0], [255, 0, 0], [255, 128, 0], [200, 0, 0]])

    # Create mask for valid tissue regions
    tissue_mask = np.any(np.all(mask[:, :, None] == valid_mask_colors, axis=-1), axis=-1)

    # Initialize matrices where mask is valid
    main_array[tissue_mask] = 0
    main_neo[tissue_mask] = 0
    main_inflam[tissue_mask] = 0
    main_connec[tissue_mask] = 0
    main_dead[tissue_mask] = 0
    main_epi[tissue_mask] = 0
    # 20X: 0-neo, 1-inflam, 2-connec, 3-dead, 4-nonneo
    # 40X: 0-nolabel, 1-neo, 2-inflam, 3-connec, 4-dead, 5-nonneo
    # neo>=10, 6<=inflam<=15
    for i in range(len(mod_loc)):
        x = int(mod_loc[i][0]-1)
        y = int(mod_loc[i][1]-1)
        if x < shape[1] and y < shape[0] and x >= 0 and y >=0:
            if tissue_mask[y, x]:
                if cellType[i] == 0:
                    main_array[y, x] += 1
                    main_neo[y, x] += 1
                elif cellType[i] == 1:
                    main_array[y, x] += 1
                    main_inflam[y, x] += 1
                elif cellType[i] == 2:
                    main_array[y, x] += 1
                    main_connec[y, x] += 1
                elif cellType[i] == 4:
                    main_array[y, x] += 1
                    main_epi[y, x] += 1
                else:
                    # exclude dead cells or no-label
                    main_dead[y, x] += 1
                    pass
            else:
                pass
        else:
            pass


    # return neo_diameters, inflam_diameters
    return main_array, main_neo, main_inflam, main_connec, main_epi, main_dead

def genHoverCellMatrix_40X(mod_loc, mask, cellType, diameterList):
    """
    :param mod_loc: the list of contour polygons representing the mode value for each cell
    :param mask_path: the tumor-til mask path
    :param cellType: [5 types] neoplastic, inflammatory, connective, necrosis, and non-neoplastic
    :return: *typeTumor_matrix, *typeLymph_matrix, *typeTILs_matrix
    """


    mask = np.array(mask)
    shape = mask.shape[:2]

    # Pre-allocate matrices
    main_array = np.full(shape, np.nan)
    main_neo = np.full(shape, np.nan)
    main_inflam = np.full(shape, np.nan)
    main_connec = np.full(shape, np.nan)
    main_dead = np.full(shape, np.nan)
    main_epi = np.full(shape, np.nan)

    # Define valid mask colors
    valid_mask_colors = np.array([[192, 192, 192], [255, 255, 0], [255, 0, 0], [255, 128, 0], [200, 0, 0]])

    # Create mask for valid tissue regions
    tissue_mask = np.any(np.all(mask[:, :, None] == valid_mask_colors, axis=-1), axis=-1)

    # Initialize matrices where mask is valid
    main_array[tissue_mask] = 0
    main_neo[tissue_mask] = 0
    main_inflam[tissue_mask] = 0
    main_connec[tissue_mask] = 0
    main_dead[tissue_mask] = 0
    main_epi[tissue_mask] = 0
    # 20X: 0-neo, 1-inflam, 2-connec, 3-dead, 4-nonneo
    # 40X: 0-nolabel, 1-neo, 2-inflam, 3-connec, 4-dead, 5-nonneo
    # neo>=10, 6<=inflam<=15
    for i in range(len(mod_loc)):
        x = int(mod_loc[i][0]-1)
        y = int(mod_loc[i][1]-1)
        if x < shape[1] and y < shape[0] and x >= 0 and y >=0:
            if tissue_mask[y, x]:
                if cellType[i] == 1:
                    main_array[y, x] += 1
                    main_neo[y, x] += 1
                elif cellType[i] == 2:
                    main_array[y, x] += 1
                    main_inflam[y, x] += 1
                elif cellType[i] == 3:
                    main_array[y, x] += 1
                    main_connec[y, x] += 1
                elif cellType[i] == 5:
                    main_array[y, x] += 1
                    main_epi[y, x] += 1
                else:
                    # exclude dead cells or no-label
                    main_dead[y, x] += 1
                    pass
            else:
                pass
        else:
            pass

    return main_array, main_neo, main_inflam, main_connec, main_epi, main_dead