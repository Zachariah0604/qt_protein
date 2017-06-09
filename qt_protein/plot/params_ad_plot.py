import numpy as np
import matplotlib.pyplot as plt
def single_var(data_file,x_coordinate,x_limit,x_lower,y_limit,y_lower):
    
    with open(data_file,'r') as rf:
        x=[]
        pcc=[]
        max_pcc=0.0
        max_of_x=0
        while True:
            line = rf.readline()
            if not line:
                break
            list_=line.split()
            if float(list_[1]) > float(max_pcc):
                    max_pcc =list_[1]
                    max_of_x=list_[0]
            x.append(list_[0])
            pcc.append(list_[1])
       
        plt.plot(x,pcc,lw=1.5)
        x1=[float(x_lower),float(max_of_x)]
        y1=[max_pcc,max_pcc]
        x2=[float(max_of_x),float(max_of_x)]
        y2=[float(y_lower),max_pcc]
        plt.plot(x1,y1,marker='x',linestyle='--',color='black')
        plt.plot(x2,y2,marker='x',linestyle='--',color='black')
        plt.annotate("("+str(max_of_x)+","+str(max_pcc)+")",xy=(float(max_of_x),max_pcc),xytext=(float(max_of_x),float(float(max_pcc)-0.05)),arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"))

       
        plt.xlabel(str(x_coordinate))
        plt.ylabel('pcc')
        plt.xlim(float(x_lower),float(x_limit))
        plt.ylim(float(y_lower),float(y_limit))
        plt.show()
def double_var(data_file,x_coordinate,z_coordinate,x_count,z_count,x_limit,x_lower,y_limit,y_lower):
    with open(data_file,'r') as rf:
        cunt=0
        max_pcc=0.0
        max_of_x=0
        max_of_z=0
        while cunt<int(z_count):
            
            cunt+=1
            pear=[]
            x=[]
            for j in range(int(x_count)):
                line=rf.readline()
                if not line:
                    break
                list=line.split()
                if float(list[2]) > float(max_pcc):
                    max_pcc =list[2]
                    max_of_x=list[1]
                    max_of_z=list[0]
                pear.append(list[2])
                x.append(list[1])
                z=list[0]
            plt.plot(x,pear,lw=1.5,label=str(z_coordinate)+'='+str(z))
        plt.legend(loc='lower right')
        x1=[int(x_lower),int(max_of_x)]
        y1=[max_pcc,max_pcc]
        x2=[int(max_of_x),int(max_of_x)]
        y2=[0,max_pcc]
        plt.plot(x1,y1,marker='x',linestyle='--',color='black')
        plt.plot(x2,y2,marker='x',linestyle='--',color='black')
        plt.annotate("("+str(max_of_x)+","+str(max_pcc)+"),"+str(z_coordinate)+"="+str(max_of_z),xy=(int(max_of_x),max_pcc),xytext=(float((3/4)*int(x_limit)),float(float(y_limit)-0.005)),arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"))
        plt.xlim(int(x_lower),int(x_limit))
        plt.ylim(float(y_lower),float(y_limit))
        plt.xlabel(str(x_coordinate))
        plt.ylabel('pcc')
        plt.show()