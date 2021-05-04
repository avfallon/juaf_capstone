<?php
 // This is a script that receives a username and password, checks if they match in the database,
 // and returns the associated account information if they are matched correctly
 // test comment
 include( "../php/constants.php" );
 include("../js/core/cookie.js"); 
//include( "getUserInfo.php" );
 $username = Constants::USERNAME;

 // connect to database using credentials
 $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

 // get the username and password from the app
 $usrname = $_POST['email'];
 $password = $_POST['password'];
  //echo $usrname;
  //echo $password;
 // run a sql query using the info the client provided to sign in the user
 $result = $mysqli->query("Select * from login_info where account_email = '$usrname' AND password = '$password'");
 //echo $result;
if( mysqli_num_rows($result)== 0 ) {
	echo 0;
}
else {
	// Echos the user information associated with that id
	setcookie('account_email', $usrname, time() + (86400 * 30), "/");
	setcookie('password', $password, time() + (86400 * 30), "/");
	//setcookie('account_email', $typeAccount, time() + (86400 * 30), "/");
	//setcookie('', $typeAccount, time() + (86400 * 30), "/");

	echo 1;

	
	// getUserInfo($result->fetch_assoc()['id'])
}

 ?>
