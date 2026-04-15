<html>

<?php

// Display jsonfile
$jsonName = "test.json";
echo "<h1>$jsonName file contents</h1>";
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
    'blueFreq' => $_POST['blueFreq'],
    'blueStartDay' => $_POST['blueStartDay'],
    'blueStartTime' => $_POST['blueStartTime']
);
$json = json_encode($myObj);
echo "<p>$json</p><hr>";

echo "<h1>Debug Info</h1>";
// Write json to folder
$status = file_put_contents($jsonName, $json);
echo $status ? "<p>Successfully made $jsonName</p>" : "<p>ERROR: Could not make $jsonName</p>";

// Kill old main.py
$status = shell_exec("pkill -f py");
echo $status ? "ERROR: Could not kill main.py...\n" : "";

// Start new main.py located in /var/www/html...
$program = "main.py";
$log_file = "logs/mylog.txt";
$status = shell_exec("/var/www/html/MarbleMachine/venv/bin/python /var/www/html/MarbleMachine/$program >> /var/www/html/MarbleMachine/$log_file 2>&1 < /dev/null &");
echo $status ? "ERROR: Error in starting $program\n" : "";

echo "<hr><p>Started $program. Logging output to $log_file.</p>";
?>

</html>
