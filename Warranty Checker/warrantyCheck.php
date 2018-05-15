<?php
$server = "datarobot.compnow.com.au";
$username = "magi";
$password = "6ecbbe26fa99e15be123970799605a73";
$db = "service";

$conn = new mysqli($server, $username, $password, $db);

if ($conn->connect_error) {
	die("Unable to connect to database: " . $conn->connect_error);
}

$sql = "SELECT * FROM tblWarren WHERE Serial LIKE '%" . $_POST["serial"] . "'";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
	// output data of each row
	while ($row = $result->fetch_assoc()) {
		echo "Serial: " . $row["Serial"] . "<br>";
		echo "First: " . $row["First"] . "<br>Last: " . $row["Last"] . "<br>";
		echo "Product Name: : " . $row["ProductName"] . "<br>Expiry: " . $row["ExpiryDate"] . "<br>";
	}
} else {
	echo "0 results";
}

$conn->close();
?>