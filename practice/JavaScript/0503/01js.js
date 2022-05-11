axios.get('https://jsonplaceholder.typicode.com/users') // 비동기 처리
  .then((res) => {                                      // 비동기 처리가 성공하면
    console.log(res);                                   // 출력이 str이 아닌 object 형식인데 이는 axios에서 처리해 줘서 이다.
    console.log(res.data);
    return res.data
  })
  .then((rlt) => {
    console.log(rlt);
  })
  .catch((err)=>{                                       //처리가 실패하면
    console.log(err);
  })
  .then((rlt) => {
    console.log(rlt);
  })







