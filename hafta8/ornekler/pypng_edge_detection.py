import png

def rate(pixels ,i, j): # Koordinatlari verilen pixel ile komsulari arasinda ne kadar renk farkliligi oldugunu bulur.
    tmp = 0

    for ni in range(i-1, i+2):
        if ni >= 0 and ni < numrows:
            for nj in range(j-1, j+2):
                if nj >=0 and nj < numcols:
                    for c in range(0, 3):
                        tmp += (pixels[i][j*numchannels+c] - pixels[ni][nj*numchannels+c])**2

    return tmp


filename = input('Enter file name:')
r = png.Reader(file=open(filename + '.png', 'rb'))

res = r.read()
numcols = res[0]
numrows = res[1]
rows    = res[2]
if (res[3]['alpha']): # Eger resmin alfa kanali varsa, i'nci pixel i*4'uncu sutundan baslar. Yoksa (sadece RGB kanallari varsa) i*3'uncu sutundan baslar.
    numchannels = 4
else:
    numchannels = 3

rows = list(rows)
newpixels = []

for i in range(numrows):
    newcurrow = []
    for j in range(numcols):
        x = rate(rows, i, j)
        if x < 15000:
            newcurrow.append(255) # Cikti resmimizde her pixel icin uc kanal var (RGB). Bu yuzden burda ciktiya ucer defa 255 veya 0 ekliyoruz.
            newcurrow.append(255)
            newcurrow.append(255)
        else:
            newcurrow.append(0)
            newcurrow.append(0)
            newcurrow.append(0)
    newpixels.append(newcurrow)

w = png.Writer(numcols, numrows)
w.write(open(filename + '_edges.png', 'wb'), newpixels)

