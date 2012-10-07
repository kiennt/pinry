/**
 * Based on Wookmark's endless scroll.
 */
var apiURL = '/api/pin/?format=json&offset='
var page = 0;
var isLastPage = false;
var handler = null;
var globalTag = null;
var isLoading = false;

/**
 * When scrolled all the way to the bottom, add more tiles.
 */
function onScroll(event) {
  if(!isLoading && !isLastPage) {
      var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
      if(closeToBottom)
          loadData();
  }
};

function applyLayout() {
  $('#pins').imagesLoaded(function() {
      // Clear our previous layout handler.
      if(handler) handler.wookmarkClear();

      // Create a new layout handler.
      handler = $('#pins .pin');
      handler.wookmark({
          autoResize: true,
          offset: 3,
          itemWidth: 242
      });
  });
};

/**
 * Loads data from the API.
 */
function loadData(tag) {
    isLoading = true;
    $('#loader').show();

    if (tag !== undefined) {
        globalTag = tag;
    }

    if (tag !== undefined && page != 0) {
        $('#pins').html('');
        page = 0;
        if (tag != null) $('.tags').html('<span class="label tag" onclick="loadData(null)">' + tag + ' x</span>');
        else $('.tags').html('');
    }

    var loadURL = apiURL+(page*API_LIMIT_PER_PAGE);
    if (globalTag !== null) loadURL += "&tag=" + tag;

    $.ajax({
        url: loadURL,
        success: onLoadData
    });
};

/**
 * Receives data from the API, creates HTML for images and updates the layout
 */
function onLoadData(data) {
    data = data.objects;
    isLoading = false;
    $('#loader').hide();

    page++;

    var html = '';
    var i=0, length=data.length, image;

    for(; i<length; i++) {
        image = data[i];
        html += '<div class="pin">';
        html += '   <div class="pin-options">';

        if (image.is_owner) {
            html += '       <a href="/pins/delete-pin/'+image.id+'/">';
            html += '           <div class="icon-trash"></div>';
            html += '       </a>';
        }

        html += '       <a href="/pins/'+image.id+'/like">';
        html += '           <div class="icon-heart"></div>';
        html += '       </a>';

        html += '       <a href="/pins/'+image.id+'/comment">';
        html += '           <div class="icon-comment"></div>';
        html += '       </a>';

        html += '       <a href="/pins/'+image.id+'/repin">';
        html += '           <div class="icon-retweet"></div>';
        html += '       </a>';

        html += '   </div>';

        html += '   <a class="fancybox" rel="pins" href="'+image.image+'">';
        html += '       <img src="'+image.thumbnail+'" width="200" >';
        html += '   </a>';

        if (image.description)
            html += '   <p>'+image.description+'</p>';
        if (image.tags) {
            html += '   <p>';
            for (tag in image.tags) {
                html += '       <span class="label tag" onclick="loadData(\'' + image.tags[tag] + '\')">' + image.tags[tag] + '</span> ';
            }
            html += '   </p>';
        }
        html += '   <p>Posted by <a class="author" href="/">' + image.author +'</a></p>'
        html += '   </p>'
        html += '</div>';
    }

    $('#pins').append(html);

    if (length == 0) isLastPage = true;
    applyLayout();
};

$(document).ready(new function() {
    $(document).bind('scroll', onScroll);
    loadData();
});

/**
 * On clicking an image show fancybox original.
 */
$('.fancybox').fancybox({
    openEffect: 'none',
    closeEffect: 'none'
});
