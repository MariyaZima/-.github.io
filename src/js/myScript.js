"use strict"

let question = confirm("Рассчитаем стоимость и сроки?", "Да или нет");
if (question === true)
   {alert ("Тогда начнем!!!");
	
let type = prompt("Какой тип сайта Вас интересует? (указать номер)", "1 - Сайт-визитка 2 - Интернет-магазин 3 - Корпоративный сайт");
if (type <= 3)
   {alert ("Вы выбрали " + ": " + type);}
	else {
    alert ("Вы ничего не выбрали!");}
	if (type == 1){
		alert ("Стоимость - 5 000руб");
	console.log(type + " = " + "5000");}
	if (type == 2){
		alert ("Стоимость - 20 000руб");
	console.log(type + " = " + "20000");}
	if (type == 3){
		alert ("Стоимость - 10 000руб");
	console.log(type + " = " + "10000");}
	console.log(type);
		
let design = prompt("Какой стиль дизайна Вас интересует?", "1 - Классический 2 - Минимализм 3 - Рисованный 4 - Ретро");		
if (design <= 4){		
alert("Вы выбрали " + ": " + design);}		
	else {	
    alert ("Вы ничего не выбрали!");}		
	if (design == 1){	
		alert ("Стоимость - 1 000руб");
	console.log(design + " = " + "1000");}
	if (design == 2){	
		alert ("Стоимость - 2 000руб");
	console.log(design + " = " + "2000");}
	if (design == 3){	
		alert ("Стоимость - 3 000руб");
	console.log(design + " = " + "3000");}
	if (design == 4){	
		alert ("Стоимость - 4 000руб");
	console.log(design + " = " + "4000");}
    console.log(design);																		
		
		
let adaptive = prompt("Должен ли сайт быть адаптивен?", "Да или Нет");		
if (adaptive === "Да" || "Нет"){		
alert("Вы выбрали " + ": " + adaptive);}		
else {		
alert ("Вы ничего не выбрали!");}		
	if (adaptive == "Да"){	
		alert ("Стоимость - 15 000руб");
	console.log(adaptive + " = " + "15000");}
	if (adaptive == "Нет"){	
		alert ("Стоимость - 5 000руб");
	console.log(adaptive + " = " + "5000");}
	console.log(adaptive);}	

	else {
    alert ("Вы нажали отмена");
	}console.log(question);

















