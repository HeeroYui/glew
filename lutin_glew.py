#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "Glew generic glew interface (for windows only)"

def get_licence():
	return "BSD-3"

def get_maintainer():
	return ["Milan Ikits <milan ikits@ieee org>",
	        "Marcelo E. Magallon <mmagallo@debian org>"]

def get_version():
	return [2,0,0]

def configure(target, my_module):
	if "Windows" not in target.get_type():
		return False
	
	my_module.add_header_file([
	    'glew/include/GL/glew.h',
	    'glew/include/GL/glxew.h',
	    'glew/include/GL/wglew.h',
	    'glew/include/GL/eglew.h'
	    ],
	    destination_path="GL")
	my_module.add_src_file([
	    'glew/src/glew.c',
	    #'glew/src/glewinfo.c',
	    #'glew/src/visualinfo.c'
	    ])
	"""
	my_module.add_src_file([
	    'glew/auto/src/glewinfo_gl.c',
	    'glew/auto/src/glew_init_tail.c',
	    'glew/auto/src/glew_head.c',
	    'glew/auto/src/glew_init_egl.c',
	    'glew/auto/src/glew_init_gl.c',
	    'glew/auto/src/glew_init_glx.c',
	    'glew/auto/src/glew_str_glx.c',
	    'glew/auto/src/glewinfo_wgl.c',
	    'glew/auto/src/glewinfo_tail.c',
	    'glew/auto/src/glew_str_wgl.c',
	    'glew/auto/src/glew_str_egl.c',
	    'glew/auto/src/glew_str_tail.c',
	    'glew/auto/src/glewinfo_head.c',
	    'glew/auto/src/glew_str_head.c',
	    'glew/auto/src/glew_init_wgl.c',
	    'glew/auto/src/glewinfo_egl.c',
	    'glew/auto/src/glewinfo_glx.c',
	    ])
	"""
	my_module.add_depend([
	    "opengl",
	    "gdi"
	    ])
	my_module.add_path("glew/auto/src/")
	return True


