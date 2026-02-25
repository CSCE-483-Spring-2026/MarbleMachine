<?php

echo 'php file'

$myObj = new marbleClass();
$myObj->redFreq = \$_GET['redFreq'];
$myObj->yellowFreq = \$_GET['yellowFreq'];
$myObj->greenFreq = \$_GET['greenFreq'];
$myObj->blueFreq = \$_GET['blueFreq'];

$myJSON = json_encode($myObj);
echo $myJSON;
file_put_contents('test.json', $myJSON);

?>