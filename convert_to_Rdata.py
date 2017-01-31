# Stores the matrices in R format for loading in the model. This script is called from the implement plsr model 

import readline
import numpy as np
from rpy2.robjects import r
import pandas.rpy.common as com
from pandas import DataFrame


def convert_to_Rdata(affix,source,derived):


	target_path = '/home/du3/13CS30045/affix_final/plsr_new/pls/data/lexfunc_model_input/'
	#source = np.load(path_to_files+affix+'_source_350_X.npy')
	#derived = np.load(path_to_files+affix+'_derived_350_Y.npy')

	source_df = DataFrame(source)
	derived_df = DataFrame(derived)
	source_df = com.convert_to_r_dataframe(source_df)
	derived_df = com.convert_to_r_dataframe(derived_df)
	strs_temp = affix+'_source_foo'
	r.assign(strs_temp, source_df)
	#r.assign("target",file_source)
	#r.assign("r_affix",affix)	
	file_source = "/home/du3/13CS30045/affix_final/plsr_new/pls/data/lexfunc_model_input/"+affix+"_source_350.gzip"
	#print file_source
	#r.assign("target",file_source)
	#file_source = affix+"_source_350.gzip"
	save_exp = "save("+affix+"_source_foo,file ='"+ file_source +"' ,compress=TRUE)"
	r(save_exp)
	strs_temp = affix+'_derived_foo'
	r.assign(strs_temp,derived_df)
	#r.assign("r_affix",)
	file_derived = "/home/du3/13CS30045/affix_final/plsr_new/pls/data/lexfunc_model_input/"+affix+"_derived_350.gzip"
	#file_derived = affix+"_derived_350.gzip"
	#r.assign("target",file_source)
	save_exp = "save("+affix+"_derived_foo, file='"+ file_derived +"', compress=TRUE)"
	r(save_exp)


#temp = np.load("test_mat.npy")

#temp_df = DataFrame(temp)
#temp_df = com.convert_to_r_dataframe(temp_df)
#r.assign("temp_df",temp_df)
#r("save(temp_df,file = '/home/du3/13CS30045/affix_final/plsr_new/pls/data/temp_350.gzip',compress=TRUE)")


if __name__== "__main__":
	
	convert_to_Rdata()
