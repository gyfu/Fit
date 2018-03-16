#Höfundur: Huginn Þór Jóhannsson
#Liður 1: Sléttar tölur frá 1 - 1000
def slettTolurListi():	#Býr til lista af sléttum tölum frá einum upp í þúsund með einfaldri for loop-u og lista
	listi = []
	for x in range(2,1001,2):
		listi.append(x)
	return listi
def skrifaSkra(talnaListi, nafnskra):	#Skrifar lista í skrá með bili með því að nota einfalda for loop-u
	with open(nafnskra, "w") as f:
		for x in talnaListi:
			f.write(str(x) + " ")
def lesaSkra(nafntxt):	#Les skrá og setur í lista, skiptir hverju staki þegar kemur bil
	with open(nafntxt, "r") as f:
		listi = f.read().split(" ")
	listi.pop()
	return listi
def medaltal(listi):	#Finnur meðaltal, summa er fundin með for loop-u en lengd með len() falli
	summa = 0
	for x in listi:
		summa += int(x)
	lengd = len(listi)
	medaltal = summa / lengd
	return("%.2f" % medaltal)
def skraAtta(listi):	#Skilar lista með öllum tölum sem eru deilanlegar með 8, ef tala er deilanleg með átta fer hún inn í lista sem skilast
	new_list = []
	for x in listi:
		if int(x) % 8 == 0:
			new_list.append(x)
	return new_list
def skraMedBilum(listi):	#Printar út efni úr lista í "töflu" með bilum. Tíu stök í röð
	count = 0
	print("Eftirfarandi eru tíu tölur í línu úr skrá.")
	for x in listi:
		print("{}".format(x), end = "	")
		count += 1
		if count == 10:
			print("")
			count = 0
	print("")
def lidur1():		#Samantekt allra verkefna úr liði eitt
	skrifaSkra(slettTolurListi(), "slettar_tolur.txt")
	print("Hér eftir kemur listinn af sléttum tölum:\n{}".format(lesaSkra("slettar_tolur.txt")))
	print("Hér eftir kemur meðaltal listans:\n", medaltal(lesaSkra("slettar_tolur.txt")))
	skrifaSkra(skraAtta(lesaSkra("slettar_tolur.txt")), "sumarslettartolur.txt")
	skraMedBilum(lesaSkra("sumarslettartolur.txt"))
#lidur_1()
#Liður 2: Prím Tölur
def primTolur(n):	#Finnur allar prímtölur upp að n með því að nota "Sieve of Eratosthenes" aðferðina og situr í lista sem skilast.
	listi = [2,3,5,7]
	for x in range(8, n):
		if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
			listi.append(x)
	return listi
def erSjo(listi):	#Finnur út hvort það sé sjö í tölu með því að breita tölunni í streng, ef það er sjö er það fært í annan lista sem skilast
	sjoListi = []
	for x in listi:
		if "7" in str(x):
			sjoListi.append(x)
	return sjoListi
def fjordaHver(listi):	#Finnur fjórða hverja tölu með því að nota teljara og setur svo tölunna í lista sem skilast
	fjordaListi = []
	tel = 0
	for x in listi:
		tel += 1
		if tel == 4:
			fjordaListi.append(x)
			tel = 0
	return fjordaListi
def lidur2():		#Samantekt allra verkefna í lið tvö
	skrifaSkra(primTolur(100), "primtolur.txt")
	primListi = lesaSkra("primtolur.txt")
	print("Prime tölur eru eftirfarandi:\n{}".format(primListi))
	print("Prime tölur með sjö í sér eru eftirfarandi:\n{}".format(erSjo(primListi)))
	print("Fjórða hver tala í fyrri listanum:\n{}".format(fjordaHver(primListi)))
	skrifaSkra(fjordaHver(primListi), "fjorda.txt")	
#lidur2()
#Liður 3: Tuple
def lesaAlt(skra):	#Sama og lesaSkra() nema án þess að setja í lista, Alt er stutt fyrir Alternative
	with open(skra, "r") as f:
		file = f.read()
		return file
def writeTuple(efni, skra, mode):	#Skrifar tuple inn í skrá með svigum og kommum
	with open(skra, mode) as f:
		f.write("(")
		for x in efni:
			f.write(str(x))
			f.write(",")
		f.write(")")
		f.write("\n")
def notandaTuple():			#Býr til notanda skilgreint tuple og skilar því
	tempList = []
	while True:
		text = input("Hvaða texta viltu skrifa(skrifaður break! til að hætta):\n")
		if text == "break!":
			break
		else: 
			tempList.append(text)
	userTuple = tuple(tempList)
	return userTuple
def findSum(efni):		#Finnur summu einhvers lista/tuple
	summa = 0
	for x in efni:
		summa += x
	return summa
	
def lidur3():			#Samantekt á öllum verkefnum í lið 3
	fyrsta = (123,"ghgh",321,"hghg")
	annad = (1,2,3,4,5,6,7,8,9)
	thridja = ("a","b","c","d","e","f","g","h")
	writeTuple(fyrsta, "tuple.txt", "w")
	writeTuple(annad, "tuple.txt", "a")
	writeTuple(thridja, "tuple.txt", "a")
	print(lesaAlt("tuple.txt"))
	userTuple = notandaTuple()
	writeTuple(userTuple, "tuple.txt", "a")
	print("Summa annars tuplesins er {}".format(findSum(annad)))	
#lidur3()
#Liður 4: Dict
def makeDict(strengList, numList):	#Býr til dict úr tveimur listum, tekur listanna og tengir þá með for loop-u
	tempDict = {}
	for i in range(len(numList)):
		tempDict[numList[i]] = strengList[i]
	return tempDict
def writeDict(efni, skra, mode):	#Skrifar dict í skrá og setur \n newline	
	with open(skra, mode) as f:
		f.write(str(efni))
		f.write("\n")
def eittSett(skra):			#Les skrá og prentar út með commu separator(split(",")
	with open(skra, "r") as f:
		listi = f.read().split(",")
		for x in listi:
			print(x, "\n")
def lidur4():				#Samantekt á öllum verkefnum í lið 4
	tempDict = makeDict(["Konni","Snorri","Kalli","Palli"], [1,2,3,4])
	writeDict(tempDict, "dict.txt","w")
	print(lesaAlt("dict.txt"))
	dictTwo = makeDict(["Epli","Granít","Snorra saga","Lúðvík","Grænmeti", "Bílar",],[6,5,4,3,2,1])
	dictThree = makeDict(["Jón","Hulda","Hít","Gimli"],["Maður","Álfur","Tröll","Dvergur"])
	writeDict(dictTwo,"dict.txt","a")
	writeDict(dictThree,"dict.txt","a")
	eittSett("dict.txt")
#lidur4()

def main():		#Main fall sem keyrir allar samantektir eftir vild
	while True:
		val = input("Veldu af eftirfarandi: \n 1. Sléttar tölur frá 1 - 1000\n 2. Prím Tölur \n 3. Tuple\n 4. Dict\n 5. Hætta\n: ")
		if val == "1":
			lidur1()
		elif val == "2":
			lidur2()
		elif val == "3":
			lidur3()
		elif val == "4":
			lidur4()
		elif val == "5":
			break
main()



	

