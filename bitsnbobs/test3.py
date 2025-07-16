#
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

original_watermark_width = 61
original_watermark_height = 41

displayed_watermark_width = 75
displayed_watermark_height = 50

watermark_display_posX = 50
watermark_display_posY = 50


watermark_original_posY = original_image_height * (watermark_display_posY / displayed_image_height)
watermark_original_posX = original_image_width * (watermark_display_posX / displayed_image_width)

watermark_final_width = (displayed_watermark_width / displayed_image_width) * original_image_width
watermark_final_height = (displayed_watermark_height / displayed_image_height) * original_image_height

print(round(watermark_original_posY))
print(round(watermark_original_posX))

print(round(watermark_final_width))
print(round(watermark_final_height))







