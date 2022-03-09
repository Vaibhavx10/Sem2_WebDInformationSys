function subscribe(){
    

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

    $.ajax({
        url: 'addSubscriptionInDB',
        async: false,
        dataType: 'json',        
        type: 'POST',
        data: infodata,
        success: function (data) {
            console.log(data)
            alert(" >> "+data['uname'])
          } , error: function () {
            alert("error");
          }
        }
      )






}