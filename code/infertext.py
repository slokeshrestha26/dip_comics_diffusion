import torch
import numpy as np
from PIL import Image, ImageFilter
from diffusers import StableDiffusionImg2ImgPipeline
import os
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler, StableDiffusionImg2ImgPipeline

### Text 2 Image

model_base = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_base, torch_dtype=torch.float16, use_safetensors=True,
    cache_dir="/scratch/09175/asvin/.cache/huggingface/hub",
    safety_checker=None,
    )
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

lora_model_path = '/scratch/09175/asvin/dip/cnh4'
pipe.unet.load_attn_procs(lora_model_path)
pipe.to("cuda")

cnhstyle = lambda text: text + " in the style of CNH3000"

# text = "A happy dog in car with it's head out of the window"
# image = pipe(cnhstyle(text), num_inference_steps=25, guidance_scale=7.5).images[0]
# image.save("testoutput/dog1.png")

# text = "A policeman at a traffic light on a busy street wearing a hat"
# image = pipe(cnhstyle(text), strength=0.5, guidance_scale=7.5, generator=torch.Generator(device='cuda').manual_seed(1024)).images[0]
# image.save("testoutput/police.png")

# text = "A little girl with a baloon walking down a street with buildings in the background"
# image = pipe(cnhstyle(text), strength=0.5, guidance_scale=7.5, generator=torch.Generator(device='cuda').manual_seed(1024)).images[0]
# image.save("testoutput/girl.png")

# text = ""
# image = pipe(cnhstyle(text), strength=0.5, guidance_scale=7.5, generator=torch.Generator(device='cuda').manual_seed(1024)).images[0]
# image.save("testoutput/picnic.png")