from pathlib import Path
from PIL import Image, ImageOps
from pdf2image import convert_from_path


def preproccesing(path_to_document: str,
                  max_pixels: int
                  ) -> [Image]:
    ...
    for _, page in enumerate(pages):
        # corrects the image orientation
        page = ImageOps.exif_transpose(page)

        if page.width * page.height > max_pixels:
            scale_factor = (max_pixels / (page.width * page.height)) ** 0.5

            new_width = int(page.width * scale_factor)
            new_height = int(page.height * scale_factor)

            page = page.resize((new_width, new_height),
                               Image.Resampling.LANCZOS)

    ...
