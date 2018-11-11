import os






def build_file_dict(file_dir):
	file_dict = dict()
	files = os.listdir(file_dir)
	print(files)
	
	return file_dict



def main():
	file_dir = "./test_pics/"
	build_file_dict(file_dir)



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