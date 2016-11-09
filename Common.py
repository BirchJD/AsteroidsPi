#!/usr/bin/python

# AsteroidsPi - Raspberry Pi Asteroids Using Python and PyGame
# Copyright (C) 2015 Jason Birch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#/****************************************************************************/
#/* AsteroidsPi - Raspberry Pi Asteroids Using Python and PyGame             */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2016-11-07 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Conversion of Asteroids example game programming on multiple platforms,  */
#/* Raspberry Pi Asteroids Using Python and PyGame.                          */
#/****************************************************************************/


import struct
import pygame
import Common


#  /***************************/
# /* Set the play area size. */
#/***************************/
class DesktopType:
   DISPLAY_X = 0
   DISPLAY_Y = 0
   DISPLAY_WIDTH = 640
   DISPLAY_HEIGHT = 440

   def __init__(self):
      self.x = self.DISPLAY_X
      self.y = self.DISPLAY_Y
      self.width = self.DISPLAY_WIDTH
      self.height = self.DISPLAY_HEIGHT


class XPoint:
   def __init__(self):
      self.x = 0
      self.y = 0


Desktop = DesktopType()



def DrawLine(ThisSurface, X1, Y1, X2, Y2, Colour):
   pygame.draw.line(ThisSurface, Colour, [X1, Y1], [X2, Y2], 1)



def DrawLines(ThisSurface, Points, PointCount, Colour):
   for Count in range(PointCount - 1):
      DrawLine(ThisSurface, Points[Count].x, Points[Count].y, Points[Count + 1].x, Points[Count + 1].y, Colour)



def FillRectangle(ThisSurface, X, Y, SizeX, SizeY, Colour):
   pygame.draw.rect(ThisSurface, Colour, [X, Y, SizeX, SizeY], 0)



def DrawUpdate():
   pygame.display.flip()

