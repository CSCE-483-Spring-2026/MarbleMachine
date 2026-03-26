<?php

echo 'php file';

$myObj = array(
    'redFreq' => $_POST['redFreq'],
    'redStartDay' => $_POST['redStartDay'],
    'redStartTime' => $_POST['redStartTime'],
    'yellowFreq' => $_POST['yellowFreq'],
    'yellowStartDay' => $_POST['yellowStartDay'],
    'yellowStartTime' => $_POST['yellowStartTime'],
    'greenFreq' => $_POST['greenFreq'],
    'greenStartDay' => $_POST['greenStartDay'],
    'greenStartTime' => $_POST['greenStartTime'],
    'blueFreq' => $_POST['blueFreq']
    'blueStartDay' => $_POST['blueStartDay'],
    'blueStartTime' => $_POST['blueStartTime'],
);

$myJSON = json_encode($myObj);
echo $myJSON;
$tester = file_put_contents('test.json', $myJSON);
echo $tester ? 'true' : 'false';

// shell_exec('sudo nano test.json');

?>
