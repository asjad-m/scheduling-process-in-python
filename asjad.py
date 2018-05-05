import time
def display():
	print"			WELCOME TO PROCESS SCHEDULING SYSTEM "
	print" "
	print"		SELECT ANY PROCESS (1-6)"
	print"		1.FIRST COME FIRST SERVE(FCFS)"
	print"		2.SHORTEST JOB FIRST(SJF)"
	print"		3.ROUND ROBIN(RR)"
	print"		4.VIRTUAL ROUND ROBIN(VRR)"
	print"		5.MULTILEVEL QUEUE(MQ)"
	print"		6.MULTILEVEL FEEDBACK QUEUE(MFQ)"
	print" "
	a=input("ENTER YOU CHOICE(1-6):") 
	if a==1:
		fcfs()
	if a==2:
		sjf()
	if a==3:
		rr()
													
def fcfs():
	print" "
	print"				**WELCOME TO FIRST COME FIRST SERVE PROCESS**"
	print"		IN THIS PROCESS, PROCESSES WILL RUN ACCORDING TO THEIR ARRIVAL TIMES ,THOSE WITH SHORTEST ARRIVAL TIMES"
	print"			     WILL BE RUN FIRST AND PROCESS WILL CONTINUE TILL LAST PROCESS"
	print" "

	cont=0
	size=int(raw_input("ENTER HOW MANY PROCESSCES DO YOU WANT TO EXECUTE: "))
	prolist=[0]*size

	print"  "

	for i in range (size):
		prolist[i]=int(raw_input("NOW ENTER ARRIVAL TIME OF EACH  PROCESS:  "))
		cont=cont+1

	burst=[0]*size
	print" "

	for j in range(size):
		burst[j]=int(raw_input("NOW ENTER THE BURST TIME OF EACH PROCESS : "))

	print" "
	print"		PROCESSCES		 ARRIVAL TIME		 BURST TIME"

	for k in range(size):
		print" "
		print"		PROCESS ",k+1,"			",prolist[k]," 			",burst[k]
		print" "

	c= min(prolist)
	d=prolist.index(c)

	avgtime=0
	pretot=c
	waittime=0

	for k in range(cont):

		a= min(prolist)
		b=prolist.index(a)
		print" "
		print"ON FIRST COME FIRST SERVE BASIS PROCESS ", b+1," WILL EXECUTE FOR  ", burst[b]," SECONDS!"
		print"WAIT UNTILL YOU RECEIVE A COMPLETION MESSAGE! "

		time.sleep(burst[b])


		if a > pretot:
			print" "
			print"PROCESS ", b+1 ," STARTED AT ",min(prolist)," AND COMPLETED AT ",(a+burst[b])
			waittime=0
			avgtime=0
		else:
			print" "
                        print"PROCESS ", b+1 ," STARTED AT ",pretot," AND COMPLETED AT ",(pretot+burst[b])
			waittime=pretot-a
			avgtime=avgtime+waittime
		pretot=0
		pretot=a+burst[b]
		print" "
		print"WAITING TIME OF PROCESS ",b+1," IS : ",waittime
		prolist.remove(min(prolist))
		prolist.insert(b,10000)

	print" "
	print"TOTAL TIME TAKEN TO COMPLETE ALL PROCESSCES IS: ",sum(burst)," SECONDS"
	print" "
	print"AVERAGE WAITING TIME IS : ",avgtime/size
	print" "

															
def sjf():
	print" "
	print"         			 **WELCOME TO SHORTEST JOB FIRST  PROCESS**"
        print"		IN THIS PROCESS,FIRST OF ALL PROCESS WITH MINIMUM ARRIVAL TIME WILL RUN THEN PROCESSES WILL RUN ACCORDING TO THEIR BURST TIMES ,THOSE WITH SHORTEST BURST TIMES"
        print" 		             WILL BE RUN FIRST AND PROCESS SCHEDULING WILL CONTINUE TILL LAST PROCESS"
        print" "

        cont=0
        size=int(raw_input("ENTER HOW MANY PROCESSCES DO YOU WANT TO EXECUTE: "))
        prolist=[0]*size

        print"  "

        for i in range (size):
                prolist[i]=int(raw_input("NOW ENTER ARRIVAL TIME OF EACH  PROCESS:  "))
                cont=cont+1

        burst=[0]*size
        print" "

        for j in range(size):
                burst[j]=int(raw_input("NOW ENTER THE BURST TIME OF EACH PROCESS : "))

        print" "
        print"          PROCESSCES               ARRIVAL TIME            BURST TIME"

        for k in range(size):
                print" "
                print"          PROCESS ",k+1,"                 ",prolist[k],"                  ",burst[k]
                print" "


	d=min(prolist)
	c=prolist.index(d)
	avgtime=0

        sumbt=d
        waittime=0

	sum=0
	print"PEHLA"
	print" "
       	print"ON SHORTEST JOB  FIRST BASIS PROCESS ", c+1," WILL EXECUTE FIRST FOR  ", burst[c]," SECONDS!"
        print"WAIT UNTILL YOU RECEIVE A COMPLETION MESSAGE! "

        time.sleep(burst[c])
        print" "
        print"PROCESS ", c+1 ," STARTED AT ",d," AND COMPLETED AT ",burst[c]+d
	sumat=d+burst[c]
        waittime=0

	burst.remove(burst[c])
	prolist.remove(prolist[c])
	l=0
	aat=sumat

	for k in range(size):
	    a= min(burst)
            b=burst.index(a)
	    l=l+1
            x=min(prolist)
            y=prolist.index(x)
	 
      	    if   prolist[b] < sumat :
		print"if call 1"
		sumbt=sumat+burst[b]
		print" "
              	print"ON SHORTEST JOB  FIRST BASIS PROCESS  WILL EXECUTE FOR  ", burst[b]," SECONDS!"
               	print"WAIT UNTILL YOU RECEIVE A COMPLETION MESSAGE! "

	        time.sleep(burst[b])
		print" "
		print"PROCESS STARTED AT ",sumat," AND COMPLETED AT ",sumbt

		waittime=sumat-prolist[b]
		sumat=sumat+burst[b]
		burst.remove(burst[b])
        	prolist.remove(prolist[b])

	    elif prolist[b]>=aat :
		print"if call 2"
		print" "
             	print"ON SHORTEST JOB  FIRST BASIS PROCESS  WILL EXECUTE FOR  ", burst[b]," SECONDS!"
              	print"WAIT UNTILL YOU RECEIVE A COMPLETION MESSAGE! "

     		time.sleep(burst[b])
         	print" "
                print"PROCESS  STARTED AT ",prolist[b]," AND COMPLETED AT ",burst[b]+prolist[b]
		
		waittime=0
	        avgtime+=waittime
                print" "
                print"WAITING TIME OF PROCESS  IS : ",waittime

		sum=sum+min(burst)
                burst.remove(burst[b])
                prolist.remove(prolist[c])
                

        print" "
        print"TOTAL TIME TAKEN TO COMPLETE ALL PROCESSCES IS: ",sum," SECONDS"
	print" "
	print"AVERAGE WAITING TIME : ",avgtime/size
												

def rr():

	print" "
        print"         					 **WELCOME TO ROUND ROBIN  PROCESS**"
        print"		IN THIS PROCESS, PROCESSES WILL RUN FIRST ACCORDING TO THEIR ARRIVAL TIMES AND EXECUTE ONLY ACCORDING TO QUANTUM TIME"
	print"		,THOSE WITH SHORTEST ARRIVAL TIMES WILL BE RUN FIRST AND WILL BE EXECUTED FOR QUANTUM TIME AND THEN NEXT PROCESS WILL"
	print"		COME And PROCESS WILL GO TO WAITING QUEUE FOR I/O ACCORDING TO DEMAND AND THIS PROCESS WILL  CONTINUES TILL LAST PROCESS"
        print" "

        cont=0
        size=int(raw_input("ENTER HOW MANY PROCESSCES DO YOU WANT TO EXECUTE: "))
        prolist=[0]*size

        print"  "

        for i in range (size):
                prolist[i]=int(raw_input("NOW ENTER ARRIVAL TIME OF EACH  PROCESS:  "))
                cont=cont+1

        burst=[0]*size
        print" "

        for j in range(size):
                burst[j]=int(raw_input("NOW ENTER THE BURST TIME OF EACH PROCESS : "))
	print" "
	qt=input("NOW ENTER QUANTIME TIME TO LOCATE THE EXECUTION TIME OF EACH PROCESS: ")

	print" "
	eveodd=input("NOW CHOOSE EITHER EVEN OR ODD PROCESSES WILL GO FOR I/O?(0 FOR EVEN/1 FOR ODD): ")

	print" "
	io=input("ENTER I/O WAITING TIME : ")

        print" "
        print"          PROCESSCES               ARRIVAL TIME            BURST TIME		QUANTUM TIME		I/O TIME"

        for k in range(size):
                print" "
                print"          PROCESS ",k+1,"                 ",prolist[k],"                  ",burst[k],"			",qt,"			",io
                print" "


	c= min(prolist)
        d=prolist.index(c)

        avgtime=0
        pretot=c
        waittime=0
	rt=[0]*size
        for k in range(cont):

                a= min(prolist)
                b=prolist.index(a)
                print" "
                print"IN ROUND ROBIN PROCESS ", b+1," WILL EXECUTE FOR  ",qt," SECONDS!"
                print"WAIT UNTILL YOU RECEIVE A COMPLETION MESSAGE! "

                time.sleep(qt)


                if a > pretot:
                        print" "
                        print"PROCESS ", b+1 ," STARTED AT ",min(prolist)," AND STOPPED	 AT ",(a+qt)
                        waittime=0
                        avgtime=0
			rt[b]=burst[b]-qt
			print" "
			print"REMAINING EXECUTION TIME OF ", b+1," IS : ",rt[b]
                else:
                        print" "
                        print"PROCESS ", b+1 ," STARTED AT ",pretot," AND STOPPED AT ",(pretot+qt)
                        waittime=pretot-a
                        avgtime=avgtime+waittime
			rt[b]=burst[b]-qt
                        print" "
                        print"REMAINING EXECUTION TIME OF ", b+1," IS : ",rt[b]

                pretot=0
                pretot=a+qt
                print" "
		prolist.remove(min(prolist))
                prolist.insert(b,10000)
	A=input("PRESS 1 TO SEE READY QUEUE : ")
	print " "
	print"		|	PROCESSCES	|	REMAINING EXECUTION TIME		|"
	print"_______________________________________________________________________________"
	m=0
	for kk in range(cont):
		rt[kk]=rt[m]
		m+=1
	m=0
	for l in range (cont):
		print "		|  	PROCESS ",l+1,"	|		",rt[l],"		|"
		m+=1
		print"________________________________________________________________________________________"
display()

