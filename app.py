import os
import sys
import time
from PIL import Image
import torch
import random

# ================== CONFIGURATION ==================

# Prompt for thermal image generation
base_prompt = (
    "Generate a thermal image of an industrial pipeline system in a factory environment. "
    "The thermal image should vividly display temperature zones using a clear and smooth heatmap style: "
    "Red zones represent the hottest areas, yellow zones are warm, green zones are moderate, and blue zones are the coolest. "
    "Maintain a realistic thermal imaging style with soft transitions between colors, avoiding hard edges."
)

# Paths
input_image_path = r"C:\Users\DELL\Desktop\SmartWork Hackathon\Thermal Image\frame1.jpg"
output_dir = r"C:\Users\DELL\Desktop\SmartWork Hackathon\OutputFrames"

# Model parameters
model_type = "flux-dev"
ref_size = 512
image_size = 512
steps = 30
guidance = 4.0
num_frames = 1  # Set to 1 to speed up testing

# ================== SYSTEM SETUP ==================

# Add UNO pipeline to path
sys.path.append(os.path.join(os.path.dirname(__file__), "uno"))

from uno.flux.pipeline import UNOPipeline, preprocess_ref

# Use GPU if available
use_cuda = torch.cuda.is_available()
device = "cuda" if use_cuda else "cpu"
print(f"🖥️  Using device: {device}")

# ================== LOAD REFERENCE IMAGE ==================

print("🖼️  Loading reference image...")
start_ref = time.time()

input_image = Image.open(input_image_path).convert("RGB")
ref_image = preprocess_ref(input_image, ref_size)

print(f"✅ Reference image loaded and preprocessed in {time.time() - start_ref:.2f}s")

# Ensure output folder exists
os.makedirs(output_dir, exist_ok=True)

# ================== LOAD MODEL ==================

print("🚀 Loading UNO pipeline...")
start_model = time.time()

pipeline = UNOPipeline(
    model_type=model_type,
    device=device,
    offload=False,
    only_lora=True,
    lora_rank=512
)

print(f"✅ UNO pipeline loaded in {time.time() - start_model:.2f}s")

# ================== PROMPT FLUCTUATION FUNCTION ==================

def fluctuate_prompt(base, frame_idx):
    variations = [
        "slightly increased red intensity with warmer yellow zones",
        "slightly decreased red intensity with cooler yellow zones",
        "moderate red zones with stable yellow and green areas",
        "intensified blue and green cooler zones",
        "soft transition between warm and cool zones"
    ]
    return base + " " + variations[frame_idx % len(variations)] + "."

# ================== GENERATE FRAMES ==================

print(f"🎬 Starting generation of {num_frames} frame(s)...")

for i in range(num_frames):
    current_seed = 1234 + i
    prompt = fluctuate_prompt(base_prompt, i)
    print(f"\n🖼️  Generating frame {i+1}/{num_frames}")
    print(f"📜 Prompt: {prompt}")
    print(f"🔢 Seed: {current_seed}")

    start_gen = time.time()

    result_image = pipeline(
        prompt=prompt,
        width=image_size,
        height=image_size,
        guidance=guidance,
        num_steps=steps,
        seed=current_seed,
        ref_imgs=[ref_image],
        pe="d",
    )

    elapsed = time.time() - start_gen
    print(f"✅ Frame generated in {elapsed:.2f}s")

    # Save the output image
    output_path = os.path.join(output_dir, f"thermal_frame_{i:03}.png")
    result_image.save(output_path)
    print(f"💾 Saved to: {output_path}")

print("\n✅ All frames generated and saved successfully.")
