<?php
 include( "constants.php");
 $username = Constants::USERNAME;

 // credentials to connect to sqli
 $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

 $result = $mysqli->query("select account_email, current_funds from Pets");

 // make an array of json email and fund data
 $array = [];
 while($row = $result->fetch_assoc())
 {
  // assign the values into the json object
   array_push($array, [
     'account_email' => $row['account_email'],
     'current_funds' => $row['current_funds'],
   ]);
 }

 //encode the array into json
 $result = json_encode($array);

 //reurn the array of emails and fund information in the database
 echo $result;

 ?>
