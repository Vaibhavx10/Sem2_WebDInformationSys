function displatytsearchresultfor_home(){
    ytsearch = $("#ytsearch").val();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    // clears the older data gets the new one
    document.getElementById("ytdataResponse").innerHTML = "";
        $.ajax({
            url: '/displatytsearchresultfor_home',
            async: true,
            dataType: 'json',        
            type: 'POST',
            data:{
                  'ytsearch':ytsearch,
                  'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function (data) {
                console.log(data)
                var ytdataResponse ;
                ytdataResponse = document.getElementById("ytdataResponse");
                
                if(data.videos != 'FAIL'){
                    for (let i = 0; i < data.videos.length; i++) {
                        var elem = `<div class="col-md-4">
                            <div class="card mb-4 shadow-sm">
                            <img class="bd-placeholder-img card-img-top" width="100%" height="225" 
                            src=${data.videos[i].thumbnails} preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"></img>
                            <div class="card-body">
                                <p class="card-text">${data.videos[i].title}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <a type="button" href="${data.videos[i].url }"
                                     class="btn btn-md btn-outline-danger">Watch on Youtube </a>
                                </div>
                                <small class="text-muted">${data.videos[i].totaltimeinMinutes} mins</small>
                                </div>
                            </div>
                            </div>
                        </div>`
    
                        ytdataResponse.innerHTML = ytdataResponse.innerHTML + elem
                    }
                }else{
                    var elem = `<blockquote class="blockquote text-danger">
                                    <p>Sorry No Valid Data was found on Youtube !! </p>
                                </blockquote>`
                    ytdataResponse.innerHTML = ytdataResponse.innerHTML + elem
                }





              } , error: function () {
                alert("error");
              }
            }
          )

}

function toggleNavbar(){
    $("#navbarScroll").toggle(); 
}