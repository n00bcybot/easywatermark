
width = 4752
height = 3168

new_width = 2328
new_height = int

if width > height:
    ratio = width / new_width
    new_height = round(height / ratio)
    print(ratio)
else:
    ratio = height / new_height
    new_width = round(width / ratio)
    print(ratio)

