<?php
 include( "constants.php");
 $username = Constants::USERNAME;
 echo $username;
 echo "\n";
 // credentials to connect to sqli
 $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

 $result = $mysqli->query("select * from user_info");

 // make an array of json pet objects
 $array = [];
 while($row = $result->fetch_assoc())
 {
  // assign the values into the json object
   array_push($array, [
     'id' => $row['id'],
     'account_name' => $row['account_name'],
     'account_email' => $row['account_email'],
     'current_funds' => $row['current_funds'],
     'recent_purcahse' => $row['recent_purchase'],
   ]);
 }

 //encode the array into json
 $result = json_encode($array);

 //reurn the array of pets in the database
 echo $result;
 echo "\n";
 ?>
