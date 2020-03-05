//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
document.getElementById("myBtn").addEventListener ("click", function () {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
});

/*
document.getElementById("show-hide").addEventListener("click", function() {
    let test = document.getElementsByClassName("reply");
        if (test.style.display === "none") {
            test.style.display = "block";
        }
        else {
            test.style.display = "none";
        }
})
*/

function replyFunction(id) {
  let replySection = document.getElementById('replies-for-' + id);
  
  if (!replySection.style.display || replySection.style.display == 'none') {
    replySection.style.display = 'block';
  } else {
    replySection.style.display = 'none';
  }
}