function GOOGonSignIn(googleUser) {
//  var profile = googleUser.getBasicProfile();
  var token = googleUser.getAuthResponse().id_token;
  
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/glogin');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onload = function() {
    console.log('Signed in as: ' + xhr.responseText);
  };
  xhr.send('idtoken=' + token);
}

function GOOGonSignOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log('User signed out.');
  });
}

function GOOGonFailure(error) {
  console.log(error);
}


function GOOGrenderButton() {
  gapi.signin2.render('goog-signup', {
    'scope': 'https://www.googleapis.com/auth/plus.login',
    'width': 300,
    'height': 60,
    'longtitle': true,
    'theme': 'dark',
    'onsuccess': GOOGonSignIn,
    'onfailure': GOOGonFailure
  });
  
  gapi.signin2.render('goog-signin', {
    'scope': 'https://www.googleapis.com/auth/plus.login',
    'width': 300,
    'height': 60,
    'longtitle': true,
    'theme': 'dark',
    'onsuccess': GOOGonSignIn,
    'onfailure': GOOGonFailure
  });
}