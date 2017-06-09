import features.features_tocsv as fft 
import features.features_tocsv_43 as f43

def main(func,feature_flag,normalize_flag,data_file,output_dir):
    print(feature_flag,normalize_flag,data_file,output_dir)
   
    if feature_flag == 43:
        f43.main(normalize_flag,data_file,output_dir)
    else:
        fft.main(normalize_flag,data_file,output_dir,feature_flag)
    