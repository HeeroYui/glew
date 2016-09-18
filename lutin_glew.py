#!/usr/bin/python
import lutin.module as module
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

def create(target, module_name):
	if "Windows" in target.get_type():
		#http://glew.sourceforge.net/index.html
		my_module = module.Module(__file__, module_name, get_type())
		
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
		my_module.add_flag('link-lib', [
		    "opengl32",
		    "gdi32"
		    ],
		    export=True)
		my_module.add_path("glew/auto/src/")
		return my_module
	else:
		return None


