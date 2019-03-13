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
	url = module_url[module_path.index(submodule)].split('#')
	try :
		git_url = url[0]
		git_branch = url[1]
	except :
		git_url = url[0]
		git_branch = 'master'

	print('Cloning/Updating Repo ' + git_url)
	os.system('git clone ' + git_url + ' ' + submodule)
	# Checkout to specified Branch or Tag after cloning or fetching
	os.system('cd ' + submodule + ' && ' + 'git checkout ' + git_branch + ' && git fetch')
	print(' ')

