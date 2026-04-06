<html>

<?php
$cmd = '/var/www/html/MarbleMachine/venv/bin/python /var/www/html/MarbleMachine/phpTests/timeTest.py >> /var/www/html/MarbleMachine/logs/mylog.txt 2>&1 < /dev/null &';
shell_exec($cmd);
echo "Started";
?>

















</html>
