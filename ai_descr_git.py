from io import BytesIO

from PIL import Image
from transformers import GitProcessor, GitForCausalLM

"""
Using GIT model from Microsoft
"""
processor = GitProcessor.from_pretrained("microsoft/git-base-coco")
model = GitForCausalLM.from_pretrained("microsoft/git-base-coco")


def describe_git(flo):
    bytes_io = BytesIO(flo.read())
    image = Image.open(bytes_io)

    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    generated_ids = model.generate(
        pixel_values=pixel_values,
        max_length=50,
        num_beams=5,
        early_stopping=True
    )

    description = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return description
