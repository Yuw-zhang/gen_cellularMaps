from utils import *

arr_dir = 'read/hovernet_20x_array'
out_dir = 'read_tumorTIL'

def genMatrix(arr_data, cType):
    rgb_matrix = np.full((arr_data.shape[0], arr_data.shape[1], 3), [255, 255, 255], dtype=np.uint8)
    if cType == 'neo':
        rgb_matrix[arr_data>= 1] = [255, 255, 0]
        rgb_matrix[arr_data<1] = [192, 192, 192]
    elif cType == 'inflam':
        rgb_matrix[arr_data>=2] = [200, 0, 0]
        rgb_matrix[arr_data<2] = [192, 192, 192]
    
    return rgb_matrix

def genTIL(tumor, lym):
    TILmatrix = np.copy(tumor)
    for i in range(tumor.shape[0]):
        for j in range(tumor.shape[1]):
            if np.all(tumor[i, j]==[255, 255, 0], axis=-1) & np.all(lym[i, j]==[200, 0, 0], axis=-1):
                TILmatrix[i, j] = [255, 0, 0]
            elif np.all(tumor[i, j] !=[255, 255, 0], axis=-1) & np.all(lym[i, j]==[200, 0, 0], axis=-1):
                TILmatrix[i, j] = [200, 0, 0]
    
    return TILmatrix

if __name__ == '__main__':
    
    for i in os.listdir(arr_dir):
        os.makedirs(out_dir, exist_ok=True)
        #os.makedirs(os.path.join(out_dir, i), exist_ok=True)
        print(i)
        neo_arr = loadtxt(os.path.join(arr_dir, i, 'main_neopla.csv'), delimiter=' ')
        inflam_arr = loadtxt(os.path.join(arr_dir, i, 'main_inflam.csv'), delimiter=' ')
        
        tumor_matrix = genMatrix(neo_arr, 'neo')
        lym_matrix = genMatrix(inflam_arr, 'inflam')
        til_matrix = genTIL(tumor_matrix, lym_matrix)
        
        til = Image.fromarray(til_matrix, 'RGB')
        til.save(os.path.join(out_dir, i+'.png'))