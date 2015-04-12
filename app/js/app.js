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

	makeDroppable();
	getFiles();
});


/**
* Allows the course catalog items and the course placeholders
* to be draggable and droppable.
*/
function makeDroppable() {

    $( ".course-draggable li" ).draggable({
      appendTo: "body",
      helper: "clone"
    });

    $( ".course-draggable li" ).draggable({
      appendTo: "body",
      helper: "clone"
    });

    $( ".course-placeholder ul" ).droppable({
      activeClass: "ui-state-default",
      hoverClass: "ui-state-hover",
      accept: ":not(.ui-sortable-helper)",
      drop: function( event, ui ) {
        $( this ).find( ".placeholder" ).remove();
        $( "<li></li>" ).text( ui.draggable.text() ).appendTo( this );
      }
    }).sortable({
      items: "li:not(.placeholder)",
      sort: function() {
        // gets added unintentionally by droppable interacting with sortable
        // using connectWithSortable fixes this, but doesn't allow you to customize active/hoverClass options
        $( this ).removeClass( "ui-state-default" );
      }
    });
}

/**
* Get JSON. If successful call getData()
*/
function getFiles(){
	$.parseJSON(econMajor);

}


/**
* Displays the Course Cart List on the left
*/
function displayInterestedCourses(){
    var $interestedCourses = $("#course-cart");


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
    var $courseCat = $("#course-catalog");
}