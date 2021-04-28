<?php
 include( "constants.php");
 //$username = Constants::USERNAME;

 // credentials to connect to sqli
 //$mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE);


function getUserInfo($email, $mysqli) {
  $result = $mysqli->query("select * from user_info where account_email=$email");
  $userInfo = json_encode($result);

  echo $result;
}

 ?>

