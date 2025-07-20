from PIL import Image
import sys



# width = 4752
# height = 3168
#
# new_width = 2555
# new_height = 1703
#
# if width > height:
#     ratio = width / new_width
#     new_height = round(height / ratio)
#     print(round(ratio, 2))
# else:
#     ratio = height / new_height
#     new_width = round(width / ratio)
#     print(round(ratio, 2))


original_image_width = 4751
original_image_height = 3161

displayed_image_width = 1584
displayed_image_height = 1056

original_watermark_width = 610
original_watermark_height = 410

displayed_watermark_width = 1500
displayed_watermark_height = 1000

watermark_display_posX = 3500
watermark_display_posY = 2500


# watermark_original_posY = original_image_height * (watermark_display_posY / displayed_image_height)
# watermark_original_posX = original_image_width * (watermark_display_posX / displayed_image_width)
#
# watermark_final_width = (displayed_watermark_width / displayed_image_width) * original_image_width
# watermark_final_height = (displayed_watermark_height / displayed_image_height) * original_image_height

desired_image_width = original_image_width

width_ratio = displayed_image_width / desired_image_width

watermark_new_width = width_ratio * displayed_watermark_width
watermark_new_height = width_ratio * displayed_watermark_height

watermark_new_positionX =  watermark_display_posX
watermark_new_positionY =  watermark_display_posY

file = "C:\\Users\\fresh\\Desktop\\repos\\easywatermark\\images\\_MG_1930.jpg"
working_image = Image.open(file)

watermark_file = "C:\\Users\\fresh\\Desktop\\repos\\easywatermark\\images\\logo.png"
watermark = Image.open(watermark_file)

# Resize the watermark correctly
watermark = watermark.resize((round(watermark_new_width), round(watermark_new_height)), Image.Resampling.NEAREST)

# Create base with same size as working image
base = Image.new("RGBA", working_image.size, (255, 255, 255, 0))
base.paste(working_image.convert("RGBA"))  # Convert to RGBA for compositing

print(watermark_new_positionX, watermark_new_positionY)
print(watermark_new_width, watermark_new_height)

# Paste resized watermark and set position
base.paste(watermark, (round(watermark_new_positionX), round(watermark_new_positionY)), mask=watermark)

# Save the result
base.save("C:\\Users\\fresh\\Desktop\\repos\\EasyWaterMark\\images\\resized\\result.png")


# print(round(watermark_original_posY))
# print(round(watermark_original_posX))
#
# print(round(watermark_final_width))
# print(round(watermark_final_height))



