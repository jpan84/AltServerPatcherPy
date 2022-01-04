infile = open('AltServer.exe', 'rb')
EXEBytes = infile.read()

defurl = b'https://cdn.altstore.io/file/altstore/altstore.ipa'
newurl = b'http://127.0.0.1:7800/ER_YLb4aaaaaaaaaaaaaaaaa.ipa'
spaceddefurl = b''.join([bytes(bytearray([c, 0])) for c in defurl])
spacednewurl = b''.join([bytes(bytearray([c, 0])) for c in newurl])

newEXEBytes = EXEBytes.replace(spaceddefurl, spacednewurl)
outfile = open('AltServerCustom.exe', 'wb')
outfile.write(newEXEBytes)
outfile.close()
