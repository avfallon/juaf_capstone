<?php
include( "constants.php" );
include( "getUserInfo.php" );
 $username = Constants::USERNAME;

 // connect to database using credentials
 $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

 // get the username and password from the app
 $usrname = $_POST['username'];
 $password = $_POST['password'];

 // run a sql query using the info the client provided to sign in the user
 $result = $mysqli->query("select * from login_info where username = '$username' AND password = '$password'");

if(empty($result)) {
	echo "login unsuccessful";
}
else {
	// Echos the user information associated with that id
	getUserInfo($result->fetch_assoc()['id'])
}

 ?>
