$(function () {

var acc = document.getElementsByClassName("cart_expand");

for (var i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function(e) {
            e.stopImmediatePropagation();

            var up = this.getElementsByClassName('up')[0];
            var down = this.getElementsByClassName('down')[0];

            var panel = this.parentElement.nextElementSibling;
          
            if (panel.classList.contains('open')) {
               console.log(up);
               panel.classList.remove('open');
               panel.classList.add('close');
            
               down.classList.remove('open');
               down.classList.add('close');
               
               up.classList.add('open');

            } 
            else{
                console.log(down);
                panel.classList.add('open');
                panel.classList.remove('close');

                down.classList.add('open');
                down.classList.remove('close')

                up.classList.remove('open');
                up.classList.add('close');
            }
        })
    }
   
});




