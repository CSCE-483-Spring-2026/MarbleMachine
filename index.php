<!DOCTYPE html>

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

<html>
<head>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div>
        <h1>Welcome to the marble sorter!</h1>
        <p>Configure each marble to your liking, then click "Submit Changes" when you're done!</p>
    </div>
        <!-- <div class="configBody">
            <div class="configBox">
                <h2>Red Marble</h2>
                <div class="redMarble"></div>
                <div class="freqInput">
                    <label for="redFreq">Frequency:</label>
                    <input type="text" id="redFreq" name="redFreq">
                </div>
            </div>
            <div class="configBox">
                <h2>Yellow Marble</h2>
                <div class="yellowMarble"></div>
                <div class="freqInput">
                    <label for="yellowFreq">Frequency:</label>
                    <input type="text" id="yellowFreq" name="yellowFreq">
                </div>
            </div>
            <div class="configBox">
                <h2>Green Marble</h2>
                <div class="greenMarble"></div>
                <div class="freqInput">
                    <label for="greenFreq">Frequency:</label>
                    <input type="text" id="greenFreq" name="greenFreq">
                </div>
            </div>
            <div class="configBox">
                <h2>Blue Marble</h2>
                <div class="blueMarble"></div>
                <div class="freqInput">
                    <label for="blueFreq">Frequency:</label>
                    <input type="text" id="blueFreq" name="blueFreq">
                </div>
            </div>
        </div> -->
        
    <form action="connect.php" method="post">
        Red: <input type="text" id="redFreq" name="redFreq">
        Yellow: <input type="text" id="yellowFreq" name="yellowFreq">
        Green: <input type="text" id="greenFreq" name="greenFreq">
        Blue: <input type="text" id="blueFreq" name="blueFreq">
        <input type="submit">
    </form>
    <button type="button" id="submitButton">Submit Changes</button>
</body>
</html>