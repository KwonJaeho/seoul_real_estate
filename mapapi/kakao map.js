
window.addEventListener('load',(e)=>{
    console.log(e)

    fetch("http://localhost:8090/data", {
        method: "get",
        headers: {
            "Content-Type": "application/json",
        },
    }).then((response) => response.json())
    .then((data) => {
        
        console.log(data.data)}
    );
})




// $.ajax({        
//     type:"GET",
//     url:"http://localhost:8090",                    //http://localhost:8090에 AJAX요청
//     data:{},
//     dataType:"json",        
//     success:function(data){            
                                
//         var data = json.features;
//         var coordinates = [];
//         var name = '';
//         $.each(data, function(index, val){
//             coordinates = val.geometry.coordinates;
//             name = val.properties.SIG_KOR_NM;
//             displayArea(coordinates, name);
//         });
//     }
// });    



//     polygons.push(polygon);

//     // 다각형에 mouseover 이벤트를 등록하고 이벤트가 발생하면 폴리곤의 채움색을 변경합니다 
//     // 지역명을 표시하는 커스텀오버레이를 지도위에 표시합니다
//     kakao.maps.event.addListener(polygon, 'mouseover', function(mouseEvent) {
//         polygon.setOptions({fillColor: '#09f'});

//         customOverlay.setContent('<div class="area">' + area.name + '</div>');
        
//         customOverlay.setPosition(mouseEvent.latLng); 
//         customOverlay.setMap(map);
//     });

//     // 다각형에 mousemove 이벤트를 등록하고 이벤트가 발생하면 커스텀 오버레이의 위치를 변경합니다 
//     kakao.maps.event.addListener(polygon, 'mousemove', function(mouseEvent) {
        
//         customOverlay.setPosition(mouseEvent.latLng); 
//     });

//     // 다각형에 mouseout 이벤트를 등록하고 이벤트가 발생하면 폴리곤의 채움색을 원래색으로 변경합니다
//     // 커스텀 오버레이를 지도에서 제거합니다 
//     kakao.maps.event.addListener(polygon, 'mouseout', function() {
//         polygon.setOptions({fillColor: '#fff'});
//         customOverlay.setMap(null);
//     }); 

//     // 다각형에 click 이벤트를 등록하고 이벤트가 발생하면 다각형의 이름과 면적을 인포윈도우에 표시합니다 
//     kakao.maps.event.addListener(polygon, 'click', function(mouseEvent) {
//         var content = '<div class="info">' + 
//                     '   <div class="title">' + area.name + '</div>' +
//                     '   <div class="size">총 면적 : 약 ' + Math.floor(polygon.getArea()) + ' m<sup>2</sup></div>' +
//                     '</div>';

//         infowindow.setContent(content); 
//         infowindow.setPosition(mouseEvent.latLng); 
//         infowindow.setMap(map);
//     });
// }