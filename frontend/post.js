

let coordinates
let id
let name 
let list_coordinate = []
let model
let related_model
let related_model_name
let related_model_id

var glob = require("glob");
var fs = require("fs");
var axios = require('axios')


glob("./data/counties/*.json", (err, files) => { 
    if(err) {
        console.log("cannot read the folder, something goes wrong with glob", err);
    }
    console.log('in glob')
    console.log(`files: ${files}`)
    var matters = [];
    files.forEach((file) => {
        fs.readFile(file, 'utf8', (err, data) => { 
            if(err) {
                console.log("cannot read the file, something goes wrong with the file", err);
            }
           
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
                axios.get(`http://127.0.0.1:8000/service/${related_model}/`)
                .then(res => {
                    console.log(`related_model_name ${related_model_name}`)
                    for(let model of res.data){
                        if(model.name == related_model_name){
                            related_model_id = model.id
                            console.log(model)
                            console.log(`related_model_id: ${related_model_id}`)
                        }
                    }

                    console.log(`related model id: ${related_model_id}`)
                    axios.post(`http://127.0.0.1:8000/service/${model}/detail/`, {polygon: list_coordinate, name: name, related_model_id: related_model_id})
                    .then(res => {}).catch(err => console.log(err))
                    
                }) 
                .catch(err => console.log(err))

            }
            else {
                axios.post(`http://127.0.0.1:8000/service/${model}/detail/`, {polygon: list_coordinate, name: name})
                .then(res => console.log(res)).catch(err => console.log(err))

            }

        
        });
    });
});

