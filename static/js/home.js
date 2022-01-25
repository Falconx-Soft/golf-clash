const club_type_list = document.querySelectorAll("#club_type_list");
const clubs_dropdown = document.getElementById("clubs_dropdown");

const club_type_lable = document.getElementById("club_type_lable");

for(let i=0; i<club_type_list.length; i++){
	club_type_list[i].addEventListener("click", function(){
		getClubs(club_type_list[i].innerHTML);
		club_type_lable.innerHTML=club_type_list[i].innerHTML;
	});
}

function getClubs(typeName) {
	var mydata = { typeName: typeName };
	$.ajax({
	  url: "/getClubs/",
	  method: "POST",
	  data: mydata,
	  success: function (data) {
		  var output = "";
		  for(let x=0; x<data.club_list.length; x++){
			output += "<a onClick='setClub("+data.club_list[x].id+","+"\""+data.club_list[x].name+"\""+")'>"+data.club_list[x].name+"</a>"
			console.log(output)
		  }
		  clubs_dropdown.innerHTML = output;
	  },
	});
  }

const club_input = document.getElementById("club_input");

const club_lable = document.getElementById("club_lable");

function setClub(id,name){
	club_input.value = id;
	club_lable.innerHTML = name;
}

const ball_power_list = document.querySelectorAll("#ball_power_list");
const ball_power_input = document.getElementById("ball_power_input");
const ball_power_lable = document.getElementById("ball_power_lable");
for(let i=0; i<ball_power_list.length; i++){
	ball_power_list[i].addEventListener("click", function(){
		ball_power_input.value = ball_power_list[i].innerHTML;
		ball_power_lable.innerHTML = ball_power_list[i].innerHTML;
	});
}

const club_level_list = document.querySelectorAll("#club_level_list");
const club_level_input = document.getElementById("club_level_input");
const club_level_lable = document.getElementById("club_level_lable");
for(let i=0; i<club_level_list.length; i++){
	club_level_list[i].addEventListener("click", function(){
		club_level_input.value = club_level_list[i].innerHTML;
		club_level_lable.innerHTML=club_level_list[i].innerHTML;
	});
}