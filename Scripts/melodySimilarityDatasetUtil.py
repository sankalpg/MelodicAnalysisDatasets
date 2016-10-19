import os, sys
import numpy
import json
import time



def verify_melodic_similarity_dataset_files(file_list, root_dir, ext, replace_str):
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


def batch_verify_melody_similarity_dataset_files():
	"""

	"""
	report_file = '/media/sankalp/Work1/PHD_structured/Datasets/MelodicSimilarityDataset/report.txt'
	filelist_carnatic = '../MelodicSimilarityDataset/Carnatic/_info_/filelist.txt'
	filelist_hindustani = '../MelodicSimilarityDataset/Hindustani/_info_/filelist.txt'

	root_dir = '../'

	fid = open(report_file,'w')
	fid.write("This report is generated on %s\t\n\n"%time.strftime("%x"))
	fid.write("This is an automatically generated report. It contains information about the verification of the datasets, we check each an every file related with the dataset and summarize the results in this file.\n\n")

	fid.write("Format: %s,\t%s,\t%s\n\n\n"%('Type of file', 'total files', 'files present'))

	fid.write("This is  for the Carnatic music dataset\n\n")	

	
	sources = {
				'audio': {'ext': '.mp3', 'replace': ['audio', 'audio']},
				'annotations_original': {'ext': '.anot', 'replace': ['audio', 'annotations_orig']},
				'annotations_impr': {'ext': '.anotEdit1', 'replace': ['audio', 'annotations_impr']},
				'pitch': {'ext': '.pitch', 'replace': ['audio', 'features']},
				'pitch_postp_rocessed': {'ext': '.pitchSilIntrpPP', 'replace': ['audio', 'features']},
				'tonic': {'ext': '.tonic', 'replace': ['audio', 'features']},
				'tonic_fine_tuned': {'ext': '.tonicFine', 'replace': ['audio', 'features']},
				'nyas_segments': {'ext': '.flatSegNyas', 'replace': ['audio', 'features']}
				}

	for k in sources.keys():
		nfiles, npresent = verify_melodic_similarity_dataset_files(filelist_carnatic, root_dir, sources[k]['ext'], sources[k]['replace'])
		fid.write("%s\t%d\t%d\n"%(k, nfiles, npresent))


	fid.write("\n\n\nThis is  for the Hindustani music dataset\n\n")	

	
	sources = {
				'audio': {'ext': '.wav', 'replace': ['audio', 'audio']},
				'annotations_original': {'ext': '.anot', 'replace': ['audio', 'annotations_orig']},
				'annotations_impr': {'ext': '.anotEdit4', 'replace': ['audio', 'annotations_impr']},
				'pitch': {'ext': '.tpe', 'replace': ['audio', 'features']},
				'pitch_postp_rocessed': {'ext': '.tpe5msSilIntrpPP', 'replace': ['audio', 'features']},
				'tonic': {'ext': '.tonic', 'replace': ['audio', 'features']},
				'tonic_fine_tuned': {'ext': '.tonicFine', 'replace': ['audio', 'features']},
				'nyas_segments': {'ext': '.flatSegNyas', 'replace': ['audio', 'features']}
				}

	for k in sources.keys():
		nfiles, npresent = verify_melodic_similarity_dataset_files(filelist_hindustani, root_dir, sources[k]['ext'], sources[k]['replace'])
		fid.write("%s\t%d\t%d\n"%(k, nfiles, npresent))




	fid.close()



