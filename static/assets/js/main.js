$(function () {

var acc = document.getElementsByClassName("cart_expand");

for (var i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
        
            var up = this.getElementsByClassName('up');
            var down = this.getElementsByClassName('down');
        
            console.log(up);
            var panel = this.parentElement.nextElementSibling;
            console.log(panel);
        
            if (panel.style.display === "block") {
                panel.style.display = "none";
                up.style.display = "none";
                // down.style.display = "block";
            
            } else {
                panel.style.display = "block";
                // up.style.display = "block";
                // down.style.display = "none";
            }
        });
    }
});




