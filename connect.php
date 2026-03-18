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
file_put_contents('test.json', $myJSON);

?>
