$(document).ready(function ($) {

	$.getJSON('../getSounds/', function(data) {
	soundItems = [];
	var items = [];
	for (var i=0; i<data.length;i++) //Object {soundFiles: Array[5], folderName: "sounds"}
	{ 
		items.push('<ul class="small-block-grid-2 medium-block-grid-3 large-block-grid-5">');
		folderName = data[i]["folderName"];
		if (folderName != "sounds") {
			items.push('<h3>' + folderName + '</h3>')	
		}
		
		for (var j=0; j<data[i]["soundFiles"].length;j++) {
			soundName = data[i]["soundFiles"][j];

			/*
			<li>
				<a href="#" class="button" data-dropdown="hover1" data-options="is_hover:true">Has Hover Dropdown</a>

				<ul id="hover1" class="f-dropdown" data-dropdown-content>
				  <li><a href="#">This is a link</a></li>
				  <li><a href="#">This is another</a></li>
				  <li><a href="#">Yet another</a></li>
				</ul>
			</li>	
			*/

	    	divClass = '<li>';
	    	soundButton = '<a href="#" class="button soundplayer" data-dropdown="hover' + i + j +'" data-options="is_hover:true" data-id="' + folderName + '/' + soundName[0] + '">' + soundName[1] + '</a>';
	    	previewButton = '<ul id="hover' + i + j + '" class="f-dropdown" data-dropdown-content="">'
	    	previewButton += '<li><a href="#" data-id="' + folderName + '/' + soundName[0] +'" onclick="playPreview($(this))">Preview Sound Locally</a></li></ul>'
	    	
			divClass += soundButton + previewButton + '</li>'
	    	items.push(divClass);
	    	soundItems.push([folderName + '/' + soundName[0], soundName[1]]);
		}
		items.push('</ul>');
	}
  	for (var item in items){
  		$("#button_grid").append(items[item]);
  	}

  	$(".button").click(function() {
  		var name = this.getAttribute("data-id");
  		$.get('../play/' + name, function(data) {
				// console.log("played");
		});
	})
	$(document).foundation();

	var substringMatcher = function(strs) {
	  return function findMatches(q, cb) {
	    var matches, substringRegex;
	 
	    // an array that will be populated with substring matches
	    matches = [];
	 
	    // regex used to determine if a string contains the substring `q`
	    substrRegex = new RegExp(q, 'i');
	 
	    // iterate through the pool of strings and for any string that
	    // contains the substring `q`, add it to the `matches` array
	    $.each(strs, function(i, str) {
	      if (substrRegex.test(str)) {
	        // the typeahead jQuery plugin expects suggestions to a
	        // JavaScript object, refer to typeahead docs for more info
	        matches.push({ value: str });
	      }
	    });
	 
	    cb(matches);
	  };
	};

 
	$('#the-basics .typeahead').typeahead({
	  hint: true,
	  highlight: true,
	  minLength: 1
	},
	{
	  name: 'sounds',
	  displayKey: function(item) {
	    return item.value[1]
		},
	  source: substringMatcher(soundItems)
	}).bind('typeahead:selected', function(obj, datum, name) {
			$.get('../play/' + datum.value[0]);
		}).bind('typeahead:autocompleted', function(obj, datum, name) {
			$.get('../play/' + datum.value[0]);
		});

	});

	playPreview = function(p){
		var soundName = $(p).attr("data-id");
		$(preview_player)[0].src = "../preview/" + soundName;
		$(preview_player)[0].play();
	}


	// variable to hold request
	var request;
	// bind to the submit event of our form
	$("#talker").submit(function(event){
	// abort any pending request
	if (request) {
	    request.abort();
	}
	// setup some local variables
	var $form = $(this);
	// let's select and cache all the fields
	var $inputs = $form.find("input, select, button, textarea");
	// serialize the data in the form
	var serializedData = $form.serialize();

	// let's disable the inputs for the duration of the ajax request
	$inputs.prop("disabled", true);

	// fire off the request to /form.php
	var request = $.ajax({
	    url: "/speak/",
	    type: "post",
	    data: serializedData
	});

	// callback handler that will be called on success
	request.done(function (response, textStatus, jqXHR){
	    // log a message to the console
	    // console.log("Hooray, it worked!");
	});

	// callback handler that will be called on failure
	request.fail(function (jqXHR, textStatus, errorThrown){
	    // log the error to the console
	    console.error(
	        "The following error occured: "+
	        textStatus, errorThrown
	    );
	});

	// callback handler that will be called regardless
	// if the request failed or succeeded
	request.always(function () {
	    // reenable the inputs
	    $inputs.prop("disabled", false);
	});

	// prevent default posting of form
	event.preventDefault();
	});

	/* Use this js doc for all application specific JS */

	/* TABS --------------------------------- */
	/* Remove if you don't need :) */

	function activateTab($tab) {
		var $activeTab = $tab.closest('dl').find('a.active'),
				contentLocation = $tab.attr("href") + 'Tab';
				
		// Strip off the current url that IE adds
		contentLocation = contentLocation.replace(/^.+#/, '#');

		//Make Tab Active
		$activeTab.removeClass('active');
		$tab.addClass('active');

    //Show Tab Content
		$(contentLocation).closest('.tabs-content').children('li').hide();
		$(contentLocation).css('display', 'block');
	}

	$('dl.tabs').each(function () {
		//Get all tabs
		var tabs = $(this).children('dd').children('a');
		tabs.click(function (e) {
			activateTab($(this));
		});
	});

	if (window.location.hash) {
		activateTab($('a[href="' + window.location.hash + '"]'));
		$.foundation.customForms.appendCustomMarkup();
	}

	/* ALERT BOXES ------------ */
	$(".alert-box").delegate("a.close", "click", function(event) {
    event.preventDefault();
	  $(this).closest(".alert-box").fadeOut(function(event){
	    $(this).remove();
	  });
	});


	/* PLACEHOLDER FOR FORMS ------------- */
	/* Remove this and jquery.placeholder.min.js if you don't need :) */

	$('input, textarea').placeholder();

	/* TOOLTIPS ------------ */
	$(this).tooltips();



	/* UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE6/7/8 SUPPORT AND ARE USING .block-grids */
//	$('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'left'});
//	$('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'left'});
//	$('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'left'});
//	$('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'left'});



	/* DROPDOWN NAV ------------- */

	var lockNavBar = false;
	$('.nav-bar a.flyout-toggle').live('click', function(e) {
		e.preventDefault();
		var flyout = $(this).siblings('.flyout');
		if (lockNavBar === false) {
			$('.nav-bar .flyout').not(flyout).slideUp(500);
			flyout.slideToggle(500, function(){
				lockNavBar = false;
			});
		}
		lockNavBar = true;
	});
  if (Modernizr.touch) {
    $('.nav-bar>li.has-flyout>a.main').css({
      'padding-right' : '75px'
    });
    $('.nav-bar>li.has-flyout>a.flyout-toggle').css({
      'border-left' : '1px dashed #eee'
    });
  } else {
    $('.nav-bar>li.has-flyout').hover(function() {
      $(this).children('.flyout').show();
    }, function() {
      $(this).children('.flyout').hide();
    })
  }

  
});
