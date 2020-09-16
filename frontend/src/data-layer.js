

let map
let pathIndex = 0
let zoomLevel = 5.5
let layerCounter = 0
let polygonList = []
let layerLevel = 0
let previousClickedPolygon
let clickedPolygons = []


function initMap(){

  map = new google.maps.Map(document.getElementById('map'), {

    zoom: 5, 

    center: { lat: 39.925533, lng:  32.866287}
  })

  drawPolygons()

}



function makeDarkPolygon(polygon){

    let options = {
        strokeOpacity: 1,
        strokeWeight: 1.2,
        fillOpacity: 0.3,
        fillColor: '#000000',
    }
    polygon.setOptions(options)
    
    polygon.addListener('mouseover', () => polygon.setOptions({
        strokeColor: '#000000',
        strokeOpacity: 1,
        strokeWeight: 1.2,
        fillOpacity: 0.3,
        fillColor: '#00ff00',
    }))
    polygon.addListener('mouseout', () => polygon.setOptions(options))

    console.log('makeDarkPOlygon', polygon)

}


// function resetChildPolygons(childPolygons){

//     let options = {
//         strokeOpacity: 0,
//         strokeWeight: 0,
//         fillOpacity: 0,
//     }
//     console.log('childPolygonssss', childPolygons)
//     for(let polygon of childPolygons){
//         console.log('childddddddddddddddddddddddpolygon', polygon)
//         polygon.setOptions(options)
//         polygon.addListener('mouseover', () => polygon.setOptions(options))
//         polygon.addListener('mouseout', () => polygon.setOptions(options))
//     }

// }

//if clicked polygon layer level is equal to previous then set previous clicked polygon options

function makeDeactive(clickedPolygon, prevClickedPolygon){

    clickedPolygon.setOptions({clickable: false, visible: false})
    if(prevClickedPolygon != null){
        console.log('deactive func')
        if(clickedPolygon.layerLevel <= prevClickedPolygon.layerLevel){

            for(let polygon of prevClickedPolygon.childPolygons){

                polygon.setOptions({clickable: false, visible: false})
                
            
            }
            prevClickedPolygon.setOptions({clickable: true, visible: true})
            console.log('deactive', prevClickedPolygon)

        }
    }
}




function drawPolygons(prevClickedPolygon=null, clickedPolygon=null, model=null){

    let path
    console.log(`model: ${model}`)

    if(prevClickedPolygon != null && prevClickedPolygon.isLastLayer == true) return
    if(model === null){
       
        path = 'region/'
    }
    else if(model !== null && clickedPolygon !== null ){
        path = `${model}/get/${clickedPolygon.id}/`
    }
    if(path === undefined) {
       
        console.log('path is undefined')
        return
    }
    
    fetch(`http://127.0.0.1:8000/service/${path}`)
    .then(res => res.json())
    .then(data => {

        let name
        

       
        let polygonsInClickedPolygon = []
        data.forEach(obj => {
            name = obj.name
            let clickedPolygonModel
            switch(obj.model){
                case 'Region':
                    clickedPolygonModel = 'city'
                    layerLevel = 1
                    zoomLevel = 6.5
                    break
                case 'City':
                    clickedPolygonModel = 'county'
                    layerLevel = 2
                    zoomLevel = 7.5
                    break
                case 'County':
                    clickedPolygonModel = 'neighborhood'
                    layerLevel = 3
                    zoomLevel = 8.5
                    break
                case 'Neighborhood':
                    clickedPolygonModel = ''
                    layerLevel = 4
                    zoomLevel = 9.5
                    break
            }
           
            
            let polygon = new google.maps.Polygon({
                paths: obj.coordinates,
                strokeColor: '#000000',
                strokeOpacity: 1,
                strokeWeight: 1.2,
                fillOpacity: 0,
                name: name,
                id: obj.id,
                layerLevel: layerLevel,
                zoomLevel: zoomLevel,
                childPolygons: [],
                isLastLayer: obj.model === 'Neighborhood' ? true : false,
                model: obj.model
                
            })
            

            
            polygon.addListener('mouseover', () =>{
        
                polygon.setOptions({
                    fillOpacity: 0.3,
                    fillColor: '#00ff00',
                })
            })
        
            polygon.addListener('mouseout', () =>{
        
                polygon.setOptions({
                    strokeColor: '#000000',
                    strokeOpacity: 1,
                    strokeWeight: 1.2,
                    fillOpacity: 0.0,
                })
            })

            polygon.addListener('click', () =>{

                let prevClickedPolygon = clickedPolygons.pop()
                
               
                drawPolygons(prevClickedPolygon, polygon, clickedPolygonModel)

                let bounds = new google.maps.LatLngBounds()
              
                for(let coordinate of obj.coordinates) bounds.extend(coordinate)
                
                map.setOptions({
                    zoom: polygon.zoomLevel,
                    center: bounds.getCenter()
                })
               
                if(!polygon.isLastLayer) makeDarkPolygon(polygon)

                // setPolygons(polygon, prevClickedPolygon)
                makeDeactive(polygon, prevClickedPolygon)

                clickedPolygons.push(polygon)

            })


            polygon.setMap(map)
           
            if(clickedPolygon != null){
                clickedPolygon.childPolygons.push(polygon)
                polygon.setOptions({parentPolygon: clickedPolygon})
               
            }
            
        })

       
    })
    .catch(err => console.log(err))
}








