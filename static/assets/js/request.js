// function getData(){

//     fetch("http://127.0.0.1:8000/api/",{
//         "method": "GET",
       
//     })
//     .then(response => response.json().then(data => {
//         console.log(response);
//     }))
// }

// getData()


fetch('http://127.0.0.1:8000/api/')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
  });