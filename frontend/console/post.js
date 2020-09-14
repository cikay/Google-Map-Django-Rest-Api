



const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Klasor ismi giriniz: ', (folderName) => {
   
   
    rl.question('okunacak json dosya ismini yaziniz:', (fileName) => {
        let coordinates
        let name 
        let list_coordinate = []
        let model
        let related_model
        let related_model_name
        
        var fs = require("fs");
        var axios = require('axios')

        fs.readFile(`../data/${folderName}/${fileName}`, 'utf8', (err, data) => { 

            if(err) {
                console.log("cannot read the file, something goes wrong with the file", err);
                return
            }
            console.log(`file name: ../data/${folderName}/${fileName}`)
        
            var parsedData = JSON.parse(data);
    
            coordinates = parsedData[0].geojson.coordinates
            name = parsedData[0].display_name
            model = parsedData[0].model
            related_model = parsedData[0].related_model
            related_model_name = parsedData[0].related_model_name
    
            for(let list1 of coordinates[0]){
    
                list_coordinate.push(list1)
            }
    
            if(model != 'region'){
            
                axios.post(`http://127.0.0.1:8000/service/${model}/post/`, {polygon: list_coordinate, name: name, related_model_name: related_model_name})
                .then(res => {
                    console.log('post edildi')
                }).catch(err => console.log(err))
            }
            else {
                axios.post(`http://127.0.0.1:8000/service/${model}/post/`, {polygon: list_coordinate, name: name})
                .then(res => {
                    console.log('post edildi')
                }).catch(err => console.log(err))
            }
    
        });
        rl.close()
    })


});


