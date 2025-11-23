from io import BytesIO

from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM

"""
Using BLIP-2 model - state-of-the-art but requires more computational resources
"""
processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = AutoModelForCausalLM.from_pretrained("Salesforce/blip2-opt-2.7b")

def describe_blip2(flo):


    bytes_io = BytesIO(flo.read())
    image = Image.open(bytes_io)

    inputs = processor(image, return_tensors="pt")

    generated_ids = model.generate(
        **inputs,
        max_length=50,
        num_beams=5,
        early_stopping=True
    )

    description = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    return description
