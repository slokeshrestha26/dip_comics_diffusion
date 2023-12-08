# [Style Transfer Using Stable Diffusion] (http://arxiv.org/abs/2312.03993)

> Contributors: [Asvin Venkataramanan](https://github.com/asvin-kumar), [Sloke Shrestha](https://github.com/slokeshrestha26), [Sundar Sripada V.S.](https://github.com/ss26)

> We won the EE 371Q Digital Image Processing Ram’s Horn best project award!! EE 371Q is a famous class taught by [Prof. Alan Bovik](https://www.ece.utexas.edu/people/faculty/alan-bovik) at University of Texas at Austin

> Video presentation available at:

[![YouTube](https://img.youtube.com/vi/kMGjOr974vE/0.jpg)](https://www.youtube.com/watch?v=kMGjOr974vE)

## Code

This code base was used to implement the final project for the course EE371Q Digital Image Processing. 

We used this code base to fine-tune a Diffusion model using the LoRA technique to convert images into the style of Calvin and Hobbes comics. 
Here's a brief overview of the files. 

* code/get_cnh_dataset.ipynb and code/get_cnh_dataset.py were used to download files from the Internet Archive and create the dataset. 
* code/lora_example.sh and code/train_text_to_image_lora.py were used to fine-tune the diffusion model.
* code/infer.py, code/infertext.py, code/infervideo.py were used to generate samples with the fine-tuned model.
* code/utils.py and code/utils_slides.py were used for miscellaneous tasks. 
* environment.yml has the packages required to run this code.

## Samples

### Text to Image Samples

Generated samples before and after fine-tuning. 

<img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/txt2img/dog_before.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/txt2img/police_before.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/txt2img/girl_before.png" width="256" />

<img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/txt2img/dog_after.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/txt2img/police_after.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/txt2img/girl_after.png" width="256" />


### Image to Image Samples

<img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/bovik/bovik_input.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/bovik/bovik_3.png" width="256" />

<img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/jay/jay_input.jpg" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/jay/jay_4.png" width="256" />

<img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/bevo/bevo_input.jpg" width="256" />  <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/bevo/bevo_3.png" width="256" />


### Image to Image Samples with Edge Input


<img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/bovik/bovik_3.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/bovik/bovik_edge.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/bovik/bovik_edge_cnh.png" width="256" />

<img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/taylor/taylor_input.jpg" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/taylor/taylor_edge.png" width="256" /> <img src="https://github.com/slokeshrestha26/dip_comics_diffusion/blob/main/samples/taylor/taylor_edge_cnh.png" width="256" />
