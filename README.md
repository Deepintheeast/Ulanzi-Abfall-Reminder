# Ulanzi-Abfall-Reminder
Überwachung und Anzeige Abfalltermine auf Ulanzi Clock

das Script wird bei mir einmal täglich per Cron aufgerufen

``01 17  *  *  *    /home/pi/scripts/Ulanzi-Abfall-Reminder/start.sh    >/dev/null``

und checkt ob für den "morgigen" Tag Abholtermine anstehen.

Ist das der Fall erhalte ich eine entsprechende "Notifikation" auf dem Ulanzi die erst wieder weg geht wenn
man diese durch Druck der mittleren Taste am Ulanzi bestätigt!