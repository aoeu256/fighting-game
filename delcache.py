

import os, sys
done = False
print 'Enter character name:'
charname = raw_input()
print 'Enter a image name:'
imgname = raw_input()

try:
    def remove(im):
        print 'Removing %s...' % im
        os.remove(im)
    fill = (os.getcwd(), charname)
    folder = '%s/Images/characters/%s' % fill
    flist = [(os.getcwd(), charname, i[:-4]) for i in os.listdir(folder) if imgname in i]
    for fill in flist:
        remove('%s/Images/cache/characters/%s/l%s.png' % fill)
        remove('%s/cache/outline/%s/self%s' % fill)
        remove('%s/Images/cache/characters/%s/lp1%s.png' % fill)
        remove('%s/Images/cache/characters/%s/p1%s.png' % fill)
except WindowsError:
    pass