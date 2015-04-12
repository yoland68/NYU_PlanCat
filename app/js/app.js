/*
██████╗  ██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███╗   ██╗██████╗ ███████╗
██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗████╗  ██║██╔══██╗╚══███╔╝
██████╔╝██║   ██║██████╔╝██║     ██║   ██║██████╔╝██╔██╗ ██║██████╔╝  ███╔╝ 
██╔═══╝ ██║   ██║██╔═══╝ ██║     ██║   ██║██╔══██╗██║╚██╗██║██╔══██╗ ███╔╝  
██║     ╚██████╔╝██║     ╚██████╗╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████╗
╚═╝      ╚═════╝ ╚═╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

By: Chris Jimenez & Yoland                                                                            
app.js
*/

'use strict';


/**
*  Run when DOM is ready.
*/
$(document).ready(function(){

	function getMajorData(){

	var 

	var $majorDataJSON = $.parseJSON('../../hardcore_scraper/json/Economics_(ECON-UA).json');

	console.log($majorDataJSON);

	var major = $majorDataJSON["major_id"];

	// Array of course objects
	var courses = $majorDataJSON["courses"];




}



/**
* Displays the Interested Courses List on the left
*/
function displayInterestedCourses(){
    var $interestedCourses = $("#interested-courses");


}

/**
* Displays the Interested Courses List on the left
*/
function displayCurrentCourses(){
    var $currentCourses = $("#current-courses");
   

}

/**
* Displays the Top Courses List on top of the course catalog.
*/
function displayTopCourses(){
    var $topCourses = $("#top-courses");

}

/**
* Displays the Recommended Courses List on top of the course catalog.
*/
function displayRecommendedCourses(){
    var $recCourses = $("#rec-courses");

}


function displayCourseCatalog(){

		getMajorData();


    var $courseCat = $("#course-catalog");

}




});



