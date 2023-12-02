# DIP final project

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

![Dog](samples/txt2img/dog_before.png?raw=True "Happy dog in a car")
![Dog in Calvin and Hobbes style](samples/txt2img/dog_after.png?raw=True "Happy dog in a car in Calvin and Hobbes style")

![Policeman](samples/txt2img/police_before.png?raw=True "Policeman")
![Policeman in Calvin and Hobbes style](samples/txt2img/police_after.png?raw=True "Policeman in Calvin and Hobbes style")

![Girl](samples/txt2img/girl_before.png?raw=True "Girl with a balloon")
![Girl in Calvin and Hobbes style](samples/txt2img/girl_after.png?raw=True "Girl with a balloon in Calvin and Hobbes style")


### Image to Image Samples

![Bovik](samples/bovik/bovik_input.png?raw=True "Input image of Bovik")
![Bovik in Calvin and Hobbes style](samples/bovik/bovik_3.png?raw=True "Bovik in Calvin and Hobbes style")

![Jay Hartzell](samples/jay/jay_input.png?raw=True "Input image of Jay Hartzell")
![Jay Hartzell in Calvin and Hobbes style](samples/jay/jay_4.png?raw=True "Jay Hartzell in Calvin and Hobbes style")

![Bevo](samples/bevo/bevo_input.png?raw=True "Input image of Bevo")
![Bevo in Calvin and Hobbes style](samples/bevo/bevo_3.png?raw=True "Bevo in Calvin and Hobbes style")

### Image to Image Samples with edge input

![Bovik](samples/bovik/bovik_input.png?raw=True "Input image of Bovik")
![Edge map input of Bovik](samples/bovik/bovik_edge.png?raw=True "Edge map input of Bovik")
![Bovik in Calvin and Hobbes style](samples/bovik/bovik_edge_cnh.png?raw=True "Bovik in Calvin and Hobbes style")

![Taylor Swift](samples/taylor/taylor_input.png?raw=True "Input image of Taylor Swift")
![Edge map input of Taylor Swift](samples/taylor/taylor_edge.png?raw=True "Edge map input of Taylor Swift")
![Taylor Swift in Calvin and Hobbes style](samples/taylor/taylor_edge_cnh.png?raw=True "Taylor Swift in Calvin and Hobbes style")