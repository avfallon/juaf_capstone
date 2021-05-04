<?php
  // This script assigns a JSON encoded string of a new account and adds it to the database
  include( "constants.php");
  $username = Constants::USERNAME;

  // connect to database using credentials
  $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);

  // get each field from the json to create account
  $account_name = $argv[1];
  echo "$account_name\n";
  $account_email = $argv[2];
  echo "$account_email\n";
  $username = $argv[3];
  echo "$username\n";
  $password = $argv[4];
  echo "$password\n";



  // sql query to the database to create the account_info row
  $user_info_query = "insert into user_info (account_name, account_email) values('$account_name', '$account_email')";
  $login_info_query = "insert into login_info (account_email, password) values('$account_email', '$password')";

  // run the query
  if($mysqli->query($user_info_query)) {

    // Add the username/password to the login_info table if successful
    $mysqli->query($login_info_query);
  }
  else {
    echo "Failed to add account";
  }


?>
