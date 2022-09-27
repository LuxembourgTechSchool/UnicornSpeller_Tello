import os

# Auxiliary program that decodes packages received from Unicorn Speller
# and forwards it to port 127.0.0.1:2000.
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Release/TelloUnicornHybridBlackSpeller')
os.startfile(filename)

