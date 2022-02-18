// 마우스 이벤트
let pic = document.getElementById("pic");

// 마우스 올리기 - onmouseover / 마우스 내리기 - onmouseout
//pic.onmouseover = changePic;        // 함수 호출시 괄호 생략
//pic.onmouseout = originPic;

// addEventListener() - mouseover, mouseout 사용 (on 생략)
pic.addEventListener('mouseover', changePic);
pic.addEventListener('mouseout', originPic);

function changePic(){
    pic.src = '../static/coffee-blue.jpg';
}

function originPic(){
    pic.src = '../static/coffee-gray.jpg';
}