


const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Silmek istediginiz modeli yaziniz: ', (model) => {
    
    rl.question('silmek istediginiz modelin id numarasini yaziniz: ', (id) => {

        console.log(`model: ${model}, id: ${id}`)

        axios = require('axios')

        axios.delete(`http://127.0.0.1:8000/service/${model}/delete/${id}/`)
        .then(res => {
            console.log(res.data)
        })

    })

})