<?php
  // This script gets all purchases from an account that are more recent than user_info's most recent purchase id
  include("../php/constants.php");
  $username = Constants::USERNAME;

  // credentials to connect to sqli
  $mysqli = new mysqli( Constants::HOST, $username, Constants::PASSWORD, Constants::DATABASE );

  $email = $_POST['email'];
  
  if ($mysqli -> connect_errno) {
    echo "Failed to connect to MySQL: ";
    exit();
  }
  

  $result = $mysqli->query("select current_funds, last_purchase_id from user_info where account_email= '$email' ");
  
  if(mysqli_num_rows($result)== 0 ) {
  	echo 0;
  }
  else
  {
                                  
    while($account = $result->fetch_assoc())
    {
      $last_db_id = $account['last_purchase_id'];
    }

    $purchases = $mysqli->query("select * from purchase_table where purchase_id >= '$last_db_id' AND account_email = '$email'");
    $array = [];
    while($row = $purchases->fetch_assoc())
    {
      array_push($array, [
        'purchase_date' => $row['purchase_date'],
        'purchase_cost' => $row['purchase_cost'],
        'items_purchased' => $row['items_purchased']
      ]);
    }
    $result = json_encode($array);
  
    echo $result;
  }
?>