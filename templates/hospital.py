import xlwt as xw
import xlrd as xr
import webbrowser
import time as t
while(True):
    a1=int(input("WANT WOULD YOU LIKE TO PERFORM\n1.MEDICINE ENQUIRY\n2.DOCTOR ADVICE\n3.for exit\n"))
    if(a1==1):
        print("                                 WELCOME TO ONLINE MEDICAL STORE\n")
        wbr=xr.open_workbook('symptons_2.0.xls')
        d0=wbr.sheet_by_index(0)
        row=[d0.row_values(0),d0.row_values(1),d0.row_values(2),d0.row_values(3),d0.row_values(4),d0.row_values(5)]
        flag=[-1,-1,-1,-1,-1,-1]
        ch=input("SELECT SYMPTONS FROM BELOW\n\nhead pain\t,sensation of tightness,tenderness,pain across eyes,stiff neck,sweating,chills,muscle aches,dehydration,pain,pressure,squeezing,shortness of breath,arm weakness,facial drooping,loss of vision,sudden weakness,severe headache,coughing of blood,pneumonia,wheezing,chronic cough,pain,tenderness,swelling,stiffness,redness,inflammation,tingling\n")
        ch=ch.split(',')
        print("PLEASE WAIT SYSTEM IS UNDER PROCESS",end="")
        for i in range(0,3):
            print(".",end="")
            t.sleep(1)
        for j in range(0,len(ch)):
            if(ch[j] in row[0]):
                flag[0]=flag[0]+1
                
            if(ch[j] in row[1]):
                flag[1]=flag[1]+1
                
            if(ch[j] in row[2]):
                flag[2]=flag[2]+1
                
            if(ch[j] in row[3]):
                flag[3]=flag[3]+1
                
            if(ch[j] in row[4]):
                flag[4]=flag[4]+1
                
            if(ch[j] in row[5]):
                flag[5]=flag[5]+1

        #max_val=max(flag)
        l=[]
        m=[]
        for i in range(0,len(flag)):
            if(flag[i]>-1):
                print("\n\nYOU MIGHT SUFFER FROM DISEASE:",row[i][2])
                print("MEDICINE FOR ",row[i][2]," is ",row[i][1],"\n")
                l.append(row[i][0])
                m.append(row[i][1])
        ch=int(input("WOULD YOU LIKE TO BUY THE MEDICINES\n1.YES\n2.NO\n"))
        if(ch==1):
            print('MEDICINE NAME\t\tPRICE(RS)')
            d3=[]
            d4=0
            for i in range(0,len(l)):
                print(m[i],'\t\t',l[i])
                d3.append(int(input("INPUT THE REQUIRED QUANTITY\n")))
                d4=d4+(d3[i]*l[i])
            print('                                YOUR BILL INVOICE')
            print('MEDICINE\t\tQUANTITY\t\tPRICE\t\tTOTAL\t\t')
            '''print('QUANTITY',end='  ')
            print('PRICE',end=' ')
            print('TOTAL')'''
            for i in range(0,len(l)):
                print(m[i],'\t\t',d3[i],'\t\t\t',l[i],'\t\t',d3[i]*l[i])
                '''print(d3[i],end='  ')
                print(l[i],end='  ')
                print(d3[i]*l[i])'''
            print('\n############TOTAL AMOUNT TO BE PAID IN Rs',d4,'############')
            add=input('\nENTER DELIVERY ADDRESS\n')
            print("DELIVERY TO THIS ADDRESS--",add,"WILL BE DONE BY TOMMORROW.")
            print('THANK YOU FOR YOUR EFFORTS\n')
        else:
            print('THANK YOU FOR VISITING\n')
                
            
            
            
        
        
    elif(a1==2):
        print("                                 WELCOME TO ADVICE WIZARD\n")
        d2=int(input("WHAT DO YOU WANT\n1.Fix appointment with a doctor\n2.Live chat with docotor"))
        if(d2==1):
            webbrowser.open("file:///D:/Projects/LMNIT/smartcity_project/web/index.html")
        elif(d2==2):
            print("chat")
            import mqttchat_py
        else:
            print("\nINVALID CHOICE\nPLEASE SELECT A VALID CHOICE")

    elif(a1==3):
        print("See you next time")
        break
    else:
        print("WRONG CHOICE\nPlease Select A Valid Choice\n")

    c=input("do you want to quit\npress 1 to quit\nElse press any key to continue\n")
    if(c=='1'):
        print("Thanks you visiting\nSee you next time")
        break
    
    
