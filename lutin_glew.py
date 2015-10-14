#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "PREBUILD"

def get_desc():
	return "Glew generic glew interface (for windows only)"

def get_licence():
	return "BSD-3"

def get_maintainer():
	return ["Milan Ikits <milan ikits@ieee org>",
	        "Marcelo E. Magallon <mmagallo@debian org>"]

def get_version():
	return [4,5]

def create(target, module_name):
	if target.name=="Windows":
		#http://glew.sourceforge.net/index.html
		my_module = module.Module(__file__, module_name, get_type())
		
		my_module.add_header_file([
			'glew/include/GL/glew.h',
			'glew/include/GL/glxew.h',
			'glew/include/GL/wglew.h'
			],
			destination_path="GL")
		
		#my_module.add_export_path(tools.get_current_path(__file__) + "/glew/include/")
		if target.config["bus-size"] == "32":
			my_module.add_export_flag('link', [
				os.path.join(tools.get_current_path(__file__), "glew/lib/Release/Win32/glew32s.lib")
				])
		else:
			my_module.add_export_flag('link', [
				os.path.join(tools.get_current_path(__file__), "glew/lib/Release/x64/glew32s.lib")
				])
		my_module.add_export_flag('link', [
			"-lopengl32",
			"-lgdi32",
			"-static-libgcc",
			"-static-libstdc++"])
		return my_module
	else:
		return None


