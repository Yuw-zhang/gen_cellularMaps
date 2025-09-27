from utils import *
from read_file import read_hover_cell
from preprocess_polygon import get_mag, norm_loc, mode_loc
from sum_cell import *
from densityHeatmap import densityMap

# downstream files
wsi_dir = '/data10/shared/tcga_all/read'
mask_dir = '/data09/shared/yuwei/read/masks/tumorTILs_upennModel'
suffix = '.png'

# segmentation files
hover_dir = '/data06/shared/yuwei/til_segmentation_analysis/predictionFile_process/read/40x_withDiameter'
mpp = 40
densityMap_out = 'read_map'
densityArray_out = 'read_array'

def genHover(hover_dir, wsi_dir, mask_dir, suffix, mpp, out_array, out_map):

    for seg_file in os.listdir(hover_dir):
        # extract the corresponding files
        caseid = seg_file.split('-01Z')[0]
        svs_name = seg_file + '.svs'
        mask_name = seg_file + suffix
        wsi_path = os.path.join(wsi_dir, svs_name)
        mask_path = os.path.join(mask_dir, mask_name)
        seg_path = os.path.join(hover_dir, seg_file)
        os.makedirs(out_array, exist_ok=True)
        os.makedirs(out_map, exist_ok=True)
        print(caseid)
        if seg_file not in os.listdir(out_map):
            if os.path.exists(wsi_path) and os.path.exists(mask_path):
                print('Executing ', seg_file)

                # Create output folder based on each case
                os.makedirs(os.path.join(out_map, seg_file), exist_ok=True)
                os.makedirs(os.path.join(out_array, seg_file), exist_ok=True)
                oslide = openslide.OpenSlide(wsi_path)
                mask = Image.open(mask_path)
                # contour polygon preprocess
                contour_polygons, cellType, diameterList = read_hover_cell(seg_path)
                mag = get_mag(oslide, mask)
                norm_polygons = norm_loc(contour_polygons, mag)
                mode_polygons = mode_loc(norm_polygons)

                # Generate cell matrix on tumor, lymph, and til mask
                if mpp == 20:
                    main_array, main_neo, main_inflam, main_connec, main_epi, main_dead = genHoverCellMatrix_20X(mode_polygons, mask, cellType, diameterList)
                elif mpp == 40:
                    main_array, main_neo, main_inflam, main_connec, main_epi, main_dead = genHoverCellMatrix_40X(mode_polygons, mask, cellType, diameterList)
                
                savetxt(os.path.join(out_array, seg_file, 'main.csv'), main_array, delimiter=' ')
                savetxt(os.path.join(out_array, seg_file, 'main_neopla.csv'), main_neo, delimiter=' ')
                savetxt(os.path.join(out_array, seg_file, 'main_inflam.csv'), main_inflam, delimiter=' ')
                savetxt(os.path.join(out_array, seg_file, 'main_connec.csv'), main_connec, delimiter=' ')
                savetxt(os.path.join(out_array, seg_file, 'main_epi.csv'), main_connec, delimiter=' ')
                savetxt(os.path.join(out_array, seg_file, 'main_dead.csv'), main_dead, delimiter=' ')

                # Output parameters preparation
                mainName = seg_file + '_main.png'
                mainNeo = seg_file + '_neopla.png'
                mainInflam = seg_file + '_inflam.png'
                mainConnec = seg_file + '_connec.png'
                mainEpi = seg_file + '_epi.png'
                # Generate density output
                densityMap(main_array, os.path.join(out_map, seg_file, mainName))
                densityMap(main_neo, os.path.join(out_map, seg_file, mainNeo))
                densityMap(main_inflam, os.path.join(out_map, seg_file, mainInflam))
                densityMap(main_connec, os.path.join(out_map, seg_file, mainConnec))
                densityMap(main_epi, os.path.join(out_map, seg_file, mainEpi))


if __name__ == '__main__':
    genHover(hover_dir, wsi_dir, mask_dir, suffix, mpp, densityArray_out, densityMap_out)
