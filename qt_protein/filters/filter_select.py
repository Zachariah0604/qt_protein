import filters.pfind_filter as fpf
import filters.mascot_filter as fmf
import filters.coment_filter as fcf
import filters.exclude_pif as fex

def main(func,filter_flag,input_dir,output_dir,fdr):
    
    paths=fex.folder(input_dir)
    if filter_flag == 1:
        writeFile=open(output_dir+'/filter_pfind_result.txt','w')
        writeFile.write('Spectrum\tPeptide\tMod_Sites\tProteins\tEvalue\tCharge\n')
        writeFile.close()
        for spath in paths:
            fpf.main(spath,output_dir,fdr)
            print(spath+' Complete filtration')
        print('complete')
    elif filter_flag ==2:
        writeFile=open(output_dir+'/filter_mascot_result.txt','w')
        writeFile.write('Spectrum\tPeptide\tMod_Sites\tProteins\tEvalue\tCharge\n')
        writeFile.close()
        for spath in paths:
            fmf.main(spath,output_dir,fdr)
            print(spath+' Complete filtration')
        print('complete')
    elif filter_flag ==3:
        writeFile=open(output_dir+'/filter_coment_result.txt','w')
        writeFile.write('Spectrum\tPeptide\tMod_Sites\tProteins\tEvalue\tCharge\n')
        writeFile.close()
        for spath in paths:
            fcf.main(spath,output_dir,fdr)
            print(spath+' Complete filtration')
        print('complete')
   
