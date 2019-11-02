init:
    default shape = 1
image p = "images/phone[shape].png"

screen Phone():
    imagemap:
        ground "images/exphone.png"
        hotspot(460, 315, 88, 94) action If(shape == 1, SetVariable("shape", 4), SetVariable("shape", shape - 1))
            #if shape <1:
             #   shape = 4
        hotspot(761, 324, 73, 69) action If(shape == 4, SetVariable("shape", 1), SetVariable("shape", shape + 1))
           # if shape >4:
            #    shape = 1
    add "p"
    
label start:
    show p
    call screen Phone
    

    return
