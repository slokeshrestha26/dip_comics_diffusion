# DIP final project

## To Dos:
- [X] Find the peanuts model (https://civitai.com/models/17361/peanuts-comics-art-style)
- [X] Setup TACC
- [X] Get the calvin and hobbes dataset
- [X] Go through the diffusion model course (Sharon Zhou)
- [ ] Debug the LoRA collab notebook
- [ ] Read the HuggingFace LoRA implementation API
- [ ] Read blogs on diffusion model fine tuning
  - [ ] Civitai Wiki: https://github.com/civitai/civitai/wiki/How-to-use-models
  - [ ] Blog 2:
     

## Calvin & Hobbes Dataset

## Blogs of Interest
## Plan

So, here's what HuggingFace did for a the ghibli LoRA example.
* They took a txt2img ghibli diffusion model. 
* Passed it through an img2img pipeline. 
* Got outputs. 

We're gonna do something very similar. 
* We're gonna fine-tune a txt2img LoRA model for calvin and hobbes. 
* We're gonna plug that into an img2img pipeline.
* We're gonna use [controlnet](https://huggingface.co/docs/diffusers/v0.21.0/en/using-diffusers/controlnet) to create masks/edges of the an input image.
* We're gonna get outputs.

### Experiments to try

1. LoRA  
2. DreamBooth  
3. Textual Inversion
4. Fine-tune existing cartoonifier [checkpoint](https://civitai.com/models/17368/pseudo-peanuts-cartoonifier-art-style)  
5. Increasing training input size
6. Inference - jay hartzell, bevo, taylor swift, mona lisa and other famous paintings

### Keyword conditioning
1. https://octoml.ai/blog/the-beginners-guide-to-fine-tuning-stable-diffusion/ What's dreambooth, textual inversion and lora? Which one do we want to use?

### Finetuning on dataset
1. Pokemon finetuning example: https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning  
CUB Dataset: https://paperswithcode.com/dataset/cub-200-2011  
CUB Dataset: https://huggingface.co/datasets/alkzar90/CC6204-Hackaton-Cub-Dataset/viewer/default/test

2. Huggingface:  
* a. Start here: https://huggingface.co/docs/diffusers/index  
    i. Ctrl+F for "Image-to-Image Text-Guided Generation" on https://huggingface.co/docs/diffusers/v0.21.0/en/index  
* b. LoRA: https://huggingface.co/docs/diffusers/training/lora  
* c. Training Examples: https://huggingface.co/docs/diffusers/training/overview  
* d. Controlnet: https://huggingface.co/docs/diffusers/v0.21.0/en/using-diffusers/controlnet  
* e. Text2Img: https://huggingface.co/docs/diffusers/training/text2image  

Ctrl+F for "Image-to-Image Text-Guided Generation" on https://huggingface.co/docs/diffusers/v0.21.0/en/index

DreamBooth training examples:  
1. https://github.com/nitrosocke/dreambooth-training-guide
2. https://huggingface.co/docs/diffusers/training/dreambooth

Textual Inversion examples:
1. https://huggingface.co/docs/diffusers/training/text_inversion
2. https://huggingface.co/docs/diffusers/using-diffusers/textual_inversion_inference

LoRA training training examples:
1. cloneofsimo script
2. https://huggingface.co/docs/diffusers/training/lora#texttoimage
3. (Example) https://huggingface.co/docs/diffusers/v0.21.0/en/using-diffusers/img2img

## Log into TACC
`ssh asvin@ls6.tacc.utexas.edu`  
LuckyMonkey!!  
\< Get TACC Code from Asvin \>

TACC has three main directories, 
1. /home/
2. /work/
3. /scratch/

Use /home just as a login landing page. Don't save much here. 

Use /work to put all code. Create a folder for our project here.

Use /scratch for saving datasets. If data saved here is not modified/accessed once in every 2 weeks it'll get deleted.

Use command `cdw` to go to the /work directory.
Use command `cds` to go the /scratch directory.
You can also do `cdw folder-name` to directly navigate to that folder in /work. This format works for /scratch too.

Ask for a compute node using the following command:
`idev -N 1 -p gpu-a100 -m 30:00`
Use `-p normal` if you don't need GPUs.  
Use `-m 60:00` if you want it for 60 mins or `-t 1:0:0` if you want it for 2 hours.  
Use `-N 2` if you need 2 nodes instead.  

Sharan's command is:
`srun --gres=gpu:2 -c 32 -m 32 --pty /bin/bash`

Use the virtual env at `dipenv/`
Use the following command to activate: `source dipenv/bin/activate`

## Calvin & Hobbes Dataset

- [X] Find a calvin and hobbes dataset
- [X] Download it
- [X] Extract images
- [ ] Select only the black and white panels
- [ ] Crop panels

## Blogs of Interest
### Keyword conditioning
1. https://octoml.ai/blog/the-beginners-guide-to-fine-tuning-stable-diffusion/ What's dreambooth, textual inversion and lora? Which one do we want to use?
### Finetuning on dataset
1. Pokemon finetuning example: https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning  
CUB Dataset: https://paperswithcode.com/dataset/cub-200-2011  
CUB Dataset: https://huggingface.co/datasets/alkzar90/CC6204-Hackaton-Cub-Dataset/viewer/default/test
2. Huggingface:
Start here: https://huggingface.co/docs/diffusers/index  
LoRA: https://huggingface.co/docs/diffusers/training/lora
Training Examples: https://huggingface.co/docs/diffusers/training/overview  
Controlnet: https://huggingface.co/docs/diffusers/v0.21.0/en/using-diffusers/controlnet  
Text2Img: https://huggingface.co/docs/diffusers/training/text2image

