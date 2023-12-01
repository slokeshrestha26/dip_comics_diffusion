from PIL import Image

def get_concat_h(ims):
    newwidth = 0
    for img in ims:
        newwidth += img.width + 10
    dst = Image.new('RGB', (newwidth-10, ims[0].height))
    for i, img in enumerate(ims):
        dst.paste(img, ((img.width+10)*i, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + 10 + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, 10+im1.height))
    return dst

def concatframes():

    frames = [0, 30, 60, 90, 120, 150, 180, 210, 239]
    inputframepath = 'data/down_x4_4k/turtles/'
    outputframepath = 'testoutput/turtles/'

    im = []
    for f in frames:
        img = Image.open(inputframepath+f'im{f+1:04d}.png')
        im.append(img)
    a = get_concat_h(im)

    im = []
    for f in frames:
        img = Image.open(outputframepath+f'{f}.png')
        im.append(img)
    b = get_concat_h(im)

    # get_concat_v(a, b).save('testoutput/videosample.jpg')
    a.save('testoutput/videosample1.jpg')
    b.save('testoutput/videosample2.jpg')

if __name__ == '__main__':
    concatframes()