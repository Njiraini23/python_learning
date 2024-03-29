function get(url) {
  //Return a new promise
  return new Promise(function(resolve, reject) {
  var req = new XMLHttpRequest();
  req.open('GET', url);
	
  req.onload = function() {
  //This is called even on 404 etc
  // So check the status
  if (req.status == 200) {
    //Resolve the promise with the response text
    resolve(req.response);
  }
  else {
    reject(Error(req.statusText));
  }
  };


  //Handle network errors
  req.onerror = function() {
    reject(Error("Network Error"));
  };

  // Make the request
  req.send();
  });
}
