import os
import shutil

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



if __name__ == '__main__':
    moveimgs()