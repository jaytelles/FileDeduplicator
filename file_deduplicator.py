import os
import hashlib
from functools import partial


#from https://stackoverflow.com/questions/7829499/using-hashlib-to-compute-md5-digest-of-a-file-in-python-3
def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

def build_file_dict(file_dir):
	file_dict = dict()
	filenames = os.listdir(file_dir)
	
	#should probs be a lambda
	for x in range(0, len(filenames)):
		filenames[x] = file_dir + filenames[x]
	
	for filename in filenames:
		file_dict[filename] = md5sum(filename)
	print(len(file_dict))
	
	return file_dict

def parse_out_dups(file_dict):
	for key in file_dict.keys()
	

	return file_dict

	

def main():
	in_file_dir = "./test_pics/"
	out_file_dir = "./test_final"
	file_dict = build_file_dict(file_dir)
	parse_out_dups(file_dict)


if __name__ == "__main__":
	main()
	
	
"""
potential file naming scheme:
YYYY-MM-DD
YYYYMMDD_6[0-9]((1-2))
YYYYMMDD_6[0-9]_HDR((1-2))
IMG_YYYYMMDD_6[0-9]
4371237753670073950_account_id=1 //wtf
PANO_YYYYMMDD_6[0-9]
VID_YYYYMMDD_6[0-9]
"""