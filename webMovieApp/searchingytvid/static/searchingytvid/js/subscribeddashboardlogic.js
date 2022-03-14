function initialize() {
    uemail = $('#uemail').val();
    jwtcookie = $('#jwtcookie').val();
    userid = $('#userid').val();
    
    

    var inputparam = {
      "userid":userid
    }

    // Get Data from API using imdbID
    $.ajax({
      url: '/getUserSubscribedData',
      async: false,
      dataType: 'json',        
      type: 'POST',
      data:inputparam,
      success: function (data) {
        var videoContent = document.getElementById("userbased_Content");

          for (let i = 0; i < data.length; i++) {
            console.log("imdbID "+data[i].imdbID+"Title "+data[i].Title) ;
            var setter = `  <div class="col-md-3">
            <div class="card text-center text-success fw-bold">
              <div class="card-body">
                  SUBSCRIBED
              </div>
            </div>
            <div class="card mb-3 shadow-sm">
              <img class="bd-placeholder-img card-img-top" height="400px" src=${data[i].Poster} preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"></img>
              <div class="card-body">
                <p class=" card-text text-center">Name : ${data[i].Title}</p>
                <p class=" card-text col-md-10">Genres : ${data[i].Genre}</p>
                <div class="row">
                    <p class="">Source ${data[i].Ratings[0].Source}</p>
                    <p class="">Value ${data[i].Ratings[0].Value}</p>
                </div>
                <div class="row">
                    <p class="">Country : ${data[i].Country}</p>
                </div>
                <div class="row">
                    <p class="">Type : ${data[i].Type}</p>
                </div>

                <div class="row">
                    <p class="">RunTime : ${data[i].Runtime} </p>
                </div>
                <input type="hidden" id="deleteimdbID" value=${data[i].imdbID} />

                <div class="container">
                    <div class="row">
                      <div class="col text-center">
                          <input type="hidden" name="ytsearch" value="${data[i].Title}" />
                              <div class="col btn-group">
                                  <button onclick=removeVideo('${data[i].imdbID}') class="btn btn-md btn-danger" type="submit"> DELETE </button>
                              </div>
                      </div>
                    </div>
                </div>



              </div>
            </div>
          </div>`
          videoContent.innerHTML = videoContent.innerHTML + setter
          }
          
        } , error: function () {
          alert("initialize error");
        }
      }
    )




    // all random videos un subscribed



  }


  function removeVideo(imdbID){
    
    $('#errorcnt').hide();
    userid = $('#userid').val();
    deleteimdbID = imdbID;
    
    
    var passValue = {
      "userid":userid,
      "deleteimdbID":deleteimdbID
    }
    
    document.getElementById("errorMessage").innerHTML = "";
    var submitRes = document.getElementById("errorMessage");

    $.ajax({
      url: '/deleteVideoEntry',
      async: false,
      dataType: 'json',        
      type: 'POST',
      data:passValue,
      success: function (data) {
          console.log(data)
          var res = `
              <h1 class="text-center text-success">Video Deleted</h1> `
                submitRes.innerHTML = submitRes.innerHTML + res
                $('#errorcnt').show();
        } , error: function () {
          alert("error");
          var res = `
                 <h1 class="text-center text-danger"> Failed To Delete <h1>
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