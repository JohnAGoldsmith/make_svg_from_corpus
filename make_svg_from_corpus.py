 
 
# John Goldsmith
# University of Chicago

import argparse
 

def commandline():

        parser = argparse.ArgumentParser(description='Compute morphological analysis.')
        parser.add_argument('-l', action="store", dest= "language", help = "name of language", default="english")
        parser.add_argument('-w', action="store", dest= "wordcount", help = "number of words to read", default = 10000)
        parser.add_argument('-f', action="store", dest= "filename", help = "name of file to read", default="browncorpus")
        parser.add_argument('-c', action="store", dest= "corrections", help = "number of corrections to make",default=0)
        parser.add_argument('-d', action="store", dest= "data_folder", help = "data directory",default="../../data/")

        results = parser.parse_args()
        language = results.language
        numberofwords	 = results.wordcount
        shortfilename = results.filename
        NumberOfCorrections = results.corrections

#---------------------------------------------------------------------------------------------------------##
#	readfile
#---------------------------------------------------------------------------------------------------------##
def readfile(infilename,Locations):
        index = 0
        with open (infilename, "rt"  ) as infile:
                for line in infile:
                    pieces = line.split()
                    if len(pieces) == 0:
                        continue
                    if pieces[0] == "#":
                        continue
                    for word in pieces:
                        if word not in Locations:
                            Locations[word] = list()
                        Locations[word].append(index)
                        index+= 1
        infile.close()




#---------------------------------------------------------------------------------------------------------##
#	Section 1 user modified variables: languages, directories, filenames, parameters
#---------------------------------------------------------------------------------------------------------##

 
def print_header(outfile):
        print("<html>\n<body>\n\n"  , file=outfile)

def print_footer(outfile):
        print("</body>\n</html>", file=outfile)
        outfile.close()
 
def print_svg(outfile, width , height ):
        print("<svg width=\"1000\" height=\"1000\">"   , file=outfile)
def print_circle(outfile, x,y,r):
        print ("<circle cx =\" " + str(x) + "\" cy=\""  + str(y) + "\" r=\"" + str(r) + "\" />", file=outfile)
def print_line(outfile, y):
        print ("<line  x1 =\"0\" " + "y1=\""  + str(y) + "\" " + "x2=\"1000\" y2=\""    + str(y) + "\"  style=\"stroke:rgb(255,0,0);stroke-width:2\" />", file=outfile)        

#_______________________________________________________

 
#________________________________________________________
 

def main():

        parser = argparse.ArgumentParser(description='Compute morphological analysis.')
        parser.add_argument('-l', action="store", dest= "language", help = "name of language", default="english")
        parser.add_argument('-w', action="store", dest= "wordcount", help = "number of words to read", default = 10000)
        parser.add_argument('-f', action="store", dest= "filename", help = "name of file to read", default="browncorpus.txt")
        parser.add_argument('-c', action="store", dest= "corrections", help = "number of corrections to make",default=0)
        parser.add_argument('-d', action="store", dest= "data_folder", help = "data directory",default="../../data/")

        results = parser.parse_args()
        language = results.language
        numberofwords	 = results.wordcount
        shortfilename = results.filename
        NumberOfCorrections = results.corrections
        Locations=dict()

        readfile(results.data_folder+shortfilename,Locations)

        pointgap=5
        screenwidth = 200 
        line_separator = 40
        corpuslength = 1000
        numberoflines = 20
        filename = "picture.html"
        outfile=open(filename, 'w' ) 
        print_header(outfile)
        print_svg(outfile, 100, 100)
        word = "the" 
        lineno = 0
        for i in Locations[word]:
            print(i)
            print_line(outfile,line_separator * (lineno+1))
            if i > (lineno+1)*screenwidth:
                lineno += 1
                if lineno > numberoflines:
                        break
                continue
            print_circle(outfile,(i-lineno*screenwidth)*pointgap,50+line_separator*lineno,3 )
        print_footer(outfile)

 
if __name__=="__main__": main()





