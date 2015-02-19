#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright 2012-2015 OpenBroadcaster, Inc.

This file is part of OpenBroadcaster Player.

OpenBroadcaster Player is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenBroadcaster Player is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with OpenBroadcaster Player.  If not, see <http://www.gnu.org/licenses/>.
"""

import obplayer

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk, Gdk, GdkX11, GdkPixbuf, cairo, Pango, PangoCairo


class ObOverlay (object):
    def __init__(self):
	self.enabled = False
	self.message = ''
	self.scroll_pos = 0.0
	self.scroll_wrap = 1.0
	GObject.timeout_add(50, self.overlay_scroll_timer)

    def overlay_scroll_timer(self):
	self.scroll_pos -= 0.01
	if self.scroll_pos <= 0.0:
	    self.scroll_pos = self.scroll_wrap
        GObject.timeout_add(50, self.overlay_scroll_timer)

    def set_message(self, msg):
	if msg == '':
	    self.enabled = False
	else:
	    self.enabled = True
	    if self.message != msg:
		self.scroll_pos = 0.0
	    self.message = msg

    def draw_overlay(self, context, width, height):
	if self.enabled and self.message:
	    #print str(width) + " x " + str(height)
	    #context.scale(width, height)
	    #context.scale(width / 100, height / 100)
	    #context.scale(100, 100)
	    #context.set_source_rgb(1, 0, 0)
	    #context.paint_with_alpha(1)
	    #context.select_font_face("Helvetica")
	    #context.set_font_face(None)
	    #context.set_font_size(0.05)
	    #context.move_to(0.1, 0.1)
	    #context.show_text("Hello World")
	    #context.rectangle(0, height * 0.60, width, 30)
	    #context.rectangle(0, 0.60, 1, 0.1)

	    context.set_source_rgb(1, 0, 0)
	    context.rectangle(0, 0.60 * height, width, 0.1 * height)
	    context.fill()

	    #context.scale(1.0 / width, 1.0 / height)
	    #context.translate(0, height * 0.60)

	    layout = PangoCairo.create_layout(context)
	    layout.set_font_description(Pango.font_description_from_string("Sans " + str(0.060 * height)))
	    layout.set_text(self.message, -1)

	    (layout_width, layout_height) = layout.get_pixel_size()
	    self.scroll_wrap = 1.0 + (float(layout_width) / float(width))
	    pos = (self.scroll_pos * width) - layout_width
	    context.set_source_rgb(1, 1, 1)
	    context.translate(pos, 0.60 * height)
	    PangoCairo.update_layout(context, layout)
	    PangoCairo.show_layout(context, layout)

	    #context.set_line_width(0.1)
	    #context.move_to(0, 0)
	    #context.line_to(1, 0)
	    #context.stroke()

	#pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size("/home/trans/Downloads/kitty.jpg", width, height)
	#Gdk.cairo_set_source_pixbuf(context, pixbuf, 0, 0)
	#context.stroke()

