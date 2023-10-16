# DIP final project

## To Dos:
- [X] Find the peanuts model (https://civitai.com/models/17361/peanuts-comics-art-style)
- [X] Setup TACC
- [X] Get the calvin and hobbes dataset
- [ ] Read blogs on diffusion model fine tuning
  - [ ] Civitai Wiki: https://github.com/civitai/civitai/wiki/How-to-use-models
  - [ ] Blog 2:
     
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

## Calvin & Hobbes Dataset


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
