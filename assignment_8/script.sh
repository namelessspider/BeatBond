grep -E 'rvardiashv' ssl_access_log > filtered_log.txt
grep -E 'rvardiashv' error_log > filtered_error_log.txt
goaccess filtered_log.txt -o report.html --log-format='[%d:%t %^] %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x "%r" %s %R "%u"' 
goaccess filtered_error_log.txt -o error_report.html --log-format='[%^ %d %t.%^ %^] [%^] [%^] %^: [%^ %h:%^] %^: %U' --date-format='%b %d'
