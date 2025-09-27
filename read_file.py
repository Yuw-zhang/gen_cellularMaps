from utils import *

def read_hover_cell(f_path):
    """
    :param f_path: hovernet feature path, txt file
    :return: contour polygons and class
    """

    hovernet_df = pd.read_csv(f_path)
    return hovernet_df['contour'].tolist(), hovernet_df['type'], hovernet_df['diameter']

