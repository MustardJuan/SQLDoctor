import requests
import sys
import urllib

def main():

	html = urllib.urlopen("someURL").read().decode('utf-8')
	print(html)

if __name__ == "__main__":

    main()
