$(go);

//Gets user Information from DB when dashboard is loaded

function go() {

    $.post("../php/lookupAccount.php", {email: getCookie('account_email')}, function(json)
    {
      var jsonObject = JSON.parse( json );
      if(jsonObject != undefined)
      {
          for (var key in jsonObject){
              if(jsonObject.hasOwnProperty(key)){
                  var account_name= jsonObject[key]["account_name"];
                  var current_funds = jsonObject[key]["current_funds"];
                  var account_email = jsonObject[key]["account_email"];
                  var recentPurchase = jsonObject[key]["last_purchase_id"]
              }
          }
                //Update user Information on the screen to be current account logged in
          if(document.title =="Profile Page")
          {
            console.log(account_email);
            document.getElementById("userName").innerHTML = account_name;
            document.getElementById("profileName").innerHTML = account_name;
            document.getElementById("userEmail").setAttribute("placeholder", "  " + account_email);
            document.getElementById("userFunds").setAttribute("placeholder", "  " + current_funds);
            document.getElementById("userPassword").setAttribute("placeholder", "  " + getCookie('password'));
            document.getElementById("recentPurchase").setAttribute("placeholder", " " + recentPurchase);   
          }
          else {  //For the Dashboard
            document.getElementById("userName").innerHTML = account_name;
            document.getElementById("zehnfundsTotal").innerHTML = current_funds;
            if(current_funds < 100)
            {
              document.getElementById('redeemButton').setAttribute("disabled" , true);
            }
          }
        }
    })
}
