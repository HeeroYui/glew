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
	return [1,13,0]

def create(target, module_name):
	if "Windows" in target.get_type():
		#http://glew.sourceforge.net/index.html
		my_module = module.Module(__file__, module_name, get_type())
		
		my_module.add_header_file([
		    'glew/include/GL/glew.h',
		    'glew/include/GL/glxew.h',
		    'glew/include/GL/wglew.h'
		    ],
		    destination_path="GL")
		my_module.add_src_file([
		    'glew/src/glew.c',
		    'glew/src/glewinfo.c',
		    'glew/src/visualinfo.c'
		    ])
		"""
		my_module.add_flag('link-lib', [
		    "opengl32",
		    "gdi32"
		    ],
		    export=True)
		"""
		return my_module
	else:
		return None


