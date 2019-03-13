import os
from numpy import size

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

f = open(".gitmodules", "r")

content = f.read()

modules = content.split('[submodule')

module_path = []
module_url = []

print('\033[93m' + 'This process will take couple of minutes')
print('Please go get a coffee or do something else while this code is running')

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

	print(' ' + bcolors.NORMAL)
	print('Cloning/Updating Repo ' + git_url)
	os.system('git clone ' + git_url + ' ' + submodule)
	# Checkout to specified Branch or Tag after cloning or fetching
	os.system('cd ' + submodule + ' && ' + 'git checkout ' + git_branch + ' && git fetch')
	print(' ')


print(bcolors.OKGREEN + ' ' + 'All Done')
