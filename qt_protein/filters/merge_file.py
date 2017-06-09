from filters.exclude_pif import *
def merge(output_dir,input_dir):
    writeFile=open(output_dir+'/merge_file.txt','w')
    paths=folder(input_dir)
    print(paths)
    pfind_index=[u for u,v in enumerate(paths) if 'pfind' in v ]
    print(pfind_index)
    for spath in paths:
        with open(spath,'r') as pf:
            pf.readline()
            while True:
                line = pf.readline()
                if not line :
                    break
                if 'pfind_' in spath:
                    write_str=line.split()[0]+'\t'+line.split()[1]+'\t'+line.split()[4]+'\t'+line.split()[5]+'\n'
                else:
                    write_str=(line.split()[0]+'\t'+line.split()[1])+'\n'
                writeFile.write(write_str)
            pf.close()
        print('merge compelte')
    writeFile.close()
    return pfind_index[0]