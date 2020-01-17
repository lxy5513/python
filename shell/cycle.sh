for i in {1..5}
	do 
		echo $i 
		python test1.py & 
		python test2.py
	done 

