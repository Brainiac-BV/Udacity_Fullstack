import sys

def scrabble_cheat():
   words_parsed =[]
   file_path = r'C:\Users\keith gray\Downloads\sowpods\sowpods.txt'
   with open(file_path) as wlist:
      for line in wlist:
       line = line.strip()  
       words_parsed.append(line)
       print(words_parsed)


#scrabble_cheat()

def get_rack():
   try:
      rack = sys.argv[1]
      print(rack)
   except IndexError as e:
         print('No letters!', e)
         exit()
   

get_rack()       
