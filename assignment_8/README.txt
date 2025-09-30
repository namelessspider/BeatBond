step by step explanation of process

1. we downloaded  ssl access log and error log to out local device
2. we filtered out our website by running following commands in linux shell
        2.1. grep -E 'rvardiashv' ssl_access_log > filtered_log.txt
        2.2. grep -E 'rvardiashv' error_log > filtered_error_log.txt
3. for analyzing data and creating charts we used tool named goaccess(goaccess.io) and ran following commands
        3.1. goaccess filtered_log.txt -o report.html --log-format='[%d:%t %^] %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x "%r" %s %R "%u"' 
        3.2. goaccess filtered_error_log.txt -o error_report.html --log-format='[%^ %d %t.%^ %^] [%^] [%^] %^: [%^ %h:%^] %^: %U' --date-format='%b %d'
4. we looked at outputted data, sorted it and constructed it into pdf
