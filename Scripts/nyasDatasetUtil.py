import os, sys
import numpy
import json
import time



def verify_nyas_dataset_files(file_list, root_dir, ext, replace_str):
	"""
	"""

	#reading the dataset file
	lines = open(file_list, 'r').readlines()
	files_present = 0
	files_absent = 0
	for line in lines:
		fname = line.strip()
		audiopath = os.path.join(root_dir, fname)
		fname, ext_temp = os.path.splitext(audiopath)
		fname = fname.replace(replace_str[0], replace_str[1])
		if os.path.isfile(fname + ext):
			files_present += 1
		else:
			print fname + ext
			files_absent += 1

	return files_present + files_absent, files_present


def batch_verify_nyas_dataset_files():
	"""

	"""
	report_file = '/media/sankalp/Work1/PHD_structured/Datasets/NyasDataset/report.txt'
	filelist_file = '..//NyasDataset/_info_/filelist.txt'
	root_dir = '../'

	fid = open(report_file,'w')
	fid.write("This report is generated on %s\t\n\n"%time.strftime("%x"))
	fid.write("This is an automatically generated report. It contains information about the verification of the dataset, we check each an every file related with the dataset and summarize the results in this file.\n\n")

	fid.write("Format: %s\t%s\t%s\n\n\n"%('Type of file', 'total files', 'files present'))


	sources = {
				'audio': {'ext': '.mp3', 'replace': ['audio', 'audio']},
				'annotations': {'ext': '.nyas', 'replace': ['audio', 'annotations']},
				'pitch': {'ext': '.essentia.pitch', 'replace': ['audio', 'features']},
				'tonic': {'ext': '.tonic', 'replace': ['audio', 'features']},
				'intermediate_output': {'ext': '.NyasCand.textgrid', 'replace': ['audio', 'intermediate_output']},
				'intermediate_output': {'ext': '.OwnSegments', 'replace': ['audio', 'intermediate_output']},
				'annotations_textgrid_complex': {'ext': '.NyasAnnotation.TextGrid', 'replace': ['audio', 'annotations_textgrid_complex']}								
				}

	for k in sources.keys():
		nfiles, npresent = verify_nyas_dataset_files(filelist_file, root_dir, sources[k]['ext'], sources[k]['replace'])
		fid.write("%s\t%d\t%d\n"%(k, nfiles, npresent))

	fid.close()



