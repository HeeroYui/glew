#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "PREBUILD"

def get_desc():
	return "Glew generic glew interface (for windows only)"

def get_licence():
	return "GPL"

def get_maintainer():
	return ["Milan Ikits <milan ikits@ieee org>",
	        "Marcelo E. Magallon <mmagallo@debian org>"]

def get_version():
	return [4,5]

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
		
		if target.config["bus-size"] == "32":
			my_module.add_flag('link-lib', [
				os.path.join(tools.get_current_path(__file__), "glew/lib/Release/Win32/glew32s.lib")
				],
				export=True)
		else:
			my_module.add_flag('link-lib', [
				os.path.join(tools.get_current_path(__file__), "glew/lib/Release/x64/glew32s.lib")
				],
				export=True)
		my_module.add_flag('link-lib', [
			"opengl32",
			"gdi32"
			],
			export=True)
		return my_module
	else:
		return None


