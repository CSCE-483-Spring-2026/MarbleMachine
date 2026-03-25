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

$output = Shell_exec('python3 /var/www/html/MarbleMachine/main.py');

echo $output;

?>
