from utils import *

def densityMap(denseArray, out):
    #denseArray.astype('float')
    min = np.nanmin(denseArray)
    max = np.nanmax(denseArray)
    #mean_value = np.nanmean(denseArray)
    #denseArray = (denseArray - min) / (max - min)
    masked_array = np.ma.array(denseArray, mask=np.isnan(denseArray))
    #masked_array = np.ma.masked_where(denseArray==0, denseArray)
    cmap = plt.cm.jet
    cmap.set_bad('white', 1.)
    cmap.set_under('lightgray')
    ax = plt.subplot()
    im = ax.imshow(masked_array, cmap=cmap, vmin=1)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='3%', pad=0.05)
    cb = plt.colorbar(im, cax=cax)
    cb.set_ticks([1, max])
    ax.axis('off')
    # plt.axis('off')
    plt.savefig(out)
    plt.clf()