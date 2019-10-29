define o = Character("Old Lady")
image m = "images/map/exmap.png"
image mr = "images/map/exmaprec.png"
# The game starts here.
label start:
    call screen myFirstScreen
    
label rectangle:
    show m 
    "this is a rectangle"
    call screen myFirstScreen
label pyramid:
    show m
    "this is a pyramid"
    call screen myFirstScreen
label weirdshape:
    show m
    "this is a weird shape."
    call screen myFirstScreen
    
    return
