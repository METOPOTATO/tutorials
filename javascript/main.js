function request(url) {
  return new Promise((resolve, reject) => { //Chỗ này mới, sử dụng Promise thay vì Callback
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function Success() {
      if (this.readyState === xhr.DONE) {
        resolve(JSON.parse(xhr.responseText));  //Chỗ này không có callback nữa để gọi. Ta dùng hàm resolve() để trả về kết quả.
      }
    };
    xhr.open("GET", url, true);
    xhr.send();
    xhr.onerror = function(error) {
      reject("Error");
    };
  });
}

request("https://api.github.com/search/users?q=location:delhi")
  .then(data1 => {
    console.log(data1);
    return request("https://jsonplaceholder.typicode.com/posts/1");
  })
  .then(data2 => {
    console.log(data2);
    return request("https://api.icndb.com/jokes/random/1");
  })
  .then(data3 => {
    console.log(data3);
    return request("https://jsonplaceholder.typicode.com/posts/2");
  })
  .then(data4 => {
    console.log(data4);
  })
  .catch(error => {
    console.log(error);
  });
