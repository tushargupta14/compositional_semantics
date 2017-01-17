import readline
import numpy as np
from rpy2.robjects import r
import pandas.rpy.common as com
from pandas import DataFrame

'''
source = np.load('source_350_X.npy')
#derived = np.load('derived_350_Y.npy')

source_df = DataFrame(source)
derived_df = DataFrame(derived)
source_df = com.convert_to_r_dataframe(source_df)
derived_df = com.convert_to_r_dataframe(derived_df)
r.assign("source_foo", source_df)
r("save(source_foo, file='/home/du3/13CS30045/affix_final/plsr_new/pls/data/source_350.gzip', compress=TRUE)")
r.assign("derived_foo",derived_df)
r("save(derived_foo, file='/home/du3/13CS30045/affix_final/plsr_new/pls/data/derived_350.gzip' , compress=TRUE)")

'''

temp = np.load("test_mat.npy")

temp_df = DataFrame(temp)
temp_df = com.convert_to_r_dataframe(temp_df)
r.assign("temp_df",temp_df)
r("save(temp_df,file = '/home/du3/13CS30045/affix_final/plsr_new/pls/data/temp_350.gzip',compress=TRUE)")



