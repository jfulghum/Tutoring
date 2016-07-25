import urllib

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/chess/king-rook-vs-king-pawn/kr-vs-kp.data")

opener = urllib.FancyURLopener({})
f = opener.open(url)
#f.read()

if __name__ == '__main__':
	print f.read()

