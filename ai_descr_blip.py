from io import BytesIO

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

"""
Using BLIP model from Salesforce - currently one of the best for image captioning
"""
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def describe_blip(flo):
    bytes_io = BytesIO(flo.read())
    image = Image.open(bytes_io)

    # Process image
    inputs = processor(image, return_tensors="pt")

    # Generate caption
    output_ids = model.generate(
        **inputs,
        max_length=50,
        num_beams=5,
        early_stopping=True
    )

    description = processor.decode(output_ids[0], skip_special_tokens=True)
    return description
