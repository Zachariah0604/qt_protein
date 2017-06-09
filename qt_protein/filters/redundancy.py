from filters.tri_result import *
def main(input_file,output_dir):
    total_list=[]
    with open(input_file,'r') as rf:
        rf.readline()
        while True:
            line =rf.readline()
            if not line:
                break
            list_=line.split()
            temp=[]
            temp.append(list_[0])
            temp.append(list_[1])
            temp.append(list_[4])
            temp.append(list_[5].strip('\n'))
            total_list.append(temp)
    dic=get_spectrum_dict(total_list)
    get_redundancy(dic,output_dir+'/redundancy.txt')
    print('complete')