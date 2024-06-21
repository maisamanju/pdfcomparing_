
def compare(f1path,f2path):
	f1 = open(f1path, "r") 
	f2 = open(f2path, "r") 

	f1_data = f1.readlines()
	f2_data = f2.readlines()

	#print(f1_data)
	result = open('differance.txt','w')
	for i in range(0, len(f1_data),1):
		text1=f1_data[i]
		if text1 not in f2_data:
			#print(text1 +"doesnot exist")
			
			result.writelines(text1)
			
			print(text1)
	result.close()
	
	
        
    
	

