<?php
 // This is a basic script to find user info for a given email
 include( "constants.php");
 include( "getUserInfo");
 
 $username = Constants::USERNAME;
// echo $username;
// echo "\n";
 // credentials to connect to sqli
 $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

 $result = $mysqli->query("select * from user_info where account_email=$email");
 

 $array = [];
 while($row = $result->fetch_assoc())
 {
  // assign the values into the json object
   array_push($array, [
     'account_name' => $row['account_name'],
     'account_email' => $row['account_email'],
     'current_funds' => $row['current_funds'],
   ]);
 }

 //encode the array into json
 $result = json_encode($array);

 //reurn the array of accounts in the database
 echo $result;
 echo "\n";
 ?>

