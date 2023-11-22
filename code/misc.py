import os
import shutil
import pandas as pd
from glob import glob
from PIL import Image
import numpy as np
from tqdm import tqdm
import contextlib
import joblib

@contextlib.contextmanager
def tqdm_joblib(tqdm_object):
    """Context manager to patch joblib to report into tqdm progress bar given as argument"""
    class TqdmBatchCompletionCallback(joblib.parallel.BatchCompletionCallBack):
        def __call__(self, *args, **kwargs):
            tqdm_object.update(n=self.batch_size)
            return super().__call__(*args, **kwargs)

    old_batch_callback = joblib.parallel.BatchCompletionCallBack
    joblib.parallel.BatchCompletionCallBack = TqdmBatchCompletionCallback
    try:
        yield tqdm_object
    finally:
        joblib.parallel.BatchCompletionCallBack = old_batch_callback
        tqdm_object.close()

def moveimgs():
    os.makedirs('data/comics/all', exist_ok=True)
    ctr = 0
    for part in range(1,12):
        list = os.listdir(f'data/comics/Part{part:02d}')
        for j in list:
            oldname = os.path.join(f'data/comics/Part{part:02d}', j)
            newname = os.path.join(f'data/comics/all', f'{ctr:04d}.png')
            shutil.move(oldname, newname)
            ctr+=1

def makemetadata():
    filenames = glob('data/comics/all/*.png')
    filenames = [x.split(os.sep)[-1] for x in filenames]
    textprompts = len(filenames) * ["CNH3000"]
    dct = {'file_name': filenames, 'additional_feature': textprompts}
    df = pd.DataFrame(dct)
    df.to_csv('data/comics/all/metadata.csv', index=False)


def classifysingleimage(file):
    img = np.asarray(Image.open(file), dtype=np.int16)
    a = np.abs(img[:,:,0]-img[:,:,1])
    b = np.abs(img[:,:,1]-img[:,:,2])
    if np.all(a<10) and np.all(b<10):
        cat = 'bnw'
    else:
        cat = 'color'
    parts = file.split(os.sep)
    oldloc = file
    newloc = os.path.join(*parts[:-1], cat, parts[-1])
    shutil.move(oldloc, newloc)

def classifycolorimages(folder='data/comics/sample/*.png'):
    filenames = glob(folder)
    # filenames = [x.split(os.sep)[-1] for x in filenames]
    filenames = sorted(filenames)
    if len(filenames) == 0:
        print("Folder is empty")

    base = os.sep.join(filenames[0].split(os.sep)[:-1])
    os.makedirs(os.path.join(base, 'bnw'), exist_ok=True)
    os.makedirs(os.path.join(base, 'color'), exist_ok=True)

    with tqdm_joblib(tqdm(desc="Classifying based on color", total=len(filenames))):
        joblib.Parallel(n_jobs=100)(joblib.delayed(classifysingleimage)(file) for file in filenames)
    return

def crop_image(input_image_path, output_image_path, c):
    # Unpack coordinates
    x1, y1, x2, y2 = c

    # Open the image
    img = Image.open(input_image_path)

    # Crop the image using the coordinates
    cropped_img = img.crop((x1, y1, x2, y2))

    # Save the cropped image
    cropped_img.save(output_image_path)

def extractpanels(folder):

    os.makedirs(folder+'_crop', exist_ok=True)
    
    filenames = glob(os.path.join(folder, '*.png'))
    filenames = [x.split(os.sep)[-1] for x in filenames]
    filenames = sorted(filenames)

    input_path = lambda x: os.path.join(folder, x)
    output_path = lambda f, x: os.path.join(folder+'_crop', f"{f.split('.')[0]}_{x}.png")

    # Set your coordinates
    coordinates = [(235, 51, 758, 730), (807, 53, 1320, 731), (1354, 52, 1866, 731), (1911, 52, 2434, 731),
                    (235, 925, 761, 1601), (807, 925, 1320, 1601), (1354, 925, 1866, 1601), (1911, 925, 2434, 1601)]

    with tqdm_joblib(tqdm(desc="Croppping Images", total=len(filenames)*8)):
        joblib.Parallel(n_jobs=100)(joblib.delayed(crop_image)(input_path(file), output_path(file, i), c) for file in filenames for i, c in enumerate(coordinates))

if __name__ == '__main__':
    # moveimgs()
    # makemetadata()
    # classifycolorimages('data/comics/all/*.png')
    extractpanels('data/comics/split/bnw')
    pass