

window.addEventListener('load', function() {
    setTimeout(function() {
        document.getElementById('loadingScreen').style.display = 'none';
        

        setTimeout(function() {
            welcomeAlert.classList.remove('show');
            welcomeAlert.classList.add('hide');
        }, 1000); 

        
        setTimeout(function() {
            welcomeAlert.style.display = 'none';
        }, 3500);
    }, 800); 
});