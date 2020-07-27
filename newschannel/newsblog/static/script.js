console.log('hello');
$(document).ready(function(){
var url = "https://api.covid19india.org/data.json";
$.getJSON(url,function(data)
{
//console.log(data)
var total_active,total_recovered,total_deaths,total_confirmed
total_active = data.statewise[0].active
total_confirmed = data.statewise[0].confirmed
total_recovered = data.statewise[0].recovered
total_deaths = data.statewise[0].deaths

var state = []
var confirmed = []
var recovered = []
var deaths = []
var active = []

$.each(data.statewise,function(id,obj){
state.push(obj.state)
confirmed.push(obj.confirmed)
recovered.push(obj.recovered)
deaths.push(obj.deaths)
active.push(obj.active)
})
console.log(state)

state.shift()
confirmed.shift()
recovered.shift()
deaths.shift()
console.log(state)
$("#confirmed").append(total_confirmed)
$("#active").append(total_active)
$("#recovered").append(total_recovered)
$("#decreased").append(total_deaths)

var mychart = document.getElementById("mychart").getContext('2d')
var chart = new Chart(mychart,{
type:'line',
data:{
labels:state,
datasets:[
{
 label:'Confirmed-cases',
 data:confirmed,
 backgroundColor:'#f1c40f',
 minBarLength:100,
},
{
 label:'Recovered',
 data:recovered,
 backgroundColor:'#2ecc71',
 minBarLength:100,
},
{
 label:'Decreased',
 data:deaths,
 backgroundColor:'#e74c3c',
 minBarLength:100,
},
{
 label:'Active',
 data:active,
 backgroundColor:'#8f8fab',
 minBarLength:100,
},
]
},
options:{}
})

})
})