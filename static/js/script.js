// Function for 'Back to top' button

mybutton = document.getElementById("myBtn");
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
document.getElementById("myBtn").addEventListener ("click", function () {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});

// Function for show/hide toggle and arrow direction change on replies

function replyFunction(childElement, id) {
  let replySection = document.getElementById("replies-for-" + id);
  
  if (!replySection.style.display || replySection.style.display == 'none') {
    replySection.style.display = 'block';
    childElement.innerHTML = '<strong>Show/hide replies <i class="fas fa-caret-up"></i></strong>';
  } else {
    replySection.style.display = 'none';
    childElement.innerHTML = '<strong>Show/hide replies <i class="fas fa-caret-down"></i></strong>';
  }  
}

// Function for show/hide toggle and arrow direction change on journey details

function detailsFunction(childElement, id) {
  let detailsSection = document.getElementById("details-for-" + id);
  
  if (!detailsSection.style.display || detailsSection.style.display == 'none') {
    detailsSection.style.display = 'block';
    childElement.innerHTML = '<strong>Show journey details <i class="fas fa-caret-up"></i></strong>';
  } else {
    detailsSection.style.display = 'none';
    childElement.innerHTML = '<strong>Show journey details <i class="fas fa-caret-down"></i></strong>';
  }
}