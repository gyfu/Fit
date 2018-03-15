#Höfundur: Huginn Þór Jóhannsson
#Liður 1: Sléttar tölur frá 1 - 1000
def slettTolurListi():
	listi = []
	for x in range(2,1001,2):
		listi.append(x)
	return listi
def skrifaSkra(talnaListi, nafnskra):
	with open(nafnskra, "w") as f:
		for x in talnaListi:
			f.write(str(x) + " ")
def lesaSkra(nafntxt):
	with open(nafntxt, "r") as f:
		listi = f.read().split(" ")
	listi.pop()
	return listi
def medaltal(listi):
	summa = 0
	for x in listi:
		summa += int(x)
	lengd = len(listi)
	medaltal = summa / lengd
	return("%.2f" % medaltal)
def skraAtta(listi):
	new_list = []
	for x in listi:
		if int(x) % 8 == 0:
			new_list.append(x)
	return new_list
def skraMedBilum(listi):
	count = 0
	print("Eftirfarandi eru tíu tölur í línu úr skrá.")
	for x in listi:
		print("{}".format(x), end = "	")
		count += 1
		if count == 10:
			print("")
			count = 0
	print("")
	
	
def lidur_1():
	skrifaSkra(slettTolurListi(), "slettar_tolur.txt")
	print("Hér eftir kemur listinn af sléttum tölum:\n{}".format(lesaSkra("slettar_tolur.txt")))
	print("Hér eftir kemur meðaltal listans:\n", medaltal(lesaSkra("slettar_tolur.txt")))
	skrifaSkra(skraAtta(lesaSkra("slettar_tolur.txt")), "sumarslettartolur.txt")
	skraMedBilum(lesaSkra("sumarslettartolur.txt"))
#lidur_1()
#Liður 2: Prím Tölur
def primTolur(n):
	listi = [2,3,5,7]
	for x in range(8, n):
		if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
			listi.append(x)
	return listi
def lidur2():
	skrifaSkra(primTolur(100), "primtolur.txt")
	primListi = lesaSkra("primtolur.txt")
	print("Prime tölur eru eftirfarandi:\n{}".format(primListi))
	print("Prime tölur með sjö í sér eru eftirfarandi:\n{}".format(erSjo(primListi)))
	print("Fjórða hver tala í fyrri listanum:\n{}".format(fjordaHver(primListi)))
	skrifaSkra(fjordaHver(primListi), "fjorda.txt")
def erSjo(listi):
	sjoListi = []
	for x in listi:
		if "7" in str(x):
			sjoListi.append(x)
	return sjoListi
def fjordaHver(listi):
	fjordaListi = []
	tel = 0
	for x in listi:
		tel += 1
		if tel == 4:
			fjordaListi.append(x)
			tel = 0
	return fjordaListi
		
#lidur2()
#Liður 3: Tuple
def makeTuple():
	temp_list = []
	while True:
		texti = input("Skrifaðu texta (skrifaðu 'break' til að hætta):\n")
		if texti == "hætta":
			break
		else: 
			temp_list.append(texti)
	temp_tuple = tuple(temp_list)
	return temp_tuple
def baetaSkra(nafnskra, efni):
	with open(nafnskra, "a") as f:
		f.write(str(efni))
def lidur3():
	efni1 = makeTuple()
	efni2 = makeTuple()
	efni3 = makeTuple()
	baetaSkra("tuple.txt", efni1)
	baetaSkra("tuple.txt", efni2)
	baetaSkra("tuple.txt", efni3)
lidur3()





	
