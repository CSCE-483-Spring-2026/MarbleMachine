<?php

echo 'php file';

$myObj = array(
    'redFreq' => $_POST['redFreq'],
    'yellowFreq' => $_POST['yellowFreq'],
    'greenFreq' => $_POST['greenFreq'],
    'blueFreq' => $_POST['blueFreq']
);

$myJSON = json_encode($myObj);
echo $myJSON;
$tester = file_put_contents('test.json', $myJSON);
echo $tester ? 'true' : 'false';
$killer = shell_exec("pkill -f main.py");
$pyOutput = shell_exec("/var/www/html/MarbleMachine/venv/bin/python /var/www/html/MarbleMachine/main.py >> /var/www/html/MarbleMachine/logs/mylog.txt 2>&1 < /dev/null &");
echo "Started main.py...";
?>
