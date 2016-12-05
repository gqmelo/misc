from PyQt5.Qt import QApplication, QFont, QFontDatabase, QFontInfo
#from esss_qt10 import qt_traits
#from esss_qt10.qt_traits import QFont, QFontDatabase


qapp = QApplication([])
fd = QFontDatabase()
print fd

#pprint(list(fd.families()))
#
#f = fd.font('Sans Serif', 'Normal', 9)
#print f.exactMatch()
#print f.defaultFamily()
#print f.lastResortFamily()
#print f.lastResortFont()
#print f.family()
#print f.rawName()
#print f.toString()
#
#info = QFontInfo(f);
#print 'QFontInfo'
#print info.family()
#
#substitutes = QFont.substitutes('DejaVu Sans')
#pprint(list(substitutes))


available_fonts = [unicode(font_name) for font_name in fd.families()]
for family in available_fonts:
    exact_match = [i for i in range(100) if QFont(family, i).exactMatch()]
    print('family: {}, exactMatch: {}'.format(family, exact_match))
