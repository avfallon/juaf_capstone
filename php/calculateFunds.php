<?php
  // This script gets all purchases from an account that are more recent than user_info's most recent purchase id
  include( "constants.php");
  $username = Constants::USERNAME;

  // credentials to connect to sqli
  $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

  $email = $argv[1];

  // Check connection
  if ($mysqli -> connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
    exit();
  }

  $result = $mysqli->query("select current_funds, last_purchase_id from user_info 
                                        where account_email=$email");
  echo mysql_fetch_object($result);
  // make an array of json email and fund data
//  while($account = $result->free_result());
  //{
    //echo $account;
  //}


  
//  $purchases = $mysqli->query("select zehnfunds, purchase_id from purchase_table
//					where purchase_id > $account[last_purchase_id]");
//
//  $new_recent_purchase_id = $account['last_purchase_id'];
//  
//  $array = [];
//  while($row = $purchases->fetch_assoc())
//  {
//    // assign the values into the json object
//    array_push($array, [
//      'zehnfunds' => $row['zehnfunds'],
//      'purchase_id' => $row['purchase_id'],
//    ]);

//    echo $row['zehnfunds'];
//    echo "\n";
//    echo $row['last_purchase_id'];  
//    echo "\n";
//  }

 ?>
