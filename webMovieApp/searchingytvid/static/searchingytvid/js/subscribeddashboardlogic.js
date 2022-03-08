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
            console.log(data[i]) ;
            var setter = `  <div class="col-md-3">
            <div class="card text-center text-success fw-bold">
              <div class="card-body">
                  SUBSCRIBED
              </div>
            </div>
            <div class="card mb-3 shadow-sm">
              <img class="bd-placeholder-img card-img-top" height="400px" src=${data[i].Poster} preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"></img>
              <div class="card-body">
                <p class="font-monospace card-text text-center">Name : ${data[i].Title}</p>
                <p class="font-monospace card-text col-md-10">Genres : ${data[i].Genre}</p>
                <div class="row">
                    <p class="font-monospace">Source ${data[i].Ratings[0].Source}</p>
                    <p class="font-monospace">Value ${data[i].Ratings[0].Value}</p>
                </div>
                <div class="row">
                    <p class="font-monospace">Country : ${data[i].Country}</p>
                </div>
                <div class="row">
                    <p class="font-monospace">Type : ${data[i].Type}</p>
                </div>

                <div class="row">
                    <p class="font-monospace">RunTime : ${data[i].Runtime} </p>
                </div>
                <input type="hidden" id="deleteimdbID" value=${data[i].imdbID} />

                <div class="container">
                    <div class="row">
                      <div class="col text-center">
                          <input type="hidden" name="ytsearch" value="${data[i].Title}" />
                              <div class="col btn-group">
                                  <button onclick=removeVideo() class="btn btn-md btn-danger" type="submit"> DELETE </button>
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


  function removeVideo(){
    userid = $('#userid').val();
    deleteimdbID = $('#deleteimdbID').val();
    
    var passValue = {
      "userid":userid,
      "deleteimdbID":deleteimdbID
    }


    $.ajax({
      url: '/deleteVideoEntry',
      async: false,
      dataType: 'json',        
      type: 'POST',
      data:passValue,
      success: function (data) {
          console.log(data)
        } , error: function () {
          alert("error");
        }
      }
    )

  }