

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



function makeDarkPolygon(clickedPolygon){

    let options = {
        strokeOpacity: 1,
        strokeWeight: 1.2,
        fillOpacity: 0.3,
        fillColor: '#000000',
    }

    if(clickedPolygon.parentPolygon != null){
        
        for(let polygon of clickedPolygon.parentPolygon.childPolygons){

            if(polygon === clickedPolygon) continue
            polygon.setOptions(options)
            polygon.addListener('mouseout', () => polygon.setOptions(options)) // mouse ayrildiginda tekrar koyulastirilir, polygon ilk olusturuldugunda koyu degil 
          
        }

    }
    
}


function makeDeactive(clickedPolygon, prevClickedPolygon){
    
    clickedPolygon.setOptions({clickable: false, visible: false})
    if(prevClickedPolygon != null){
        if(clickedPolygon.layerLevel <= prevClickedPolygon.layerLevel){
            
            while(true){

                if(prevClickedPolygon.layerLevel < clickedPolygon.layerLevel) break

                for(let polygon of prevClickedPolygon.childPolygons){

                    polygon.setOptions({clickable: false, visible: false})
                    console.log('disabled polygon name:', polygon.name)
                }
                prevClickedPolygon.setOptions({clickable: true, visible: true})
                prevClickedPolygon = prevClickedPolygon.parentPolygon

            }

        }
    }
    
    if(clickedPolygon.earlierCreatedChildPolygons){
        console.log('clicked polygon has child polygons')
        for(let polygon of clickedPolygon.childPolygons){

            polygon.setOptions({clickable: true, visible: true})
            
        }
        console.log('neden iki kez')
    }

}




function drawPolygons(prevClickedPolygon=null, clickedPolygon=null, model=null){

    let path
    console.log(`model: ${model}`)
    if(clickedPolygon != null && clickedPolygon.isLastLayer == true){
        console.log('last layer')
        return
    }

    if(model === null){
       
        path = 'region/'
    }
    else if(model !== null && clickedPolygon !== null ){
        path = `${model}/get/${clickedPolygon.id}/`
        
    }
    if(path === null) {
       
        console.log('path is undefined')
        return
    }

    if(clickedPolygon !== null && clickedPolygon.childPolygons.length){
        console.log('Earlier created child polygons of clicked polygon, no need to make http request.')
        clickedPolygon.setOptions({earlierCreatedChildPolygons: true})
        return 
    }
    
    fetch(`http://127.0.0.1:8000/service/${path}`)
    .then(res => res.json())
    .then(data => {

        if(data.length === 0){
            
            return
        }

        let name
        console.log(data)
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
                    zoomLevel = 15
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
                model: obj.model,
                earlierCreatedChildPolygons: false,

                
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








