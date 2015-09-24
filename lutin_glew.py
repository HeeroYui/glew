#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "Glew generic glew interface (for windows only)"


def create(target):
	if target.name=="Windows":
		#http://glew.sourceforge.net/index.html
		my_module = module.Module(__file__, 'glew', 'PREBUILD')
		
		my_module.add_export_path(tools.get_current_path(__file__) + "/glew/include/")
		if target.config["bus-size"] == "32":
			my_module.add_export_flag('link', [
				tools.get_current_path(__file__) + "/glew/lib/Release/Win32/glew32s.lib"
				])
		else:
			my_module.add_export_flag('link', [
				tools.get_current_path(__file__) + "/glew/lib/Release/x64/glew32s.lib",
				])
		my_module.add_export_flag('link', [
			"-lopengl32",
			"-lgdi32",
			"-static-libgcc",
			"-static-libstdc++"])
		
		# add the currrent module at the 
		return my_module
	else:
		return None


