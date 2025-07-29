document.addEventListener('DOMContentLoaded', function(){
  const elements = document.querySelectorAll('div>div>div');

  function runAnimation() {
    elements.forEach(function(element, id){
        element.style.position = 'relative';
        element.style.top = '-200px';
        element.style.opacity = '0';
        element.style.transition = 'all 1s ease';
        
        const wait = Math.floor((Math.random()*3000)+1);
        setTimeout(function(){
            element.style.top = '0px';
            element.style.opacity = '1';
        }, wait);
    });
  }

  runAnimation();

  setInterval(runAnimation, 5000);
});
