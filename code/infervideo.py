import torch
import numpy as np
from PIL import Image, ImageFilter
from diffusers import StableDiffusionImg2ImgPipeline
from glob import glob
from tqdm import tqdm
from os.path import join, exists
import ffmpeg
import os


def resizeimg(img, k):
    img = img.resize(tuple(x//k for x in img.size), Image.Resampling.LANCZOS)
    return img

def edge(img):
    img = img.convert('L')

    edgeoperator = 'sobel'

    if edgeoperator == 'sobel':
        horz = (1, 0, -1, 2, 0, -2, 1, 0, -1)
        vert = (1, 2, 1, 0, 0, 0, -1, -2, -1)
        img_h = img.filter(ImageFilter.Kernel((3, 3), horz, 1, 0))
        img_v = img.filter(ImageFilter.Kernel((3, 3), vert, 1, 0))
        img_h.save('s1.png')
        img_v.save('s2.png')
        img_h = np.array(img_h)
        img_v = np.array(img_v)
        img = np.max([img_h, img_v], axis=0)
        img = Image.fromarray(img)
        img.save('s3.png')
        img = Image.fromarray(img_h) # TEST
    elif edgeoperator == 'laplacian':
        outer = (0, 1, 0, 1, -4, 1, 0, 1, 0)
        inner = tuple(-x for x in outer)
        img_o = img.filter(ImageFilter.Kernel((3, 3), outer, 1, 0))
        img_i = img.filter(ImageFilter.Kernel((3, 3), inner, 1, 0))
        # img_o.save('s1.png')
        # img_i.save('s2.png')
        img_o = np.array(img_o)
        img_i = np.array(img_i)
        img = np.max([img_o, img_i], axis=0)
        img = Image.fromarray(img)
        # img.save('s3.png')
    elif edgeoperator == "g4g":
        filt = (-1, -1, -1, -1, 8, -1, -1, -1, -1)
        img = img.filter(ImageFilter.Kernel((3, 3), filt, 1, 0))

    for _ in range(1):
        img = img.filter(ImageFilter.MaxFilter(3))

    img = 255-np.array(img)
    img = Image.fromarray(img)
    img = img.convert('RGB')
    # img.save('sampleedge.png')
    return img

def blurimg(img):
    img = img.filter(ImageFilter.GaussianBlur(5))
    return img

def processimage(img):
    # print(img.size)
    img = resizeimg(img, 2)
    # print(img.size)
    final = edge(img)
    final.save('sampleturtle.png')
    # final = edge(img) + blurimg(img)
    return final

def diffusioncall(img):
    modelname = "runwayml/stable-diffusion-v1-5"

    device = "cuda"
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        modelname, torch_dtype=torch.float16, use_safetensors=True,
        cache_dir="/scratch/09175/asvin/.cache/huggingface/hub",
        safety_checker=None,
    )

    lora_model_path = '/scratch/09175/asvin/dip/cnh4'
    pipe.unet.load_attn_procs(lora_model_path)
    pipe.to(device)

    prompt = 'underwater ocean floor with corals and a turtle and fishes' 
    prompt += 'in the style of CNH3000'
    generator = torch.Generator(device=device).manual_seed(1024)
    image = pipe(prompt=prompt, image=img, strength=0.6, guidance_scale=7.5, generator=generator).images[0]
    return image


if __name__ == '__main__':

    # quick test for video frames
    filelist = glob('data/down_x4_4k/turtles/*.png')
    outfolder = 'testoutput/turtles2'
    os.makedirs(outfolder, exist_ok=True)
    for i, f in enumerate(filelist):
        if i%5:
            continue
        img = Image.open(f)
        # img = processimage(img)
        output = diffusioncall(img)
        output.save(join(outfolder, f'{i}.png'))
        if i==50:
            break
    ffmpeg.input('testoutput/turtles2/%d.png', framerate=30).output('testoutput/turtles2/movie.mp4', '-y', loglevel='quiet').run()

