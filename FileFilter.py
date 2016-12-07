import sys, os, getopt
import os.path

options = "hi:o:f:c"
optionsLong = ["input_dir=", "output_dir=", "file_suffix=", "convert", "help"]
opts, args = getopt.getopt(sys.argv[1:], options, optionsLong)
input_dir = ""
output_dir = ""
file_suffix = ""
save_convert = False

def usage() :
    print("""Options: %s, %s
        -i, --input_dir=<input_dir>   	directory of source files
        -o, --output_dir=<output_dir>	directory of target files
        -f, --file_suffix<file_suffix>	the suffix name of the file
        -c, --convert=<convert>       	convert the filter
        -h, --help                      display this help
    Note: 2016-12-08 00:52
    """ % (options, optionsLong))

for op, value in opts:
	if op in ('-i', '--input_dir'): input_dir = value
	elif op in ('-o', '--output_dir'): output_dir = value
	elif op in ('-f', '--file_suffix'): file_suffix = value
	elif op in ('-c', '--convert'): save_convert = True
	elif op in ('-h', '--help'):
		usage()
		sys.exit()

if input_dir == "" or output_dir == "" or file_suffix == "":
	print("args are invalid!")
	sys.exit()

for parent, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
    	needSave = filename.endswith(file_suffix)
    	if save_convert: needSave = (not needSave)
    	if needSave:
    		sourceFile = os.path.join(parent, filename)
    		targetDir = parent.replace(input_dir, output_dir)
    		targetFile = os.path.join(targetDir, filename)
    		if not os.path.exists(targetDir): os.makedirs(targetDir) 
    		open(targetFile, "wb").write(open(sourceFile, "rb").read())

