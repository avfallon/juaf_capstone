<?php
  // Assign JSON encoded string to a PHP variable
  include( "constants.php");
  $username = Constants::USERNAME;

  // connect to database using credentials
  $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

  $json = $_GET['json'];

  // Decode JSON data to PHP object
  $obj = json_decode($json);
  // Access values from the returned object


  // get each field from the json to create account
  $account_name = $obj->account_name;
  echo $account_name;
  $account_email = $obj->account_email;
  echo $account_email;
  $current_funds = $obj->current_funds;
  echo $current_funds;
  $recent_purchase = $obj->recent_purchase;
  echo $recent_purchase;
  $username = $obj->username;
  echo $username;
  $password = $obj->password;
  echo $password



  // sql query to the database to create the account_info row
  $query = "insert into user_info (account_name, account_email, current_funds, recent_purchase) values('$account_name', '$account_email', '$current_funds', '$recent_purchase')";

  // run the query
  $result = $mysqli->query($query);

  $id = $mysqli->query("select id from user_info where account_email = '$account_email';");
  echo $id;

// Use that id to add the username/password to the login_info table

  echo "Account Added Sucessfully";
?>

