function login(){
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    

    email=document.getElementById("name").value
    password=document.getElementById("exampleInputPassword1").value
    console.log(email)
    var raw = JSON.stringify({

      "email": email,
      "password": password
    });

    console.log(raw)
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    fetch(" http://127.0.0.1:5000/api/login", requestOptions)
    .then(response => {
      // if (!response.ok) {
      //   throw new Error('Network response was not ok');
      // }
      return response.json();
    })
    .then(data => {
      console.log(data.error);
      var a=data.error
      // console.log(a)
      
      if(a){
        document.getElementById("message").innerText=a

      }
      else{
        
          // document.getElementById("message").innerText="logined successfully"
          window.location.href = "/templates/index.html";
      }
      
    })
    .catch(error => {
      console.error('Error :', error);
    });
}


function post_validation(){
  // alert("ok")
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  tittle=document.getElementById("tittle_id").value
  text=document.getElementById("text_id").value
  // console.log(tittle)
  // console.log(text)
  var raw = JSON.stringify({

    "title": tittle,
    "content": text,
    "user_id":1
  });
  console.log(raw)
  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
  };
  console.log("before")
  fetch("http://127.0.0.1:5000/api/login/post",requestOptions)
  .then(response=>{
    console.log("after")
    return response.json()
  })
  .then(data=>{
    console.log(data)
  })
}

function Account() {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  // username = document.getElementById("username").value
  // password = document.getElementById("password").value
  // var raw = JSON.stringify({
  // "customer_id": username,
  // "password": password
  // });

  console.log("raw")
  var requestOptions = {
  method: 'GET',
  headers: myHeaders
  };

  fetch("http://127.0.0.1:5000/api/login/Account", requestOptions)
  .then(response => {
      return response.json();
      console.log("harish")
  })
  .then(result => {
      // document.getElementById("message").innerText = result.error;
      // document.getElementById("username").value = result.data.username
      document.getElementById("email").value = result.data.email
    console.log(result);
  })
  .catch(err => console.error(err));
}





