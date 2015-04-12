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

	setUpPageWrapper();
	   $('#side-menu').metisMenu();

	setUpNavBarDropdown();

	
	var results = $.parseXML(/* API CALL */)


});


//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
function setUpPageWrapper(){

    $(window).bind("load resize", function() {
        var topOffset = 50;
        var width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        var height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    var element = $('ul.nav a').filter(function() {
        return this.href == url || url.href.indexOf(this.href) == 0;
    }).addClass('active').parent().parent().addClass('in').parent();
    if (element.is('li')) {
        element.addClass('active');
    }
}




/**
* Sets up the dummy info for navigation on the top right corner
*/
function setUpNavBarDropdown(){

	var user

 var navBarTopDropdownHtml ='<!-- /.dropdown -->';
 //    <li class="dropdown">
 //        <a class="dropdown-toggle" data-toggle="dropdown" href="#">
 //            <i class="fa fa-bell fa-fw"></i>  <i class="fa fa-caret-down"></i>
 //        </a>
 //        <ul class="dropdown-menu dropdown-alerts">
 //            <li>
 //                <a href="#">
 //                    <div>
 //                        <i class="fa fa-comment fa-fw"></i> New Comment
 //                        <span class="pull-right text-muted small">4 minutes ago</span>
 //                    </div>
 //                </a>
 //            </li>
 //            <li class="divider"></li>
 //            <li>
 //                <a href="#">
 //                    <div>
 //                        <i class="fa fa-twitter fa-fw"></i> 3 New Followers
 //                        <span class="pull-right text-muted small">12 minutes ago</span>
 //                    </div>
 //                </a>
 //            </li>
 //            <li class="divider"></li>
 //            <li>
 //                <a class="text-center" href="#">
 //                    <strong>See All Alerts</strong>
 //                    <i class="fa fa-angle-right"></i>
 //                </a>
 //            </li>
 //        </ul>
 //        <!-- /.dropdown-alerts -->
 //    </li>
 //    <!-- /.dropdown -->
 //    <li class="dropdown">
 //        <a class="dropdown-toggle" data-toggle="dropdown" href="#">
 //            <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>
 //        </a>
 //        <ul class="dropdown-menu dropdown-user">
 //            <li><a href="#"><i class="fa fa-user fa-fw"></i> User Profile</a>
 //            </li>
 //            <li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>
 //            </li>
 //            <li class="divider"></li>
 //            <li><a href="login.html"><i class="fa fa-sign-out fa-fw"></i> Logout</a>
 //            </li>
 //        </ul>
 //        <!-- /.dropdown-user -->
 //    </li>
 //    <!-- /.dropdown -->';

	$(".navbar-top-links").html(navBarTopDropdownHtml);
}

/**
* Displays the Interested Courses List on the left
*/
function displayInterestedCourses(){

}

/**
* Displays the Interested Courses List on the left
*/
function displayCurrentCourses(){

}

/**
* Displays the Top Courses List on top of the course catalog.
*/
function displayTopCourses(){

}

/**
* Displays the Recommended Courses List on top of the course catalog.
*/
function displayRecommendedCourses(){

}


function displayCourseCatalog(){

}
