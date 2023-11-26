import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

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

cnhstyle = lambda text: text + " CNH3000"

# text = "A singer performing on a sidewalk CNH 3000"
# image = pipe(cnhstyle(text), num_inference_steps=25, guidance_scale=7.5, cross_attention_kwargs={"scale": 0.5}).images[0]
# image.save("testoutput/singer_lora_50.png")

# text = "A singer performing on a sidewalk CNH 3000"
# image = pipe(cnhstyle(text), num_inference_steps=25, guidance_scale=7.5).images[0]
# image.save("testoutput/singer_lora_100.png")

# text = "A policeman saying 'the area is closed' next to a stop sign"
# image = pipe(cnhstyle(text), num_inference_steps=25, guidance_scale=7.5).images[0]
# image.save("testoutput/police_lora_100.png")

text = "A dancer next to a stop sign"
image = pipe(cnhstyle(text), num_inference_steps=25, guidance_scale=7.5).images[0]
image.save("testoutput/dancer_lora_100.png")
