#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

TRACE = True
DEBUG = False

class DragonModel(object):
	"""ドラゴンのモデル。"""

	def __init__(self):
		"""ドラゴンのモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		self._triangles = []
		self._eye_point = [-5.5852450791872 , 3.07847342734 , 15.794105252496]
		self._sight_point = [0.27455347776413 , 0.20096999406815 , -0.11261999607086]
		self._up_vector = [0.1018574904194 , 0.98480906061847 , -0.14062775604137]
		self._fovy = 12.642721790235
		self._display_list = None
		self._view = None

		filename = os.path.join(os.getcwd(), 'dragon.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Dragon/dragon.txt'
			urllib.urlretrieve(url, filename)
		with open(filename, "rU") as a_file:
			a_string = a_file.readline()
			print a_string

			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_list = a_string.split()
				if "number_of_vertexes" == a_list[0]:
					number_of_vertexes = int(a_list[1])
				if "number_of_triangles" == a_list[0]:
					number_of_triangles = int(a_list[1])
				if "end_header" == a_list[0]:
					vertexes = []
					for index in range(number_of_vertexes):
						a_string = a_file.readline()
						vertex = map(float, a_string.split())
						vertexes.append(vertex)
					for index in range(number_of_triangles):
						a_string = a_file.readline()
						indexes = map(int, a_string.split())
						vertex1, vertex2, vertex3 = map((lambda index: vertexes[index-1]), indexes)
						a_triangle = DragonTriangle(vertex1, vertex2, vertex3)
						self._triangles.append(a_triangle)
		return

	def display_list(self):
		"""ドラゴンのモデルのディスプレイリスト(表示物をコンパイルしたOpenGLコマンド列)を応答する。"""
		if TRACE: print __name__, self.display_list.__doc__

		if self._display_list == None:
			self._display_list = glGenLists(1)
			glNewList(self._display_list, GL_COMPILE)
			glColor4d(0.500061,  0.500061, 1.0, 1.0)
			for index, triangle in enumerate(self._triangles):
				if DEBUG: print index,
				triangle.rendering()
			glEndList()

		return self._display_list

	def open(self):
		"""ドラゴンのモデルを描画するためのOpenGLのウィンドウを開く。"""
		if TRACE: print __name__, self.open.__doc__

		self._view = DragonView(self)

		glutMainLoop()

		return

	def rendering(self):
		"""ドラゴンのモデルをレンダリングする。"""
		if TRACE: print __name__, self.rendering.__doc__

		glCallList(self.display_list())

		return

class DragonView(object):
	"""ドラゴンのビュー。"""

	def __init__(self, a_model):
		"""ドラゴンのビューのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		self._model = a_model
		self._controller = DragonController(self)
		self._angle_x = 0.0
		self._angle_y = 0.0
		self._angle_z = 0.0

		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutCreateWindow("Dragon")

		glutDisplayFunc(self.display)
		glutReshapeFunc(self.reshape)
		glutKeyboardFunc(self._controller.keyboard)
		glutMouseFunc(self._controller.mouse)
		glutMotionFunc(self._controller.motion)


		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		glEnable(GL_NORMALIZE)

		return

	def display(self):
		"""OpenGLで描画する。"""
		if TRACE: print __name__, self.display.__doc__

		eye_point = self._model._eye_point
		sight_point = self._model._sight_point
		up_vector = self._model._up_vector

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(eye_point[0], eye_point[1], eye_point[2],
				  sight_point[0], sight_point[1], sight_point[2],
				  up_vector[0], up_vector[1], up_vector[2])
	
		glClearColor(1.0, 1.0, 1.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		glEnable(GL_LIGHTING)
		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.5, 0.5, 0.5, 1.0])
		glLightModelf(GL_LIGHT_MODEL_LOCAL_VIEWER, 0.0)
		glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, 1.0)
		glEnable(GL_LIGHT0)
		glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 1.0, 0.0])
		glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0.0, 0.0, -1.0])
		glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, 90.0)
		glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
		glLightfv(GL_LIGHT0, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
		glLightfv(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
		glLightfv(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)
		glLightfv(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)

		glBegin(GL_LINES);
		glColor([ 1.0, 0.0, 0.0, 1.0 ])
		glVertex([-1.000, 0.0, 0.0 ])
		glVertex([ 1.618, 0.0, 0.0 ])
		glColor([ 0.0, 1.0, 0.0, 1.0 ])
		glVertex([ 0.0,-1.000, 0.0 ])
		glVertex([ 0.0, 1.618, 0.0 ])
		glColor([ 0.0, 0.0, 1.0, 1.0 ])
		glVertex([ 0.0, 0.0,-1.000 ])
		glVertex([ 0.0, 0.0, 1.618 ])
		glEnd();

		glRotated(self._angle_x, 1.0, 0.0, 0.0)
		glRotated(self._angle_y, 0.0, 1.0, 0.0)
		glRotated(self._angle_z, 0.0, 0.0, 1.0)

		self._model.rendering()

		glutSwapBuffers()

		return

	def reshape(self, w, h):
		"""OpenGLを再形成する。"""
		if TRACE: print __name__, self.reshape.__doc__

		fovy = self._model._fovy

		glViewport(0, 0, w, h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(fovy, float(w) / float(h), 0.01, 100.0)

		return

class DragonController(object):
	"""ドラゴンのコントローラ。"""

	def __init__(self, a_view):
		"""ドラゴンのコントローラのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__

		self._model = a_view._model
		self._view = a_view
		self._back_x = 0
		self._back_y = 0

	def keyboard(self, key, x, y):
		"""キーボードを処理する。"""
		if TRACE: print __name__, self.keyboard.__doc__

		if key in "qQ\33":
			sys.exit()
		if key == 'r' or key == 'R':
			self._view._angle_x = 0.0
			self._view._angle_y = 0.0
			self._view._angle_z = 0.0
		if key == 'x':
			self._view._angle_x += 1.0
		if key == 'y':
			self._view._angle_y += 1.0
		if key == 'z':
			self._view._angle_z += 1.0
		if key == 'X':
			self._view._angle_x -= 1.0
		if key == 'Y':
			self._view._angle_y -= 1.0
		if key == 'Z':
			self._view._angle_z -= 1.0

		glutPostRedisplay()

		return

	def motion(self, x, y):
		"""マウスボタンを押下しながらの移動を処理する。"""
		if TRACE: print __name__, self.motion.__doc__
		dx = x - self._back_x
		dy = y - self._back_y

		if dx == 0 and dy == 0:
			pass
		elif dx == 0:
			self._view._angle_x+=dy
			self._view._angle_z+=dy
			print
		elif dy == 0:
			self._view._angle_y+=dx
		else:
			theta = math.atan2(dx, dy)
			dr = dy / math.sin(theta)
			an_angle = math.degrees(theta)
			print an_angle
			if 0 < an_angle and an_angle < 90:
				self._view._angle_z-=dr
			elif 90 < an_angle and an_angle < 180:
				self._view._angle_x-=dr
			elif 180 < an_angle and an_angle < 270:
				self._view._angle_z+=dr
			elif 270 < an_angle and an_angle < 360:
				self._view._angle_x+=dr
		self._back_x = x
		self._back_y = y
		glutPostRedisplay()
		print "motion at (" + str(x) + ", " + str(y) + ")"
	
		return

	def mouse(self, button, state, x, y):
		"""マウスボタンを処理する。"""
		if TRACE: print __name__, self.mouse.__doc__
	
		if button == GLUT_LEFT_BUTTON:
			print "left",
		elif button == GLUT_MIDDLE_BUTTON:
			print "middle"
		elif button == GLUT_RIGHT_BUTTON:
			print "right",
		else:
			pass
	
		print "button is",
	
		if state == GLUT_DOWN:
			print "down",
		elif state == GLUT_UP:
			print "up",
		else:
			pass
	
		print "at (" + str(x) + ", " + str(y) + ")"
	
		return

class DragonTriangle(object):
	"""ドラゴンの三角形。"""

	def __init__(self, vertex1, vertex2, vertex3):
		"""ドラゴンの三角形のコンストラクタ。"""
		if DEBUG: print __name__, self.__init__.__doc__

		self._vertex1 = vertex1
		self._vertex2 = vertex2
		self._vertex3 = vertex3
		ux, uy, uz  = map((lambda p1, p0: p1 - p0), vertex2, vertex1)
		vx, vy, vz = map((lambda p1, p0: p1 - p0), vertex3, vertex1)
		normal_vector = [(uy * vz - uz * vy), (uz * vx - ux * vz), (ux * vy - uy * vx)]
		distance = sum(map((lambda value: value * value), normal_vector)) ** 0.5
		self._normal_unit_vector = map((lambda vector: vector / distance), normal_vector)

	def rendering(self):
		"""ドラゴンの三角形をレンダリングする。"""
		if DEBUG: print __name__, self.rendering.__doc__

		glBegin(GL_TRIANGLES)
		glNormal3fv(self._normal_unit_vector)
		glVertex3fv(self._vertex1)
		glVertex3fv(self._vertex2)
		glVertex3fv(self._vertex3)
		glEnd()

def main():
	"""ドラゴンの立体データを読み込んで描画する。"""
	if TRACE: print __name__, main.__doc__

	a_model = DragonModel()
	a_model.open()

	return

if __name__ == '__main__':
	sys.exit(main())
