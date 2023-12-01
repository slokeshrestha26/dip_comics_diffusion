import torch
import numpy as np
from PIL import Image, ImageFilter
from diffusers import StableDiffusionImg2ImgPipeline
import os

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

imgfile = 'taytay.jpg'
img = Image.open(os.path.join("testinput", imgfile))

img = img.resize(tuple(x//4 for x in img.size), Image.Resampling.LANCZOS)

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
    img = img_h
    img = Image.fromarray(img)
elif edgeoperator == 'laplacian':
    outer = (0, 1, 0, 1, -4, 1, 0, 1, 0)
    inner = tuple(-x for x in outer)
    img_o = img.filter(ImageFilter.Kernel((3, 3), outer, 1, 0))
    img_i = img.filter(ImageFilter.Kernel((3, 3), inner, 1, 0))
    img_o.save('s1.png')
    img_i.save('s2.png')
    img_o = np.array(img_o)
    img_i = np.array(img_i)
    img = np.max([img_o, img_i], axis=0)
    img = Image.fromarray(img)
    img.save('s3.png')
elif edgeoperator == "g4g":
    filt = (-1, -1, -1, -1, 8, -1, -1, -1, -1)
    img = img.filter(ImageFilter.Kernel((3, 3), filt, 1, 0))

# Generalized dilate opertion
for i in range(3):
    img = img.filter(ImageFilter.MaxFilter(3))

img = 255-np.array(img)
img = Image.fromarray(img)
img = img.convert('RGB')
img.save('sampleedge.png')

print(img.size)

prompt = 'image of singer musician taylor swift wearing a black dress'
prompt += ' in the style of CNH3000'
generator = torch.Generator(device=device).manual_seed(1024)
image = pipe(prompt=prompt, image=img, strength=0.5, guidance_scale=7.5, generator=generator).images[0]
image.save(os.path.join("testoutput",'taytay_.png'))

print(image.size)