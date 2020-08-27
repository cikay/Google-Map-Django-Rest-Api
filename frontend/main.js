

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

var _inArray = function(needle, haystack) {
    for(var k in haystack) {
      if(haystack[k] === needle) {
        return true;
      }
    }
    return false;
}

glob("./data/*.json", (err, files) => { 
    if(err) {
        console.log("cannot read the folder, something goes wrong with glob", err);
    }
    var matters = [];
    files.forEach((file) => {
        fs.readFile(file, 'utf8', (err, data) => { // Read each file
            if(err) {
                console.log("cannot read the file, something goes wrong with the file", err);
            }
            console.log(file)
            var parsedData = JSON.parse(data);

            coordinates = parsedData[0].geojson.coordinates
            name = parsedData[0].display_name
            model = parsedData[0].model
            related_model = parsedData[0].related_model
            related_model_name = parsedData[0].related_model_name

            for(let list1 of coordinates[0]){

                list_coordinate.push(list1)
            }

         
            axios.get(`http://127.0.0.1:8000/service/${related_model}/`)
            .then(res => {
                console.log(res.data)
                for(let model of res.data){

                    if(model.name == related_model_name){
                        related_model_id = model.id
                    }
                }
                
            }) 
            .catch(err => console.log(err))

            axios.post(`http://127.0.0.1:8000/service/${model}/detail/`, {polygon: list_coordinate, name: name, related_model_id: id})
            .then(res => res.json()).catch(err => console.log(err))


        });
    });
});

