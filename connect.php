<?php

echo 'php file'

$myObj = new marbleClass();
$myObj->redFreq = \$_POST['redFreq'];
$myObj->yellowFreq = \$_POST['yellowFreq'];
$myObj->greenFreq = \$_POST['greenFreq'];
$myObj->blueFreq = \$_POST['blueFreq'];

$myJSON = json_encode($myObj);
echo $myJSON;
file_put_contents('test.json', $myJSON);

?>

<html>
    <p>Hello World<p>
</html>