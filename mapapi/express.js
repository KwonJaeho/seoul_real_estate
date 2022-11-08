
const express = require('express')
const port = 8090;
const app = express()
const cors = require('cors')
const fs = require('fs')

//cors에 옵션사용할경우
app.use(cors({
    origin : true, credentials: true
}));

app.listen(port, ()=>{
    console.log(`port started with ${port}`)
})

//읽을 제이슨 파일 라우팅
app.get('/data', (req, res)=>{
    fs.readFile(`./JSON/TL_SCCO_SIG.json`, "utf8", (err, data) => {
        if (err) {
          console.error(err);
          res.send({data : 'error'})
        } else {
          res.send({data : data})
        }
      });
    
})

app.get('/', (req, res)=>{
    res.sendFile("C:/Users/wogh2/Desktop/seoul_real-estate/mapapi/1..html")
})