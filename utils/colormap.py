import imgviz


# Palette shared by the auto shape colors in the GUI (app.py) and the label
# PNG written by utils.lblsave(), so both display the same colors.
#
# The first entries of the imgviz colormap are overridden with a
# higher-contrast set: imgviz puts green (#008000) and olive (#808000) next to
# each other, which differ only in the red channel and are hard to tell apart,
# and its whole palette sits at the dark end of the range. The colors below
# stay mid-to-dark on purpose, since the annotated images are mostly white.
#
# label_colormap() is lru_cached and returns a read-only array shared by every
# caller, so copy it before overriding.
LABEL_COLORMAP = imgviz.label_colormap().copy()
LABEL_COLORMAP[:12] = [
    (0, 0, 0),  # 0: background, and unused as a shape color (ids start at 1)
    (230, 25, 75),  # 1: red
    (67, 99, 216),  # 2: blue
    (60, 180, 75),  # 3: green
    (255, 130, 48),  # 4: orange
    (145, 30, 180),  # 5: purple
    (0, 128, 128),  # 6: teal
    (240, 50, 230),  # 7: magenta
    (128, 128, 0),  # 8: olive
    (170, 110, 40),  # 9: brown
    (0, 0, 128),  # 10: navy
    (128, 0, 0),  # 11: maroon
]
