#!/bin/bash
COUNTER=1

for filename in ../bulk/*.xml; do
	csplit -s ../bulk/$filename '/^<DTE version="1.0" >$/' '{*}'
	rm -f xx00
	rm -f p*
	rm -f m*

	for x in xx*; do 
	  sed -i '1d' $x
	  cat ../1linea.txt $x > p0$COUNTER.xml
	  grep -v "</SetDTE>" p0$COUNTER.xml > tmpfile && mv tmpfile p0$COUNTER.xml
	  (( COUNTER++ ))
	  #rm -f tmppdf
	  sleep 2
	done

	rm -f xx*
	rm -f tmpfile
	cd .. && python3.9 script_convierte_xml.py
	cd input
	sleep 3
done

for filename in ../malos/*.xml; do
	sed -i '1d' $filename
	csplit -s ../malos/$filename '/^<DTE version="1.0".*$/' '{*}'
	rm -f p*
	rm -f m*

	for x in xx*; do 
	  sed -i '1d' $x
	  cat ../1linea.txt $x > m0$COUNTER.xmx
	  grep -v "</SetDTE>" m0$COUNTER.xmx > tmpfile && mv tmpfile m0$COUNTER.xmx
	  (( COUNTER++ ))
	  #rm -f tmppdf
	  sleep 2
	done

	rm -f xx*
	rm -f tmpfile
	cd .. && python3.9 script_convierte_xml.py
	cd input
	sleep 3
done