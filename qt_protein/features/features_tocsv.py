#!usr/bin/env Python
#coding:utf-8

from numpy import *
import numpy as np
import random
import csv
import pandas as pd


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

def main(norma_flag,data_file,output_dir,features_flag):
    with open(output_dir+'/features_'+str(features_flag)+'.csv','w',newline='') as wf:
        writer=csv.writer(wf)
        CountOfAAInPeptide=''
        CountOfAAInYion=''
        CountOfAAInBion=''
        IsolationWidth=''
        C_Identity=''
        N_Identity=''
        for i in range(1,21):
            CountOfAAInPeptide+='CountOfAAInPeptide_'+str(i)+','
            CountOfAAInYion+='CountOfAAInYion_'+str(i)+','
            CountOfAAInBion+='CountOfAAInBion_'+str(i)+','
            C_Identity+='C_Identity_'+str(i)+','
            N_Identity+='N_Identity_'+str(i)+','
        for i in range(6):
            for j in range(1,21):
                IsolationWidth+='IsolationWidth_'+str(i+1)+"_"+str(j)+','
        writeStr='IsTheSamePort,RatioOfyAndPeptide,RatioOfbAndPeptide,y_Distance,b_Distance,R_Basicity,L_Basicity,R_Helicity,L_Helicity,R_Hydrophobicity,L_Hydrophobicity,y_Basic,b_Basic,y_Helicity,b_Helicity,y_Hydrophobicity,b_Hydrophobicity,AvgOfBasic,DvalueOfBasic,AvgOfHelicity,DvalueOfHelicity,AvgOfHydrophobicity,DvalueOfHydrophobicity,y_Mass,b_Mass,DvalueOfMcratioOfyAndPep,CountOfBasicAA,y_CountOfBasicAA,b_CountOfBasicAA,LengthOfPeptide,P_Basic,P_Helicity,P_Hydrophobicity,McRatioOfPeptide,Isy,Intensity'
        if features_flag == 35:
            writeStr='Number,Peptide,'+writeStr
        elif features_flag==195:
            writeStr='Number,Peptide,'+IsolationWidth+C_Identity+N_Identity+writeStr
        elif features_flag==220:
             writeStr='Number,Peptide,'+CountOfAAInPeptide+CountOfAAInYion+CountOfAAInBion+IsolationWidth+C_Identity+N_Identity
        elif features_flag ==255:
             writeStr='Number,Peptide,'+CountOfAAInPeptide+CountOfAAInYion+CountOfAAInBion+IsolationWidth+C_Identity+N_Identity+writeStr
        writer.writerow(writeStr.split(','))
        cunt=0
        f = open(data_file,'r')
        data = [];pep_mz = 0;pep = '1';pep_b = 0;pep_he = 0;pep_hy=0
        for line in f:
            flag=False
            try:
                attribute = zeros(255)
                f_line = line.split('\t')
                peptide = list(f_line[0])
                ion = list(f_line[2])
                i = 0
                ion_format = f_line[5]
                #???????а??????ĸ???
                for key in dicS.keys():
                    if key in peptide:
                        attribute[dicS[key]] = peptide.count(key)

              
                #???Ѵ??ڣ?size=3

                ion_format = f_line[5]
                if len(ion) > 3 and len(ion) < len(peptide) - 3 and ion_format[0] == 'y':
                    j = 0
                    for i in range(len(peptide) - len(ion) - 3,len(peptide) - len(ion)+3):
                        attribute[60 + 20*j+dicS[peptide[i]]] = 1
                        j += 1
                elif len(ion) > 3 and len(ion) < len(peptide) - 3 and ion_format[0] == 'b':
                    j = 0
                    for i in range(len(ion) - 3,len(ion) + 3):
                        attribute[60 + j*20+dicS[peptide[i]]] = 1
                        j += 1
                elif (len(ion) <= 3 and ion_format[0] == 'y') or (len(ion) >= len(peptide) - 3 and ion_format[0] == 'b'):
                    j = 0
                    if len(ion) == 1 or len(ion) == len(peptide) - 1:
                        for i in range(len(peptide) - 4,len(peptide)):
                            attribute[60 + 20*j + dicS[peptide[i]]] = 1
                            j += 1
                    elif len(ion) == 2 or len(ion) == len(peptide) - 2:
                        for i in range(len(peptide) - 5,len(peptide)):
                            attribute[60 + 20*j + dicS[peptide[i]]] = 1
                            j += 1
                    else:    
                        for i in range(len(peptide) - 6,len(peptide)):
                            attribute[60 + 20*j + dicS[peptide[i]]] = 1
                            j += 1
                elif (len(ion) <= 3 and ion_format[0] == 'b') or (len(ion) >= len(peptide) - 3 and ion_format[0] == 'y'):
                    if len(ion) == 1 or len(ion) == len(peptide) - 1:
                        j = 2
                        for i in range(4):
                           attribute[60 + j*20+dicS[peptide[i]]] = 1
                           j += 1
                    elif len(ion) == 2 or len(ion) == len(peptide) - 2:
                        j = 1
                        for i in range(5):
                           attribute[60 + j*20+dicS[peptide[i]]] = 1
                           j += 1   
                    else:
                        for i in range(6):
                            attribute[60 + i*20+dicS[peptide[i]]] = 1

                
                #y/b?????а??????ĸ???

                for key in dicS.keys():
                    if key in ion:
                        attribute[20 + dicS[key]] = ion.count(key)

                if ion_format[0] == 'y':        
                    other_ion = peptide[:len(peptide) - len(ion)]
                else:
                    other_ion = peptide[len(ion):]
                for key in dicS.keys():
                    if key in other_ion:
                        attribute[40 + dicS[key]] = other_ion.count(key)
                        
                
                #C/N???ĵ?????

                attribute[180 + dicS[peptide[0]]] = 1
                attribute[200 + dicS[peptide[-1]]] = 1

                
                #???ѵ??Ƿ????ĵ?һ??

                if len(ion) == 1:
                    attribute[220] = 1

                
                #?????ĵ??????????ԡ???ˮ?ԡ???????

                if pep != peptide:
                    pep_mz = 20.0;pep_b = 0.0;pep = peptide;pep_he = 0;pep_hy=0
                    for i in range(len(peptide)):
                        pep_mz += dicM[peptide[i]]
                        pep_b += dicB[peptide[i]]
                        pep_he += dicHe[peptide[i]]
                        pep_hy += dicHy[peptide[i]]

                
                #??????Ƭ???ӵ??????????ԡ???ˮ?ԡ???????

                ion_mz = 19.0;ion_b = 0.0;ion_he=0;ion_hy=0
                for i in range(len(ion)):
                    ion_mz += dicM[ion[i]]
                    ion_b += dicB[ion[i]]
                    ion_he += dicHe[ion[i]]
                    ion_hy += dicHy[ion[i]]

                if ion_format[0] == 'y':
                    #b/y???ӵ??????????????ı?
                    attribute[221] = ion_mz / pep_mz
                    attribute[222] = 1 - attribute[221]
                    
                    
                    #???ѵ?????C/N?˵ľ???

                    attribute[224] = len(ion)
                    attribute[223] = len(peptide) - len(ion)
                    
                    
                    #???ѵ????????????ļ??ԡ??????ԡ???ˮ??

                    attribute[225] = dicB[peptide[-len(ion)]]
                    attribute[226] = dicB[peptide[-len(ion) - 1]]
                    attribute[227] = dicHe[peptide[-len(ion)]]
                    attribute[228] = dicHe[peptide[-len(ion) - 1]]
                    attribute[229] = dicHy[peptide[-len(ion)]]
                    attribute[230] = dicHy[peptide[-len(ion) - 1]]

                    
                    #b/y???ӵļ??ԡ??????ԡ???ˮ??

                    attribute[231] = ion_b
                    attribute[232] = pep_b - ion_b
                    attribute[233] = ion_he
                    attribute[234] = pep_he - ion_he
                    attribute[235] = ion_hy
                    attribute[236] = pep_hy - ion_hy

                    
                    #??????Ƭ???ӵ????? 

                    attribute[243] = ion_mz
                    attribute[244] = pep_mz - ion_mz
                else:
                    #b/y???ӵ??????????????ı?
                    attribute[222] = ion_mz / pep_mz
                    attribute[221] = 1 - attribute[222]
                    
                    
                    #???ѵ?????C/N?˵ľ???

                    attribute[223] = len(ion)
                    attribute[224] = len(peptide) - len(ion)

                    
                    #???ѵ????????????ļ??ԡ??????ԡ???ˮ??

                    attribute[225] = dicB[peptide[len(ion)]]
                    attribute[226] = dicB[peptide[len(ion) - 1]]
                    attribute[227] = dicHe[peptide[len(ion)]]
                    attribute[228] = dicHe[peptide[len(ion) - 1]]
                    attribute[229] = dicHy[peptide[len(ion)]]
                    attribute[230] = dicHy[peptide[len(ion) - 1]]

                    #b/y???ӵļ??ԡ??????ԡ???ˮ??
                    attribute[232] = ion_b
                    attribute[231] = pep_b - ion_b
                    attribute[234] = ion_he
                    attribute[233] = pep_he - ion_he
                    attribute[236] = ion_hy
                    attribute[235] = pep_hy - ion_hy

                    #??????Ƭ???ӵ?????
                    attribute[244] = ion_mz
                    attribute[243] = pep_mz - ion_mz

                 #???ѵ????????????ļ??ԡ??????ԡ???ˮ?ԵĲ?ֵ?;?ֵ
                attribute[237] = (attribute[225] + attribute[226]) / 2.0
                attribute[238] = abs(attribute[225] - attribute[226])
                attribute[239] = (attribute[227] + attribute[228]) / 2.0
                attribute[240] = abs(attribute[227] - attribute[228])
                attribute[241] = (attribute[229] + attribute[230]) / 2.0
                attribute[242] = abs(attribute[229] - attribute[230])

               
                #Y???ӵ??ʺɱȼ?ȥ?ĵ??ʺɱ?

                attribute[245] = pep_mz - (ion_mz)/2.0
                
                
                #??/??????Ƭ?м??԰??????ĸ???

                attribute[246] = peptide.count('K') + peptide.count("R") + peptide.count('H')
                attribute[247] = ion.count('K') + ion.count('R') + ion.count('H')
                attribute[248] = attribute[246] - attribute[247]
               
                 #?????еĳ???
                attribute[249] = len(peptide)

                #?ĵļ??ԡ???ˮ?ԡ???????
                attribute[250] = pep_b
                attribute[251] = pep_he
                attribute[252] = pep_hy

                #?ĵ??ʺɱ?
                attribute[253] = pep_mz / 2.0

                if ion_format[0] == 'y':
                    attribute[254]=1
                cunt += 1
                flag=True
               
            except:
                print('catch error in' + str(cunt)+' line')
            if flag:
                if features_flag == 35:
                    data=attribute[220:].tolist()
                elif features_flag==195:
                    data=attribute[60:].tolist()
                elif features_flag==220:
                    data=attribute[0:221].tolist()
                elif features_flag ==255:
                    data=attribute.tolist()
                data.insert(0,cunt)
                data.insert(1,f_line[0])
                data.append(float(f_line[6].split('\n')[0]))
                writer.writerow(data)
                print('write '+str(cunt)+' line in file')
        f.close()
    wf.close()
    if norma_flag == 1:
        normalize(output_dir,features_flag)
    else:
        print('complete')
def normalize(output_dir,features_flag):
    reader=pd.read_csv(output_dir+'/features_'+str(features_flag)+'.csv')
    fftile=[]
    if features_flag == 35:
        titles=reader.columns[5:36]
        fftile=titles
    elif features_flag==195:
        titles=reader.columns[165:196]
        fftile=titles
    elif features_flag==220:
        titles=reader.columns[2:62]
        fftile=titles
    elif features_flag ==255:
        titles=reader.columns[2:256]
        for ftile  in range(0,60):
            fftile.append(titles[ftile])

        for ftile  in range(223,len(titles)):
            fftile.append(titles[ftile])
    
    for title in fftile:
        column=reader[str(title)]
        max_x=max(column)
        min_x=min(column)
        devalue=float(max_x-min_x)
        reader[str(title)]=(reader[str(title)]-min_x)/devalue
        
        print('alter ('+ str(title) +')')
    reader.to_csv(output_dir+'/features_'+str(features_flag)+'_normalized.csv',index=False)
    print('complete')