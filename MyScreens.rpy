image exmap:
    "images/map/exmap.png"
image arectangle:
    "images/map/exmaprec.png"

        
screen myFirstScreen():
    imagemap:
        ground "images/map/exmap.png"
        hover  "images/map/exmap.png" 
        hotspot(956, 60, 151, 364) action Jump("rectangle") hovered ShowTransient("frectangle", arectangle="images/map/exmaprec.png") unhovered Hide("frectangle")
        hotspot(606, 412, 224, 198) action Jump("pyramid") hovered ShowTransient("fpyramid", apyramid="images/map/exmappyr.png") unhovered Hide("fpyramid")
        hotspot(94, 416, 179, 238) action Jump("weirdshape")hovered ShowTransient("fshape", ashape="images/map/exmapcube.png") unhovered Hide("fshape")
        
screen frectangle(arectangle):
    add "images/map/exmaprec.png" xalign 1.0 yalign 0.0
screen fshape(ashape):
    add "images/map/exmapcube.png" xalign 1.0 yalign 0.0
screen fpyramid(apyramid):
    add "images/map/exmappyr.png" xalign 1.0 yalign 0.0

    