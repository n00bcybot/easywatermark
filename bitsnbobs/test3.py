from PIL import Image
import sys

# Testing results with rendering preview and final result

# Load files
file = "C:\\Users\\fresh\\Desktop\\repos\\EasyWaterMark\\images\\_MG_4068.jpg"
watermark_file = "C:\\Users\\fresh\\Desktop\\repos\\EasyWaterMark\\images\\logo.png"

original_image_width = 4751
original_image_height = 3161

original_watermark_width = 649
original_watermark_height = 270

# -----------------------------------
# Dimensions of the image as seen in the image display (image_display.py)
preview_image_width = 1584
preview_image_height = 1056

# Dimensions of the watermark as seen in the watermark custom label (watermark_label)
preview_watermark_width = 150
preview_watermark_height = 100

# Watermark's position in watermark_label
preview_watermark_posX = 1000
preview_watermark_posY = 650

# -----------------------------------
# Desired final image size, this should be set by the user via the interface
desired_image_width = 1200  # preview_image_width
desired_image_height = 800  # preview_image_height

# watermark_original_posY = original_image_height * (watermark_display_posY / displayed_image_height)
# watermark_original_posX = original_image_width * (watermark_display_posX / displayed_image_width)
#
# watermark_final_width = (displayed_watermark_width / displayed_image_width) * original_image_width
# watermark_final_height = (displayed_watermark_height / displayed_image_height) * original_image_height


ratio = desired_image_width / preview_image_width

watermark_new_width = round(ratio * preview_watermark_width)
watermark_new_height = round(ratio * preview_watermark_height)

watermark_new_positionX = round(ratio * preview_watermark_posX)
watermark_new_positionY = round(ratio * preview_watermark_posY)

# Create preview
# ----------------------------------------------------------------------------------------------------------------------
preview_image = Image.open(file)
preview_image.thumbnail((preview_image_width, preview_image_height))
preview_watermark = Image.open(watermark_file)
preview_watermark.thumbnail((preview_watermark_width, preview_watermark_height))

preview_canvas = Image.new("RGBA", (preview_image_width, preview_image_height), (255, 255, 255, 0))
preview_canvas.paste(preview_image.convert("RGBA"))  # Convert to RGBA for compositing
preview_canvas.paste(preview_watermark, (round(preview_watermark_posX), round(preview_watermark_posY)), mask=preview_watermark)
preview_canvas.save("C:\\Users\\fresh\\Desktop\\repos\\EasyWaterMark\\images\\resized\\preview.png")

# End preview
# ----------------------------------------------------------------------------------------------------------------------

# Open the image and the watermark and resize to desired dimensions
working_image = Image.open(file)
working_image.thumbnail((desired_image_width, desired_image_height), Image.Resampling.NEAREST)
watermark = Image.open(watermark_file)
watermark.thumbnail((watermark_new_width, watermark_new_height))

# Alternatively, account for changing the aspect ratio
# if aspect_ratio:
#     working_image.thumbnail((desired_image_width, desired_image_height), Image.Resampling.NEAREST)
# else:
#     working_image = working_image.resize((desired_image_width, desired_image_height), Image.Resampling.LANCZOS)

# Create base layer with same size as working image desired size
canvas = Image.new("RGBA", (desired_image_width, desired_image_height), (255, 255, 255, 0))
canvas.paste(working_image.convert("RGBA"))  # Convert to RGBA for compositing and paste into the canvas

# Paste resized watermark and set position
canvas.paste(watermark, (round(watermark_new_positionX), round(watermark_new_positionY)), mask=watermark)

# Save the result
canvas.save("C:\\Users\\fresh\\Desktop\\repos\\EasyWaterMark\\images\\resized\\result.png")

# print(desired_image_width)
# print(watermark_new_positionX, watermark_new_positionY)
# print(watermark_new_width, watermark_new_height)

