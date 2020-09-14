

axios = require('axios')


axios.get(`http://127.0.0.1:8000/service/city/get/${1}`)
.then(res => {

    for(let model of res.data){
        for(let coordinate of model.polygon){
            console.log(coordinate)
        }
    }
})