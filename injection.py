import shutil
import os
#alfa = 'alfa'
#beta = 'save0-2022-06-18 10-40-34-0x000010-halfpatched'
class InjectionProcess():
	def writeBytes( romFile,saveFile,hexAddress):
		output = os.path.dirname(romFile) +"/output-"+os.path.basename(romFile)
		shutil.copyfile(romFile, output)
		offset = int(hexAddress, base=16)
		with open(output, 'r+b') as rom, open(saveFile, 'r+b') as save:
			rom.seek(offset)
			rom.write(save.read())

	def hexAddress( name):
		print("hexAddress.input: "+name)
		output = name[26:-16]
		print('hexAddress.output: '+output)
		if(len(output)!=8):
			return None
		if(output[0:-6] != '0x'):
			return None
		return 	output

#writeBytes(alfa,beta,hexAddress(beta))

