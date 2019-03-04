from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""


def run_cmds(cmd, prm, edg, trans, scr, clr):
    if cmd == "line":
        add_edge(edg, int(prm[0]), int(prm[1]), int(prm[2]), int(prm[3]), int(prm[4]), int(prm[5]))
    elif cmd == "ident":
        ident(trans)
    elif cmd == "scale":
        matrix_mult(make_scale(int(prm[0]), int(prm[1]), int(prm[2])), trans)
    elif cmd == "translate":
        #print(make_translate(int(prm[0]), int(prm[1]), int(prm[2])))
        matrix_mult(make_translate(int(prm[0]), int(prm[1]), int(prm[2])), trans)
    elif cmd == "move":
        #print(make_translate(int(prm[0]), int(prm[1]), int(prm[2])))
        matrix_mult(make_translate(int(prm[0]), int(prm[1]), int(prm[2])), trans)
    elif cmd == "rotate":
        matrix_mult(
            make_rotX(float(prm[1])) if prm[0] == "x" else make_rotY(float(prm[1])) if prm[0] == "y" else make_rotZ(
                float(prm[1])), trans)
    elif cmd == "apply":
        matrix_mult(trans, edg)
    elif cmd == "display":
        clear_screen(scr)
        draw_lines(edg, scr, clr)
        display(scr)
    elif cmd == "save":
        clear_screen(scr)
        draw_lines(edg, scr, clr)
        save_extension(scr, prm[0])


def parse_file(fname, edges, transform, screen, color):
    cmd = ''
    with open(fname) as f:
        for l in f:
            prms = l.rstrip('\n').split()
            #print(prms)
            if prms[0] == 'quit':
                return
            if prms[0] in ['display', 'apply', 'ident']:
                #print("RUN", prms[0])
                run_cmds(prms[0], prms, edges, transform, screen, color)
            elif len(prms) > 1 or cmd == "save":
                #print("RUNN", cmd, prms)
                run_cmds(cmd, prms, edges, transform, screen, color)
            else:
                cmd = prms[0]
                #print("setting cmd", cmd)
