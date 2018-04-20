import os
path = os.getcwd()
for filename in os.listdir(os.getcwd()):

	arr = filename.split('_')
	print arr[0]
	try:
		if len(arr[0]) == 1:
			new_filename = "0" + str(arr[0]) + "_" + str(filename[2:])
			os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
	except:
		pass