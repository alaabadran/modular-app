import os
from numpy import size

f = open(".gitmodules", "r")

content = f.read()

modules = content.split('[submodule')

module_path = []
module_url = []

for module in modules :
	if modules != '':
		module_arr = module.split('\n')
		if(size(module_arr) > 1 ):
			module_path.append(module_arr[1].split('=')[1])
			module_url.append(module_arr[2].split('=')[1])

for submodule in module_path :
	os.system('git clone ' + module_url[module_path.index(submodule)] + ' ' + submodule)
