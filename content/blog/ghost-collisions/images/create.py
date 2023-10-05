import math

import cairo

LW = 3.0

D2R = math.pi/180.0

def player(cr: cairo.Context, x: float, y: float, alpha=1.0):
    cr.set_line_width(LW)
    cr.set_source_rgba(1, 0.5, 0.5, 0.25*alpha)
    w, h = 60, 130
    cr.rectangle(x-w/2, y-h, w-LW, h-LW)
    cr.fill_preserve()
    cr.set_source_rgba(1, 0.5, 0.5, alpha)
    cr.stroke()

def capsule(cr: cairo.Context, x: float, y: float):
    r = 60/2
    h = 130-r*2
    cr.save()
    cr.translate(x, y-r)
    cr.arc_negative(0, 0, r, math.pi, 0)
    cr.rel_line_to(0, -h)
    cr.arc_negative(0, -h, r, 0, math.pi)
    cr.close_path()
    cr.set_source_rgba(1, 0.5, 0.5, 0.25)
    cr.fill_preserve()
    cr.set_source_rgba(1, 0.5, 0.5)
    cr.stroke()
    cr.restore()

def ground(cr: cairo.Context, x: float, y: float, alpha=1.0):
    cr.set_line_width(LW)
    cr.set_source_rgba(0, 0.7, 0, 0.25*alpha)
    cr.rectangle(x, y, 100-LW, 100-LW)
    cr.fill_preserve()
    cr.set_source_rgba(0, 0.7, 0, alpha)
    cr.stroke()

def arrow(cr: cairo.Context, x: float, y: float, theta: float, len: float, color=(1, 1, 0)):
    cr.set_line_width(LW)
    cr.set_source_rgba(*color)
    ARROWHEAD_LEN = 10
    
    cr.save()
    cr.move_to(x, y)
    cr.rotate(theta)
    #cr.rel_move_to(LW/2, 0)
    cr.rel_line_to(len - ARROWHEAD_LEN, 0)
    cr.stroke()
    cr.restore()

    cr.save()
    dx, dy = len*math.cos(theta), len*math.sin(theta)
    cr.move_to(x+dx, y+dy)
    cr.rotate(theta)
    cr.rel_line_to(-ARROWHEAD_LEN, -ARROWHEAD_LEN/2)
    cr.rel_line_to(0, ARROWHEAD_LEN)
    cr.close_path()
    cr.fill()
    cr.restore()

def cross(cr: cairo.Context, x: float, y: float, s: float=10):
    cr.set_source_rgba(1, 0, 0)
    cr.move_to(x-s, y-s)
    cr.rel_line_to(s*2, s*2)
    cr.stroke()
    cr.move_to(x-s, y+s)
    cr.rel_line_to(s*2, -s*2)
    cr.stroke()

def edgeground(cr: cairo.Context, x1: float, y1: float, dx: float, dy: float, alpha=1.0):
    cr.set_line_width(LW)
    cr.set_source_rgba(0, 0.7, 0, alpha)
    cr.move_to(x1, y1)
    cr.rel_line_to(dx, dy)
    cr.stroke()
    arrow(cr, x1+dx/2, y1+dy/2, math.atan2(-dx, dy), 25, (0.7, 1.0, 0, 0.7*alpha))
    cr.set_source_rgba(0.7, 1.0, 0, alpha)
    cr.arc(x1, y1, LW, 0, 2*math.pi)
    cr.arc(x1+dx, y1+dy, LW, 0, 2*math.pi)
    cr.fill()


PATH = "content/blog/ghost-collisions/images/"

W, H = 300, 250
with cairo.SVGSurface(f"{PATH}/ghostcollision1.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.scale(1, 1)
    
    ground(cr, 50, 150)
    ground(cr, 150, 150)
    player(cr, 80, 150, 0.05)
    player(cr, 90, 150, 0.1)
    player(cr, 100, 150, 0.2)
    player(cr, 110, 150, 0.7)
    arrow(cr, 110, 150-130/2, 0, 50, (1, 0, 0))

with cairo.SVGSurface(f"{PATH}/ghostcollision2.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.scale(1, 1)
    
    ground(cr, 50, 150)
    ground(cr, 150, 150)
    player(cr, 120, 150)

    cross(cr, 160, 150-130/2)

    cr.set_source_rgba(1, 1, 1)
    cr.set_font_size(40)
    cr.translate(150, 30)
    cr.text_path("?")
    cr.fill()


W, H = 250, 250
with cairo.SVGSurface(f"{PATH}/resolve1.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.translate(W/2, H/2)
    cr.scale(3, 3)
    cr.translate(-W/2, -H/2)
    
    ground(cr, W/2-50, H/2)
    player(cr, W/2, H/2+10)
    arrow(cr, W/2, H/2+3, -90*D2R, 30)

with cairo.SVGSurface(f"{PATH}/resolve2.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.translate(W/2, H/2)
    cr.scale(3, 3)
    cr.translate(-W/2, -H/2)
    
    ground(cr, W/2-50, H/2)
    player(cr, W/2, H/2+1)
    arrow(cr, W/2, H/2, -90*D2R, 30)

W, H = 300, 250
with cairo.SVGSurface(f"{PATH}/corner1.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.scale(1, 1)
    
    ground(cr, 50, 150, 0.2)
    ground(cr, 150, 150)
    player(cr, 145, 160)
    arrow(cr, 160, 153, -90*D2R, 25)
    arrow(cr, 133, 153, -90*D2R, 25, (.8, .8, .2, 0.15))

with cairo.SVGSurface(f"{PATH}/corner2.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.scale(1, 1)
    
    ground(cr, 50, 150, 0.2)
    ground(cr, 150, 150)
    player(cr, 130, 175)
    arrow(cr, 153, 160, -180*D2R, 25)
    arrow(cr, 125, 162, -90*D2R, 25, (.8, .8, .2, 0.15))

W, H = 300, 250
with cairo.SVGSurface(f"{PATH}/clippedcorner.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.translate(W/2, H/2)
    cr.scale(3, 3)
    cr.translate(-W/2, -H/2)
    
    ground(cr, 50, 150, 0.2)
    ground(cr, 150, 150)

    cr.move_to(60, 150)
    cr.rel_line_to(80, 0)
    cr.rel_line_to(20, -5)
    cr.rel_line_to(0, -95)
    cr.rel_line_to(-100, 0)
    cr.close_path()
    cr.set_source_rgba(1, 0.5, 0.5, 0.25)
    cr.fill_preserve()
    cr.set_source_rgba(1, 0.5, 0.5)
    cr.stroke()

    arrow(cr, 150, 150-4, math.atan2(-20, -5), 25, (1, 1, 0, 1))
    arrow(cr, 110, 150, -90*D2R, 25, (.8, .8, .2, 0.1))

with cairo.SVGSurface(f"{PATH}/clippedcorner2.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.translate(W/2, H/2)
    cr.scale(3, 3)
    cr.translate(-W/2, -H/2)
    
    ground(cr, 50, 150, 0.2)
    ground(cr, 150, 150)

    capsule(cr, 140, 150)

    arrow(cr, 150, 150-4, math.atan2(-20, -8), 25, (1, 1, 0, 1))
    arrow(cr, 140, 150, -90*math.pi/180, 25, (.8, .8, .2, 0.1))

W, H = 250, 150
with cairo.SVGSurface(f"{PATH}/chainshape.svg", W, H) as surf:
    cr = cairo.Context(surf)
    
    edgeground(cr, 10, 100, 40, 0, 0.15)
    edgeground(cr, 50, 100, 50, -50)
    edgeground(cr, 100, 50, 100, 0)
    edgeground(cr, 200, 50, 0, 50)
    edgeground(cr, 200, 100, 40, 40, 0.15)

W, H = 250, 150
with cairo.SVGSurface(f"{PATH}/platform.svg", W, H) as surf:
    cr = cairo.Context(surf)

    ground(cr, 50, 25)
    
    c = (1, 0.2, 1)
    cr.set_source_rgba(*c, 0.25)
    cr.rectangle(150, 25, 100-LW, 40-LW)
    cr.fill_preserve()
    cr.set_source_rgba(*c, 1)
    cr.stroke()

    arrow(cr, 200, 25+40/2, 0, 25, (*c, 1))
    arrow(cr, 200, 25+40/2, math.pi, 25, (*c, 1))

W, H = 300, 250
with cairo.SVGSurface(f"{PATH}/platform2.svg", W, H) as surf:
    cr = cairo.Context(surf)

    ground(cr, 50, 150)
    player(cr, 120, 150)
    
    # c = (1, 0.2, 1)
    # cr.set_source_rgba(*c, 0.25)
    # cr.rectangle(150, 25, 100-LW, 40-LW)
    # cr.fill_preserve()
    # cr.set_source_rgba(*c, 1)
    # cr.stroke()
    c = (0, 0.8, 1.0)
    g = cairo.LinearGradient(150, 150, 150, 180)
    g.add_color_stop_rgba(0, *c, 0.25)
    g.add_color_stop_rgba(1, *c, 0)
    cr.set_source(g)
    cr.rectangle(150, 150, 200-LW, 40-LW)
    cr.fill_preserve()
    g = cairo.LinearGradient(150, 150, 150, 180)
    g.add_color_stop_rgba(0, *c, 1)
    g.add_color_stop_rgba(1, *c, 0)
    cr.set_source(g)
    cr.stroke()

W, H = 150, 150
with cairo.SVGSurface(f"{PATH}/contactarea.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.translate(W/2, H/2)
    cr.scale(2, 2)
    cr.translate(-W/2, -H/2)

    ground(cr, -25, 75, 0.2)
    ground(cr, 75, 75)
    player(cr, 65, 85)
    arrow(cr, 83, 78, -90*D2R, 25)
    cr.set_line_width(LW/2)
    cr.move_to(73.5, 78)
    cr.line_to(93, 78)
    cr.stroke()
    cr.arc(75, 78, LW/2, 0, 2*math.pi)
    cr.arc(92, 78, LW/2, 0, 2*math.pi)
    cr.fill()

with cairo.SVGSurface(f"{PATH}/contactarea2.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.translate(W/2, H/2)
    cr.scale(2, 2)
    cr.translate(-W/2, -H/2)

    ground(cr, -30, 75, 0.2)
    ground(cr, 70, 75)
    player(cr, 50, 90)
    arrow(cr, 73, 81, math.pi, 25)
    cr.set_line_width(LW/2)

    cr.move_to(73, 75)
    cr.line_to(73, 87)
    cr.stroke()
    cr.arc(73, 75, LW/2, 0, 2*math.pi)
    cr.arc(73, 87, LW/2, 0, 2*math.pi)
    cr.fill()

W, H = 300, 300
with cairo.SVGSurface(f"{PATH}/solution.svg", W, H) as surf:
    cr = cairo.Context(surf)
    cr.translate(W/2, H/2)
    cr.scale(2, 2)
    cr.translate(-W/2, -H/2)

    ground(cr, 50, 150, 0.2)
    ground(cr, 150, 150)
    player(cr, 130, 175)
    arrow(cr, 130, 150-130/2, 0, 50, (1, 0, 0))
    arrow(cr, 153, 160, -180*D2R, 25)
    arrow(cr, 125, 162, -90*D2R, 25, (.8, .8, .2, 0.15))

    cr.set_line_width(LW*0.5)
    cross(cr, 145, 160, 5)
