(function() {
    'use strict';
    window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }

          form.classList.add('was-validated');
          console.log("Need to add API Call")

          var newuserdetails = { "fname":$('#validationCustom01').val(),
          "lname":$('#validationCustom02').val(),
          "uname":$('#validationCustomUsername').val(),
          "uemail":$('#validationCustomUsername').val(),
          "age":$('#validationCustom06').val(),
          "gender":$('#validationCustom07').val(),
          "genre":$('#validationCustom08').val(),
          "role":$('#validationCustom09').val(),
          "upass":$('#validationCustom10').val(),
        };

          document.getElementById("ajaxresponse").innerHTML = "";
          var submitRes = document.getElementById("ajaxresponse");


          $.ajax({
            url: '/users/regInfoToDB',
            async: false,
            dataType: 'json',        
            type: 'POST',
            data:newuserdetails,
            success: function (data) {
                console.log(data)
                alert(" >> "+data['uname'])
                var res = `
                 <h1> Success in Registering `+data['uname']+`<h1>`
                submitRes.innerHTML = submitRes.innerHTML + res
              } , error: function () {
                var res = `
                 <h1> Failed To Register User <h1>
                `
                submitRes.innerHTML = submitRes.innerHTML + res
              }
            }
          )


        }, false);
      });
    }, false);
  })();

function toggleNavbar(){
    $("#navbarScroll").toggle(); 
}