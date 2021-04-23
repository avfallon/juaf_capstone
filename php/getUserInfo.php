<?php
function getUserInfo($id, $mysqli){
   $result = $mysqli->query("select * from user_info where id=$id");
	 // make an array of json account objects
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
	 $json_result = json_encode($array);
	 echo $json_result
 }


 ?>
