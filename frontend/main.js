

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


glob("./data/regions/*.json", (err, files) => { 
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
                    // console.log(res.data)
                    for(let model of res.data){

                        if(model.name == related_model_name){
                            related_model_id = model.id
                        }
                    }
                    
                }) 
                .catch(err => console.log(err))

            }

            axios.post(`http://127.0.0.1:8000/service/${model}/detail/`, {polygon: list_coordinate, name: name, related_model_id: id})
            .then(res => res.json()).catch(err => console.log(err))

        });
    });
});

