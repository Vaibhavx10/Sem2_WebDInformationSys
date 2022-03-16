function subscribe(){
  $('#errorcnt').hide();
    

    userid = $('#userid').val();
    imdbid = $('#imdbID').val();

    console.log(userid )
    console.log(imdbid )

    var infodata = {
      "typevideocontent":"OTT",
      "imdbid":$('#imdbID').val(),
      "videoid":"blank",
      "userid":$('#userid').val()
    };

    document.getElementById("errorMessage").innerHTML = "";
    var submitRes = document.getElementById("errorMessage");


    $.ajax({
        url: 'addSubscriptionInDB',
        async: false,
        dataType: 'json',        
        type: 'POST',
        data: infodata,
        success: function (data) {
            console.log(data)
            var res = `
                 <h1 class="text-success" > You have Subscribed Please Check your registered email ID
                 for download and streaming links <h1>`
                submitRes.innerHTML = submitRes.innerHTML + res
                $('#errorcnt').show();
          } , error: function () {
            var res = `
                 <h1 class="text-danger"> Failed To Subscribed <h1>
                `
                submitRes.innerHTML = submitRes.innerHTML + res
                $('#errorcnt').show();
          }
        }
      )

}

function toggleNavbar(){
  $("#navbarScroll").toggle(); 
}