#!/usr/bin/env python

"""
Render Command:
manim -p -qh [Filename].py [class_name]

-p          PREVIEW
-a          RENDER ALL SCENES
            IN THE FILE
            (DON'T USE IT WITH -p FLAG)
-ql         LOW QUALITY         480p    15 fps
-qm         MEDIUM QUALITY      720p    30 fps
-qh         HIGHT QUALITY       1080p   60 fps
-qp         PRODUCTION QUALITY  1440p   60 fps
-qk         4K                  2160p   60 fps
-s          RENDER PNG OF THE
            LAST FRAME
-t          TRANSPARENT RENDER
Shorts:
    -pql    PREVIEW IN LOW QUALITY
    -pqm    PREVIEW IN MEDIUM QUALITY
    -pqh    PREVIEW IN HIGHT QUALITY
    -pqp    PREVIEW IN PRODUCTION QUALITY
    -pqk    PREVIEW IN 4K QUALITY
    -ps     RENDER LAST FRAME AS PNG
"""

from manim import *

class TipToTail(Scene):
    def construct(self):

        # Define objects

        plane = NumberPlane()
        v1 = Arrow([0, 0, 0], [2, 1, 0], buff=0).set_color(BLUE)
        v2 = Arrow([0, 0, 0], [2, 3, 0], buff=0).set_color(GREEN)
        v3 = Arrow([0, 0, 0], [4, 4, 0], buff=0).set_color(RED)
        vg = VGroup(v1, v2, v3)

        # Vector A + Components + Labels

        x1_start = (0,-2,0)
        x1_end =   (2,-2,0)
        y1_start = (2,-2,0)
        y1_end =   (2,-1,0)
        v1_x = DashedVMobject(Line(x1_start, x1_end))
        v1_y = DashedVMobject(Line(y1_start, y1_end))
        v1_g = VGroup(v1_x, v1_y)
        v1_xlabel = Tex("2").set_color(BLUE)
        v1_ylabel = Tex("1").set_color(BLUE)
        v1_labels = VGroup(v1_xlabel, v1_ylabel)

        # Vector B + Components + Labels

        x2_start = (2,-1,0)
        x2_end =   (4,-1,0)
        y2_start = (4,-1,0)
        y2_end =   (4,2,0)
        v2_x = DashedVMobject(Line(x2_start, x2_end))
        v2_y = DashedVMobject(Line(y2_start, y2_end))
        v2_g = VGroup(v2_x, v2_y)
        v2_xlabel = Tex("2").set_color(GREEN)
        v2_ylabel = Tex("3").set_color(GREEN)
        v2_labels = VGroup(v2_xlabel, v2_ylabel)

        # Vector C + Components + Labels

        x3_start = (0,-2,0)
        x3_end =   (4,-2,0)
        y3_start = (4,-2,0)
        y3_end =   (4,2,0)
        v3_x = DashedVMobject(Line(x3_start, x3_end))
        v3_y = DashedVMobject(Line(y3_start, y3_end))
        v3_g = VGroup(v3_x, v3_y)
        v3_xlabel = Tex("4").set_color(RED)
        v3_ylabel = Tex("4").set_color(RED)
        v3_labels = VGroup(v3_xlabel, v3_ylabel)

        # Matrix A, B, C + Operations + Labels

        add = Tex("+")
        equals = Tex("=")

        m1 = Matrix([[2], [1]]).set_color(BLUE)
        m2 = Matrix([[2], [3]]).set_color(GREEN)
        m3 = Matrix([[4], [4]]).set_color(RED)
        mg = VGroup(m1, add, m2, equals, m3)

        m1_label = MathTex(r"\overrightarrow{\text{a}}").set_color(BLUE)
        m2_label = MathTex(r"\overrightarrow{\text{b}}").set_color(GREEN)
        m3_label = MathTex(r"\overrightarrow{\text{c}}").set_color(RED)

        # Matrix Orientations

        mg.to_edge(LEFT, buff=1)
        add.next_to(m1, RIGHT)
        m2.next_to(add, RIGHT)
        equals.next_to(m2, RIGHT)
        m3.next_to(equals, RIGHT)
        m1_label.next_to(m1, UP)
        m2_label.next_to(m2, UP)
        m3_label.next_to(m3, UP)
        v1_xlabel.next_to(v1_x, DOWN)
        v1_ylabel.next_to(v1_y, RIGHT)
        v2_xlabel.next_to(v2_x, DOWN)
        v2_ylabel.next_to(v2_y, RIGHT)
        v3_xlabel.next_to(v3_x, DOWN)
        v3_ylabel.next_to(v3_y, RIGHT)

        # Animation instructions

        def play():

            self.play(Create(plane, run_time=3, lag_ratio=0.1))
            self.wait(1)
            self.play(GrowArrow(v1))
            self.wait(1)
            self.play(GrowArrow(v2))
            self.wait(2)
            self.play(ApplyMethod(v2.shift, 2*RIGHT))
            self.play(ApplyMethod(v2.shift, 1*UP))
            self.wait(2)
            self.play(GrowArrow(v3))
            self.wait()
            self.play(FadeOut(plane))
            self.play(ApplyMethod(vg.shift, 2*DOWN))
            self.play(Create(v1_g))
            self.play(FadeIn(v1_labels))
            self.play(FadeIn(m1, m1_label))
            self.wait()
            self.play(Create(v2_g))
            self.play(FadeIn(v2_labels))
            self.play(FadeIn(add, m2, m2_label))
            self.play(FadeOut(v1_g, v2_g, v1_labels, v2_labels))
            self.wait()
            self.play(Create(v3_g))
            self.play(FadeIn(v3_labels))
            self.play(FadeIn(equals, m3, m3_label))
            self.wait(3)
            self.play(FadeOut(v3_g, v3_labels, m1, m1_label, add, m2, m2_label, equals, m3, m3_label, vg))
            self.wait()

        play()
