#coding:utf-8
from numpy import *
import numpy as np
import random
import csv
import pandas as pd
"""
feature choose,a 25d vector indicate the number of ACDEFGHIKLMNPQRSTVWYcnm(DN)(AN),
23d vector indicate the animo acid,a window of cleavage 4,4*23+2,2 indicate N-term modification,
4d vector indicate the charge of peptide sequence.
"""

dicB={'A':206.4,'c':206.2,'D':208.6,'E':215.6,'F':212.1,\
      'G':202.7,'H':223.7,'I':210.8,'K':221.8,'L':209.6,\
      'M':213.3,'N':212.8,'P':214.4,'Q':214.2,'R':237.0,\
      'S':207.6,'T':211.7,'V':208.7,'W':216.1,'Y':213.1}
dicM={'A':71.03711,'c':160.03065,'D':115.02694,'E':129.04259,'F':147.06841,\
      'G':57.02146,'H':137.05891,'I':113.08406,'K':128.09496,'L':113.08406,\
      'M':131.04048,'N':114.04293,'P':97.05276,'Q':128.05858,'R':156.10111,\
      'S':87.03203,'T':101.04768,'V':99.06841,'W':186.07931,'Y':163.06332}
dicS={'A':0,'c':1,'D':2,'E':3,'F':4,'G':5,'H':6,'I':7,\
      'K':8,'L':9,'M':10,'N':11,'P':12,'Q':13,'R':14,\
      'S':15,'T':16,'V':17,'W':18,'Y':19}
dicHe={'A':1.24,'c':0.79,'D':0.89,'E':0.85,'F':1.26,'G':1.15,'H':0.97,\
       'I':1.29,'K':0.88,'L':1.28,'M':1.22,'N':0.94,'P':0.57,'Q':0.96,\
       'R':0.95,'S':1.00,'T':1.09,'V':1.27,'W':1.07,'Y':1.11}
dicHy={'A':0.16,'c':2.50,'D':-2.49,'E':-1.50,'F':5.00,'G':-3.31,'H':-4.63,'I':4.41,
      'K':-5.00,'L':4.76,'M':3.23,'N':-3.79,'P':-4.92,'Q':-2.76,'R':-2.77,'S':-2.85,
      'T':-1.08,'V':3.02,'W':4.88,'Y':2.00}

def main(norma_flag,data_file,output_dir):
    with open(output_dir+'/features_43.csv','w',newline='') as wf:
        writer=csv.writer(wf)
       
        writeStr='Number,Peptide,IsolationWidth_1,IsolationWidth_2,IsolationWidth_3,IsolationWidth_4,IsolationWidth_5,IsolationWidth_6,C_Identity,N_Identity,IsTheSamePort,RatioOfyAndPeptide,RatioOfbAndPeptide,y_Distance,b_Distance,R_Basicity,L_Basicity,R_Helicity,L_Helicity,R_Hydrophobicity,L_Hydrophobicity,y_Basic,b_Basic,y_Helicity,b_Helicity,y_Hydrophobicity,b_Hydrophobicity,AvgOfBasic,DvalueOfBasic,AvgOfHelicity,DvalueOfHelicity,AvgOfHydrophobicity,DvalueOfHydrophobicity,y_Mass,b_Mass,DvalueOfMcratioOfyAndPep,CountOfBasicAA,y_CountOfBasicAA,b_CountOfBasicAA,LengthOfPeptide,P_Basic,P_Helicity,P_Hydrophobicity,McRatioOfPeptide,Isy,Intensity'
        writer.writerow(writeStr.split(','))
        cunt=0
        f = open(data_file,'r')
        data = [];pep_mz = 0;pep = '1';pep_b = 0;pep_he = 0;pep_hy=0
        for line in f:
            flag=False
            try:
                attribute = zeros(43)
                f_line = line.split('\t')
                peptide = list(f_line[0])
                ion = list(f_line[2])
                i = 0
                ion_format = f_line[5]

                ion_format = f_line[5]

                if len(ion) > 3 and len(ion) < len(peptide) - 3 and ion_format[0] == 'y':
                    j = 0
                    for i in range(len(peptide) - len(ion) - 3,len(peptide) - len(ion)+3):
                        attribute[j] = dicS[peptide[i]]
                        j += 1
                elif len(ion) > 3 and len(ion) < len(peptide) - 3 and ion_format[0] == 'b':
                    j = 0
                    for i in range(len(ion) - 3,len(ion) + 3):
                        attribute[j] = dicS[peptide[i]]
                        j += 1
                elif (len(ion) <= 3 and ion_format[0] == 'y') or (len(ion) >= len(peptide) - 3 and ion_format[0] == 'b'):
                    j = 0
                    if len(ion) == 1 or len(ion) == len(peptide) - 1:
                        for i in range(len(peptide) - 4,len(peptide)):
                            attribute[j]= dicS[peptide[i]]
                            j += 1
                    elif len(ion) == 2 or len(ion) == len(peptide) - 2:
                        for i in range(len(peptide) - 5,len(peptide)):
                            attribute[j] = dicS[peptide[i]]
                            j += 1
                    else:    
                        for i in range(len(peptide) - 6,len(peptide)):
                            attribute[j] = dicS[peptide[i]]
                            j += 1
                elif (len(ion) <= 3 and ion_format[0] == 'b') or (len(ion) >= len(peptide) - 3 and ion_format[0] == 'y'):
                    if len(ion) == 1 or len(ion) == len(peptide) - 1:
                        j = 2
                        for i in range(4):
                           attribute[j] = dicS[peptide[i]]
                           j += 1
                    elif len(ion) == 2 or len(ion) == len(peptide) - 2:
                        j = 1
                        for i in range(5):
                           attribute[j] = dicS[peptide[i]]
                           j += 1   
                    else:
                        for i in range(6):
                            attribute[j] = dicS[peptide[i]]

               
                attribute[6] = dicS[peptide[0]]
                attribute[7] = dicS[peptide[-1]]

                if len(ion) == 1:
                    attribute[8] = True
                else:
                    attribute[8] = False

                if pep != peptide:
                    pep_mz = 20.0;pep_b = 0.0;pep = peptide;pep_he = 0;pep_hy=0
                    for i in range(len(peptide)):
                        pep_mz += dicM[peptide[i]]
                        pep_b += dicB[peptide[i]]
                        pep_he += dicHe[peptide[i]]
                        pep_hy += dicHy[peptide[i]]

                ion_mz = 19.0;ion_b = 0.0;ion_he=0;ion_hy=0
                for i in range(len(ion)):
                    ion_mz += dicM[ion[i]]
                    ion_b += dicB[ion[i]]
                    ion_he += dicHe[ion[i]]
                    ion_hy += dicHy[ion[i]]

                if ion_format[0] == 'y':
                    attribute[9] = ion_mz / pep_mz
                    attribute[10] = 1 - attribute[7]
                    
                    attribute[11] = len(ion)
                    attribute[12] = len(peptide) - len(ion)
                    
                    attribute[13] = dicB[peptide[-len(ion)]]
                    attribute[14] = dicB[peptide[-len(ion) - 1]]
                    attribute[15] = dicHe[peptide[-len(ion)]]
                    attribute[16] = dicHe[peptide[-len(ion) - 1]]
                    attribute[17] = dicHy[peptide[-len(ion)]]
                    attribute[18] = dicHy[peptide[-len(ion) - 1]]

                    attribute[19] = ion_b
                    attribute[20] = pep_b - ion_b
                    attribute[21] = ion_he
                    attribute[22] = pep_he - ion_he
                    attribute[23] = ion_hy
                    attribute[24] = pep_hy - ion_hy

                    attribute[31] = ion_mz
                    attribute[32] = pep_mz - ion_mz
                else:
                    attribute[10] = ion_mz / pep_mz
                    attribute[9] = 1 - attribute[8]
                    
                    attribute[11] = len(ion)
                    attribute[12] = len(peptide) - len(ion)

                    attribute[13] = dicB[peptide[len(ion)]]
                    attribute[14] = dicB[peptide[len(ion) - 1]]
                    attribute[15] = dicHe[peptide[len(ion)]]
                    attribute[16] = dicHe[peptide[len(ion) - 1]]
                    attribute[17] = dicHy[peptide[len(ion)]]
                    attribute[18] = dicHy[peptide[len(ion) - 1]]

                    attribute[20] = ion_b
                    attribute[19] = pep_b - ion_b
                    attribute[22] = ion_he
                    attribute[21] = pep_he - ion_he
                    attribute[24] = ion_hy
                    attribute[23] = pep_hy - ion_hy

                    attribute[32] = ion_mz
                    attribute[31] = pep_mz - ion_mz

                attribute[25] = (attribute[13] + attribute[14]) / 2.0
                attribute[26] = abs(attribute[13] - attribute[14])
                attribute[27] = (attribute[15] + attribute[16]) / 2.0
                attribute[28] = abs(attribute[15] - attribute[16])
                attribute[29] = (attribute[17] + attribute[18]) / 2.0
                attribute[30] = abs(attribute[17] - attribute[18])

                attribute[33] = pep_mz - (ion_mz)/2.0
                
                attribute[34] = peptide.count('K') + peptide.count("R") + peptide.count('H')
                attribute[35] = ion.count('K') + ion.count('R') + ion.count('H')
                attribute[36] = attribute[34] - attribute[35]

                attribute[37] = len(peptide)

                attribute[38] = pep_b
                attribute[39] = pep_he
                attribute[40] = pep_hy

                attribute[41] = pep_mz / 2.0
                if ion_format[0] == 'y':
                    attribute[42]=1
                cunt += 1
                flag=True
            except:
                print('catch error in' + str(cunt)+' line')
            if flag:
                data=attribute.tolist()
                data.insert(0,cunt)
                data.insert(1,f_line[0])
                data.append(float(f_line[6].split('\n')[0]))
                writer.writerow(data)
                print('write '+str(cunt)+' line in file')
        f.close()
    wf.close()
    if norma_flag == 1:
        normalize(output_dir)
    else:
        print('complete')
def normalize(output_dir):
    reader=pd.read_csv(output_dir+'/features_43.csv')
    titles=reader.columns[5:44]
    
    print(titles)
    for title in titles:
        column=reader[str(title)]
        max_x=max(column)
        min_x=min(column)
        devalue=float(max_x-min_x)
        reader[str(title)]=(reader[str(title)]-min_x)/devalue
       
        print('alter ('+ str(title) +')')
    reader.to_csv(output_dir+'/features_43_normalized.csv',index=False)
    print('complete')
