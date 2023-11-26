export HUGGINGFACE_HUB_CACHE="/scratch/09175/asvin/.cache/huggingface/hub"
export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export OUTPUT_DIR="/scratch/09175/asvin/dip/cnh4"
export HUB_MODEL_ID="cnh4"
export DATASET_NAME="/work/09175/asvin/ls6/dip/data/split/bnw_crop"

CODEFOLDER="/work/09175/asvin/ls6/dip/code"

accelerate launch \
  --mixed_precision="fp16" \
  --num_processes=3 \
  --num_machines=1 \
  --dynamo_backend="no" \
  --multi_gpu \
  $CODEFOLDER/train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --train_data_dir=$DATASET_NAME \
  --dataloader_num_workers=8 \
  --resolution=512 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=30000 \
  --learning_rate=1e-04 \
  --max_grad_norm=1 \
  --lr_scheduler="cosine" --lr_warmup_steps=0 \
  --output_dir=${OUTPUT_DIR} \
  --push_to_hub \
  --hub_model_id=${HUB_MODEL_ID} \
  --report_to=wandb \
  --checkpointing_steps=500 \
  --validation_prompt="A dog in a car in the style of CNH3000." \
  --seed=1337 \
  --resume_from_checkpoint="latest" \
  --cache_dir="/scratch/09175/asvin/.cache/huggingface/hub" \

# export HUGGINGFACE_HUB_CACHE="/scratch/09175/asvin/.cache/huggingface/hub"
# export MODEL_NAME="/scratch/09175/asvin/dip/PeanutsStyle.safetensors"
# export OUTPUT_DIR="/scratch/09175/asvin/dip/cnh4"
# export HUB_MODEL_ID="cnh4"
# export DATASET_NAME="/work/09175/asvin/ls6/dip/data/comics/split/bnw_crop"

# CODEFOLDER="/work/09175/asvin/ls6/dip/code"

# accelerate launch \
#   --mixed_precision="fp16" \
#   --num_processes=3 \
#   --num_machines=1 \
#   --dynamo_backend="no" \
#   --multi_gpu \
#   $CODEFOLDER/train_text_to_image_lora.py \
#   --pretrained_model_name_or_path=$MODEL_NAME \
#   --train_data_dir=$DATASET_NAME \
#   --dataloader_num_workers=8 \
#   --resolution=512 --center_crop --random_flip \
#   --train_batch_size=1 \
#   --gradient_accumulation_steps=4 \
#   --max_train_steps=15000 \
#   --learning_rate=1e-04 \
#   --max_grad_norm=1 \
#   --lr_scheduler="cosine" --lr_warmup_steps=0 \
#   --output_dir=${OUTPUT_DIR} \
#   --push_to_hub \
#   --hub_model_id=${HUB_MODEL_ID} \
#   --report_to=wandb \
#   --checkpointing_steps=500 \
#   --validation_prompt="A dog in a car in the style of CNH3000." \
#   --seed=1337 \
#   --resume_from_checkpoint="latest" \
#   --cache_dir="/scratch/09175/asvin/.cache/huggingface/hub" \



