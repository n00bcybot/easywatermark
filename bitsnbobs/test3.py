
width = 4752
height = 3168

new_width = 2555
new_height = 1703

if width > height:
    ratio = width / new_width
    new_height = round(height / ratio)
    print(round(ratio, 2))
else:
    ratio = height / new_height
    new_width = round(width / ratio)
    print(round(ratio, 2))

