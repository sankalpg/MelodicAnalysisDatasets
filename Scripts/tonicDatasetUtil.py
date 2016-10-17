import os, sys
import numpy
import json
import time


def verify_tonic_dataset_files(dataset_file, root_dir, ext, replace_str):
	"""
	This function check for annotation and audio files for the dataset specified in the tsv file. Remember the dataset file provides a relative path, that's why we need a root directory to access the files
	Input:
		dataset_file: json file containing dataset info
		root_dir: root directory where the dataset is stored
		dataset_type: 'cm' or 'iitm' or 'iisc' this info is neeed to interpret the json. Because in datasets other than cm keys of the dictionary are file paths
		replace_str: if in the path something has to be replaced for example audio with features?
	Output: 
		Number of total files, number of files present
	"""

	#reading the dataset file
	dataset = json.load(open(dataset_file, 'r'))
	files_present = 0
	files_absent = 0
	for k in dataset.keys():
		audiopath = dataset[k]['filepath']
		fname, ext_temp = os.path.splitext(audiopath)
		fname = fname.replace(replace_str[0], replace_str[1])
		if os.path.isfile(os.path.join(root_dir, fname + ext)):
			files_present += 1
		else:
			print os.path.join(root_dir, fname + ext)
			files_absent += 1

	return files_present + files_absent, files_present




def convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict='cm'):
	"""
	Does exactly what the name says!

	if type_dict='cm': generated json has mbids as keys, if type_dict='iitm' or type_dict='iisc' then generated jsons have filepaths as the keys
	"""	

	lines = open(tsv_input, 'r').readlines()

	output = {}
	for line in lines[1:]:			#leaving first line, assuming that it contains header
		sline = line.split('\t')
		sline = [s.strip() for s in sline]
		key = sline[0]
		if type_dict == 'cm':
			mbid = os.path.basename(sline[0]).split('_')[0].strip()			
		else:
			mbid = -1
		output[key] = {'mbid':mbid, 'filepath':sline[0], 'tonic':float(sline[1]), 'tradition': sline[2], 'artist': sline[3], 'gender': sline[4], 'type':sline[5]}
	json.dump(output, open(json_output, 'w'))






# ------------------------ These functions are super hard coded functions and are not meant to be reused, they were required for compiling the dataset in new format --------------------

def batch_covert_tsv_to_json():
	"""
	Super hard coded function, maybe not reusable
	"""

# ----------------------- JNMR datasets----------------------

	tsv_input = '../TonicDataset/datasets/JNMR2014/CM/CM1.tsv'
	json_output = '../TonicDataset/datasets/JNMR2014/CM/CM1.json'
	type_dict='cm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)

	tsv_input = '../TonicDataset/datasets/JNMR2014/CM/CM2.tsv'
	json_output = '../TonicDataset/datasets/JNMR2014/CM/CM2.json'
	type_dict='cm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)	

	tsv_input = '../TonicDataset/datasets/JNMR2014/CM/CM3.tsv'
	json_output = '../TonicDataset/datasets/JNMR2014/CM/CM3.json'
	type_dict='cm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)


	tsv_input = '../TonicDataset/datasets/JNMR2014/IITM/IITM1.tsv'
	json_output = '../TonicDataset/datasets/JNMR2014/IITM/IITM1.json'
	type_dict='iitm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)

	tsv_input = '../TonicDataset/datasets/JNMR2014/IITM/IITM2.tsv'
	json_output = '../TonicDataset/datasets/JNMR2014/IITM/IITM2.json'
	type_dict='iitm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)	

	tsv_input = '../TonicDataset/datasets/JNMR2014/IISc/IISc.tsv'
	json_output = '../TonicDataset/datasets/JNMR2014/IISc/IISc.json'
	type_dict='iisc'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)	


# --------------------------- Other datasets -------------------------

	tsv_input = '../TonicDataset/datasets/ISMIR2012/ISMIR2012.tsv'
	json_output = '../TonicDataset/datasets/ISMIR2012/ISMIR2012.json'
	type_dict='cm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)	

	tsv_input = '../TonicDataset/datasets/CompMusicWorkshop2012/Info_file_237.tsv'
	json_output = '../TonicDataset/datasets/CompMusicWorkshop2012/Info_file_237.json'
	type_dict='cm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)		

	tsv_input = '../TonicDataset/datasets/CompMusicWorkshop2012/Info_file_540.tsv'
	json_output = '../TonicDataset/datasets/CompMusicWorkshop2012/Info_file_540.json'
	type_dict='cm'
	convert_tsv_to_json_tonic_dataset(tsv_input, json_output, type_dict)	


def batch_verify_tonic_datasets():

	report_file = '/media/sankalp/Work1/PHD_structured/Datasets/TonicDataset/report.txt'

	fid = open(report_file,'w')
	fid.write("This report is generated on %s\t\n\n"%time.strftime("%x"))
	fid.write("This is an automatically generated report. It contains information about the verification of the datasets, we check each an every file related with the dataset and summarize the results in this file.\n\n")

	fid.write("Format: %s\t%s\t%s\n\n\n"%('extension', 'total files', 'files present'))	

	paths = [
				{'name': 'CM1', 'db_path': '../TonicDataset/datasets/JNMR2014/CM/CM1.json', 'source_root': '../'},
				{'name': 'CM2', 'db_path': '../TonicDataset/datasets/JNMR2014/CM/CM2.json', 'source_root': '../'},
				{'name': 'CM3', 'db_path': '../TonicDataset/datasets/JNMR2014/CM/CM3.json', 'source_root': '../'},
				{'name': 'IITM2', 'db_path': '../TonicDataset/datasets/JNMR2014/IITM/IITM2.json', 'source_root': '../'},
				{'name': 'IISc', 'db_path': '../TonicDataset/datasets/JNMR2014/IISc/IISc.json', 'source_root': '../'},
				{'name': 'ISMIR2012', 'db_path': '../TonicDataset/datasets/ISMIR2012/ISMIR2012.json', 'source_root': '../'}
			]

	sources = {
				'audio': {'ext': '.mp3', 'replace': ['audio', 'audio']},
				'multipitch-hist': {'ext': '.mph.txt', 'replace': ['audio', 'features']},
				'pitch-hist': {'ext': '.ph.txt', 'replace': ['audio', 'features']},
				'pitch': {'ext': '.pit.txt', 'replace': ['audio', 'features']}
				}

	for path in paths:
		fid.write("####################  %s ###########################\n"%(path['name']))	
		for source_key in sources.keys():
			file_info = {'name': path['name'], 'db_path': path['db_path'], 'source_path': path['source_root'], 'source_ext': sources[source_key]['ext']}
			nfiles, npresent = verify_tonic_dataset_files(file_info['db_path'], file_info['source_path'], file_info['source_ext'], sources[source_key]['replace'])
			fid.write("%s\t%d\t%d\n"%(file_info['source_ext'], nfiles, npresent))

	fid.close()



