import urllib.request
import re
import argparse
import sys
import os
from time import sleep

__version__ = "1.0"

banner = """
               \033[1m\033[91m             .d888888b.
                            d88888888b
                            8888  8888
                            8888  8888
                            8888  8888  .d888888b.
                            8888  8888  d88888888b
                            8888  8888  8888  8888
                            8888  8888  8888  8888
                            8888  8888  8888  8888
                            d88P  8888  8888  8888  
               888888888888888b.  8888  8888  "88888888888888
               8888888888888P"    8888  8888   Y8888888888888
                                  8888  8888    
                                  "888  888"
                                   Y888888Y

                      \033[93mMusical.ly Downloader (\033[91mMusicalSave\033[93m)
              \033[94mMade with <3 by: \033[93mSadCode Official (\033[91mSadCode\033[93m)
                                 \033[94mVersion: \033[93m{}
              \033[0m
"""


def download(url):

  print("\033[1;92m [+] Visiting -->\033[93m", url)
  response = urllib.request.urlopen(url)
  html = response.read().decode('utf-8')

  print("\033[1;92m [+] Extracting Video")
  file_url = re.search('http(.*)mp4', html)
  file_url = file_url[0]

  file_name = file_url.split("/")[-1]
  path = file_name

  print("\033[1;92m [+] Downloading -->\033[93m", path)
  urllib.request.urlretrieve(file_url, path)

  print("\033[1;33m [!] Successfully Downloaded To -->\033[93m",
    os.getcwd()+"/"+str(file_name),
    "\033[0m")


def main():
  parser = argparse.ArgumentParser(description = "Musical.ly Downloader")
   
  parser.add_argument("-u", "--url", 
    help = "URL to the Musical.ly video.")

  parser.add_argument("-v", "--version", 
    action='store_true',
    help = "Get the current version.")

  args = parser.parse_args()

  if args.version:
    print(__version__)

  elif args.url:
    print(banner.format(__version__))
    download(args.url)

  elif len(sys.argv) == 1:
    parser.print_help()

main()
