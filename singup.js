function registration(){
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    
  // alert("hi")
    // username=document.getElementById("username").value
    email=document.getElementById("exampleInputEmail1").value
    password=document.getElementById("exampleInputPassword1").value
    confirm_password=document.getElementById("cexampleInputPassword1").value
    
    var raw = JSON.stringify({

    //   "name": username,
      "email": email,
      "password": password,
      "confirm_password":confirm_password
    });
    console.log(raw)
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
   var div = document.getElementById("message")
    fetch("http://127.0.0.1:5000/api/register", requestOptions)
    .then(response => {
      // if (!response.ok) {
      //   throw new Error('Network response was not ok');
      // }
      return response.json();
    })
    .then(data => {
      console.log(data.error);
      var a=data.error
    //   console.log(a)
      // if (a.length==0)
      if(a){
        // document.getElementsByClassName(".alert alert-success")
        div.innerHTML=a

      }
      else{
        // print("haelo")
        // document.getElementById("message").innerHTML="success"
        window.location.href = "/templates/login.html";

      }

    })
    .catch(error => {
      console.error('Error registering user:', error);
    });
}
   
