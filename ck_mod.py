# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 08:36:50 2019

@author: peng_
"""
# v1
import os
src_path = "C:\\Users\\peng_\\Documents\\Paradox Interactive\\Crusader Kings II\\mod\\5_test\\common\\landed_titles\\"
dst_path = "C:\\Users\\peng_\\Documents\\Paradox Interactive\\Crusader Kings II\\mod\\5_test\\history\\\titles\\"

f = []

for (dirpath, dirnames, filenames) in os.walk(mypath):
    f.extend(filenames)

for f1 in f:
    f2 = open(dirpath+f1, 'r', errors='ignore')
    if 'discovered_by = chinese2' in f2.read():
        print("o", end='')
        f2.close()
    else:
        f2.close()
        f3 = open(dirpath+f1, 'a')
        f3.write('\ndiscovered_by = chinese2\n')
        print("x", end='')
        f3.close()


## v2
#import os
#mypath = "C:\\Users\\peng_\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\eu4_chinese_sup\\history\\provinces\\"
#for dname, dirs, files in os.walk(mypath):
#    for fname in files:
#        fpath = os.path.join(dname, fname)
#        with open(fpath, errors='ignore') as f:
#            s = f.read()
##        #1. all Han chinese to chihan
##        s = s.replace('\nculture = jin\n', '\nculture = chihan\n')  #
##        s = s.replace('\nculture = wu\n', '\nculture = chihan\n')  #
##        s = s.replace('\nculture = chimin\n', '\nculture = chihan\n')  
##        s = s.replace('\nculture = hakka\n', '\nculture = chihan\n')  #
##        s = s.replace('\nculture = gan\n', '\nculture = chihan\n')  
##        s = s.replace('\nculture = xiang\n', '\nculture = chihan\n')  
##        s = s.replace('\nculture = sichuanese\n', '\nculture = chihan\n')  
##        s = s.replace('\nculture = jianghuai\n', '\nculture = chihan\n')  
##        s = s.replace('\nculture = xibei\n', '\nculture = chihan\n')  #
##        s = s.replace('\nculture = hubei\n', '\nculture = chihan\n')  
##        s = s.replace('\nculture = zhongyuan\n', '\nculture = chihan\n')  
##        s = s.replace('\nculture = shandong_culture\n', '\nculture = chihan\n')  #
##        
##        #2. all Korean and Japanese to wu
##        s = s.replace('\nculture = korean\n', '\nculture = wu\n')  
##        s = s.replace('\nculture = togoku\n', '\nculture = wu\n')  
##        s = s.replace('\nculture = japanese\n', '\nculture = wu\n')  
##        s = s.replace('\nculture = kyushuan\n', '\nculture = wu\n')  
##         
##        #3. all Southern mountaineers to miao
##        s = s.replace('\nculture = tibetan\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = yi\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = bai\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = central_thai\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = lao\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = northern_thai\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = shan\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = zhuang\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = khmer\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = vietnamese\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = burmese\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = mon\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = chin\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = karen\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = kachin\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = arakanese\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = assamese\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = kochi\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = bihari\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = pahari\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = nepali\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = oriya\n', '\nculture = miao\n')  
##        s = s.replace('\nculture = sinhala\n', '\nculture = miao\n')  
##         
##        #4. all Southern marines to cantonese
##        s = s.replace('\nculture = polynesian\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = cham\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = malayan\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = sumatran\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = javanese\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = filipino\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = bornean\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = madagascan\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = sulawesi\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = papuan\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = aboriginal\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = melanesian\n', '\nculture = cantonese\n')  
##        s = s.replace('\nculture = moluccan\n', '\nculture = cantonese\n')  
##       
##         #5. all nordic to xibei
##        s = s.replace('\nculture = uralic\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = samoyed\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = ostyaki\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = ingrian\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = hungarian\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = turkish\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = azerbaijani\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = mongol\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = chahar\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = khalkha\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = oirats\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = uzbehk\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = turkmeni\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = uyghur\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = khazak\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = kirgiz\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = astrakhani\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = bashkir\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = crimean\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = kazani\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = mishary\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = nogaybak\n', '\nculture = xibei\n')  
##        s = s.replace('\nculture = siberian\n', '\nculture = xibei\n')  
##       
##         #6. all southern/central_american to hakka
##        s = s.replace('\nculture = tecos\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = aztek\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = purepecha\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = totonac\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = chichimecan\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = yucatec\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = putun\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = mayan\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = highland_mayan\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = zapotek\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = mixtec\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = tlapanec\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = inca\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = aimara\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = diaguita\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = chimuan\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = jivaro\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = chachapoyan\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = muisca\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = cara\n', '\nculture = hakka\n')  
##        s = s.replace('\nculture = miskito\n', '\nculture = hakka\n')  
##       
##         #7. all northern_american to jin
##        s = s.replace('\nculture = tupinamba\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = guarani\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = charruan\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = ge\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = chacoan\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = mapuche\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = patagonian\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = het\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = huarpe\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = arawak\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = maipurean\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = carib\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = guajiro\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = aleutian\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = inuit\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = shawnee\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = illini\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = anishinabe\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = cree\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = mesquakie\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = cheyenne\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = blackfoot\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = arapaho\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = delaware\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = abenaki\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = mikmaq\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = mahican\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = powhatan\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = pequot\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = iroquois\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = cherokee\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = huron\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = susquehannock\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = dakota\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = nakota\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = chiwere\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = osage\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = catawba\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = wichita\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = caddo\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = pawnee\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = creek\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = choctaw\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = chickasaw\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = pueblo\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = piman\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = shoshone\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = kiowa\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = apache\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = navajo\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = chipewyan\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = haida\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = athabascan\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = salish\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = chinook\n', '\nculture = jin\n')  
##        s = s.replace('\nculture = yokuts\n', '\nculture = jin\n')  
##       
##         #8. all tungus to shandong_culture
##        s = s.replace('\nculture = yakut\n', '\nculture = shandong_culture\n')  
##        s = s.replace('\nculture = yukagyr\n', '\nculture = shandong_culture\n')  
##        s = s.replace('\nculture = buryat\n', '\nculture = shandong_culture\n')  
##        s = s.replace('\nculture = tungus\n', '\nculture = shandong_culture\n')  
##        s = s.replace('\nculture = manchu\n', '\nculture = shandong_culture\n')  
##        s = s.replace('\nculture = ainu\n', '\nculture = shandong_culture\n')  
##        s = s.replace('\nculture = kamchatkan\n', '\nculture = shandong_culture\n')  
##      
##        
#        #9. all Germans to Hessian
#        s = s.replace('\nculture = pommeranian\n', '\nculture = hessian\n')  #
#        s = s.replace('\nculture = prussian\n', '\nculture = hessian\n')  #
#        s = s.replace('\nculture = hannoverian\n', '\nculture = hessian\n')  #
#        s = s.replace('\nculture = saxon\n', '\nculture = hessian\n')  
#        s = s.replace('\nculture = franconian\n', '\nculture = hessian\n')  
#        s = s.replace('\nculture = swiss\n', '\nculture = hessian\n')  #
#        s = s.replace('\nculture = swabian\n', '\nculture = hessian\n')  
#        s = s.replace('\nculture = bavarian\n', '\nculture = hessian\n')  
#        s = s.replace('\nculture = austrian\n', '\nculture = hessian\n')  #
#        s = s.replace('\nculture = dutch\n', '\nculture = hessian\n')  
#        s = s.replace('\nculture = flemish\n', '\nculture = hessian\n')  #
#        
#        #10. all scandinavian to pommeranian
#        s = s.replace('\nculture = swedish\n', '\nculture = pommeranian\n')  
#        s = s.replace('\nculture = danish\n', '\nculture = pommeranian\n')  
#        s = s.replace('\nculture = norwegian\n', '\nculture = pommeranian\n')  
#        s = s.replace('\nculture = finnish\n', '\nculture = pommeranian\n')  
#        s = s.replace('\nculture = sapmi\n', '\nculture = pommeranian\n')  
#        
#        #11. all british to hannoverian
#        s = s.replace('\nculture = english\n', '\nculture = hannoverian\n')  
#        s = s.replace('\nculture = american\n', '\nculture = hannoverian\n')  
#        s = s.replace('\nculture = welsh\n', '\nculture = hannoverian\n')  
#        s = s.replace('\nculture = scottish\n', '\nculture = hannoverian\n')  
#        s = s.replace('\nculture = irish\n', '\nculture = hannoverian\n')  
#        s = s.replace('\nculture = highland_scottish\n', '\nculture = hannoverian\n')  
#        
#        #12. all french to flemish
#        s = s.replace('\nculture = gascon\n', '\nculture = flemish\n')  
#        s = s.replace('\nculture = cosmopolitan_french\n', '\nculture = flemish\n')  
#        s = s.replace('\nculture = normand\n', '\nculture = flemish\n')  
#        s = s.replace('\nculture = aquitaine\n', '\nculture = flemish\n')  
#        s = s.replace('\nculture = burgundian\n', '\nculture = flemish\n')  
#        s = s.replace('\nculture = occitain\n', '\nculture = flemish\n')  
#        s = s.replace('\nculture = wallonian\n', '\nculture = flemish\n')  
#        s = s.replace('\nculture = breton\n', '\nculture = flemish\n')  
#        
#        #13. all iberian to austrian
#        s = s.replace('\nculture = leonese\n', '\nculture = austrian\n')  
#        s = s.replace('\nculture = castillian\n', '\nculture = austrian\n')  
#        s = s.replace('\nculture = aragonese\n', '\nculture = austrian\n')  
#        s = s.replace('\nculture = catalan\n', '\nculture = austrian\n')  
#        s = s.replace('\nculture = galician\n', '\nculture = austrian\n')  
#        s = s.replace('\nculture = andalucian\n', '\nculture = austrian\n')  
#        s = s.replace('\nculture = portugese\n', '\nculture = austrian\n')  
#        s = s.replace('\nculture = basque\n', '\nculture = austrian\n')  
#        
#        #14. all latin to swiss
#        s = s.replace('\nculture = lombard\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = tuscan\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = sardinian\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = romagnan\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = ligurian\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = venetian\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = neapolitan\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = piedmontese\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = umbrian\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = sicilian\n', '\nculture = swiss\n')  
#        s = s.replace('\nculture = maltese\n', '\nculture = swiss\n')  
#        
#        #15. all west_slavic to swiss
#        s = s.replace('\nculture = czech\n', '\nculture = prussian\n')  
#        s = s.replace('\nculture = polish\n', '\nculture = prussian\n')  
#        s = s.replace('\nculture = schlesian\n', '\nculture = prussian\n')  
#        s = s.replace('\nculture = estonian\n', '\nculture = prussian\n')  
#        s = s.replace('\nculture = lithuanian\n', '\nculture = prussian\n')  
#        s = s.replace('\nculture = latvian\n', '\nculture = prussian\n')  
#        
#        with open(fpath, "w") as f:
#            f.write(s)
#        # add the observers
#        with open(fpath, "a") as f:
#            f.write('\ndiscovered_by = chinese2\n')

##v3
#import numpy as np
#a = np.array([690, 691, 702, 723, 2138, 2139, 2140, 2114, 2115, 2747, 703, 1816, 2136, 4194, 695, 696, 2137, 4195, 704, 726, 2111, 2112, 2113, 693, 694, 697, 2177, 2178, 4233])
#b = np.array([687, 1836, 2181, 2180, 698, 699, 688, 692, 2183, 2175, 2176, 681, 682, 2171, 2172, 4197, 689, 700, 2179, 4198, 701, 709, 2191, 4223, 2182, 2184, 707, 708])
#c = np.array([669, 670, 683, 684, 685, 686, 1821, 1822, 1824, 1829, 1833, 1838, 1897, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2141, 2142, 4196])
#d = np.array([2161, 1371, 610, 613, 616, 664, 665, 666, 667, 668, 672, 738, 1016, 1840, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2162, 2163, 2164, 2173, 2174, 2372, 671, 2373, 662, 663, 673, 674, 4199])
#e = np.array([679, 2132, 2167, 678, 2135, 2131, 2133, 660, 661, 2165, 2166, 680, 679, 680, 4212, 2169, 2170, 4211, 675, 2168, 2748, 4213])
#
#f = np.concatenate((a, b, c, d, e))
#f.sort()