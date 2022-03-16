
function toggleNavbar(){
    $("#navbarScroll").toggle(); 
}

function initialize(){
  $('.01invalid-feedback').hide();
  $('.02invalid-feedback').hide();
  $('.03invalid-feedback').hide();
  $('.10invalid-feedback').hide();
  $('.06invalid-feedback').hide();
  $('.08invalid-feedback').hide();
  $('.09invalid-feedback').hide();
  

}

function sendtoDB(){
  document.getElementById("ajaxresponse").innerHTML = "";
  var submitRes = document.getElementById("ajaxresponse");
  
  $('.01invalid-feedback').hide();
  $('.02invalid-feedback').hide();
  $('.03invalid-feedback').hide();
  $('.10invalid-feedback').hide();
  $('.06invalid-feedback').hide();
  $('.08invalid-feedback').hide();
  $('.09invalid-feedback').hide();
  


  
    var fname = $('#validationCustom01').val().trim();
    var lname = $('#validationCustom02').val().trim();
    var uname = $('#validationCustomUsername').val().trim();
    var age = $('#validationCustom06').val().trim();
    var gender = $('#validationCustom07').val().trim();
    var genre = $('#validationCustom08').val().trim();
    var role = $('#validationCustom09').val().trim();
    var upass = $('#validationCustom10').val().trim();

    if(fname.length == 0){ 
      $('.01invalid-feedback').show();
      var res = `<h3> Validation Failed <h3> `  
      submitRes.innerHTML = submitRes.innerHTML + res
      return false;
    }else if(lname.length == 0){ 
      $('.02invalid-feedback').show();
      var res = `<h3> Validation Failed <h3> `  
      submitRes.innerHTML = submitRes.innerHTML + res
      return false;
    }else if(uname.length == 0){ 
      $('.03invalid-feedback').show();
      var res = `<h3> Validation Failed <h3> `  
      submitRes.innerHTML = submitRes.innerHTML + res
      return false;
    }else if(upass.length == 0){
      $('.10invalid-feedback').show();
      var res = `<h3> Validation Failed <h3> `  
      submitRes.innerHTML = submitRes.innerHTML + res
      return false;
    }else if(age.length == 0){ 
      $('.06invalid-feedback').show();
      var res = `<h3> Validation Failed <h3> `  
      submitRes.innerHTML = submitRes.innerHTML + res
      return false;
    }else if(genre.length == 0){ 
      $('.08invalid-feedback').show();
      var res = `<h3> Validation Failed <h3> `  
      submitRes.innerHTML = submitRes.innerHTML + res
      return false;
    }else if(role.length == 0){ 
      $('.09invalid-feedback').show();
      var res = `<h3> Validation Failed <h3> `  
      submitRes.innerHTML = submitRes.innerHTML + res
      return false;
    }else{
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

      


            $.ajax({
              url: '/users/regInfoToDB',
              async: false,
              dataType: 'json',        
              type: 'POST',
              data:newuserdetails,
              success: function (data) {
                  console.log(data)
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


    }


    
}