$( go );

function go( )
{
  let url = "../php/calculateFunds.php";
  var table = document.getElementById("dataTable");
  var email = getCookie('account_email');
  //Getting purchase history for user
  $.post(url, { email: email }, function(response) {
    var jsonObject = JSON.parse( response );

    if(jsonObject == undefined)
    {
      console.log("Error");
    }

    var purchasesHTML = "";
    var recent_total = 0;

    for (var key in jsonObject){
      if(jsonObject.hasOwnProperty(key)){
        funds_earned = jsonObject[key]["purchase_cost"] * .02;
        funds_earned = Math.round(funds_earned);

        //Creating the table with correct html
        purchasesHTML += "<tr>";
        purchasesHTML += "<td>";
        purchasesHTML += "<div class='d-flex px-2 py-1'>";
        purchasesHTML += "<div class='d-flex px-2 '>";
        purchasesHTML += "<i class='ni ni-credit-card' > </i>";
        purchasesHTML += "</div>";
        purchasesHTML += "<div class='d-flex flex-column justify-content-center'>";
        purchasesHTML += "<h6 class='mb-0 text-sm'>";
        purchasesHTML += jsonObject[key]["purchase_date"] + "</h6>";
        purchasesHTML += "<p class='text-xs text-secondary mb-0'>Purchase Made</p></div></div></td>";

        purchasesHTML += "<td><p class='text-xs font-weight-bold mb-0'>";
        purchasesHTML += jsonObject[key]["purchase_cost"] + "</p>";
        purchasesHTML += "<p class='text-xs text-secondary mb-0'>Dollars</p>";
        purchasesHTML += "</td>" + "<td class='align-middle text-center text-sm'>";

        purchasesHTML += "<span class='badge badge-sm bg-gradient-success'>";
        purchasesHTML +=  funds_earned + "</span>";

        purchasesHTML += "<td>";
        purchasesHTML += "<div class='d-flex px-2 py-1'>";
        purchasesHTML += "<div class='d-flex px-2 '>";
        purchasesHTML += "</div>";
        purchasesHTML += "<div class='d-flex flex-column '>";
        purchasesHTML += "<h6 class='mb-0 text-sm'>";
        purchasesHTML += jsonObject[key]["items_purchased"] + "</h6>";
        purchasesHTML += "</tr>";

        recent_total += funds_earned;

      }
    }
    $("#dataTable tbody").html(purchasesHTML);
    document.getElementById("recentFunds").innerHTML = recent_total;
  });
}
