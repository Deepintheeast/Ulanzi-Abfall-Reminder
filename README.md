# Ulanzi-Abfall-Reminder
einfache Überwachung und Anzeige Abfalltermine auf "Ulanzi Pixel Clock mit Awtrix Light"

das Script wird bei mir einmal täglich per Cron aufgerufen

``01 17  *  *  *    /home/pi/scripts/Ulanzi-Abfall-Reminder/start.sh    >/dev/null``

und checkt ob für den "morgigen" Tag Abholtermine anstehen.

Ist das der Fall erhalte ich eine entsprechende "Notifikation" auf dem Ulanzi die erst wieder weg geht wenn
man diese durch Druck der mittleren Taste am Ulanzi bestätigt!



Die Entsorgungstermine im "CSV Format" bekomme ich von der Website meines Entsorgers.

Sie müssen für jede "Tonne" als seperate Datei, im selben Verzeichnis wie das Script, vorhanden sein <br> (gelb.csv , blau.csv , rest.csv , bio.csv) <br>und folgendes Format haben:


Blaue Tonne<br> 
02.01.2023<br> 
30.01.2023<br> 
27.02.2023<br> 
27.03.2023<br> 
24.04.2023<br> 
22.05.2023<br> 
19.06.2023<br> 
17.07.2023<br> 
14.08.2023<br> 
11.09.2023<br> 
09.10.2023<br> 
06.11.2023<br> 
04.12.2023<br> 


Der Eintrag in der ersten Zeile stört nicht und kann so bleiben!
