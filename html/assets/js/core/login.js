//Function to validate user information on login

function validateLogin(){
    let url = "../php/loginAuth.php";
    let form_email = document.getElementById("emailInput").value;
    let form_password = document.getElementById("passwordInput").value;
    $.post(url, { email: form_email, password: form_password }, function (response)
    {
        if (response == 1) // Login Info exists
        {
          window.location.href = "../dashboard.html";
        }
        else {
          document.getElementById("loginError").removeAttribute("hidden");
          console.log("Error in Login");
        }
    })
}
