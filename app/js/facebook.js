function FBstatusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
      testAPI();
    } else if (response.status === 'not_authorized') {
      alert("Not Authorized")
    } else {
      alert("Not Logged into FB") 
    }
  }
    
  function FBcheckLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }
      
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '511140802368207',
      xfbml      : true,
      version    : 'v2.4'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));
    
  function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      alert('you are' + response.name + '!');
    });
  }

function fb_login(){
    FB.login(function(response) {
      var userID = response.authResponse.userID
      console.log(userID)
      
      FB.api('/'+userID, function(response) {
        name = response.name;
        console.log(name)
        
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/flogin');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
          console.log('Signed in as:' + xhr.responseText);
        };
        xhr.send('data=' + JSON.stringify(response));
      });
        
    });
}