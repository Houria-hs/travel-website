

let icon = document.getElementById('light');

icon.onclick = function(){
    document.body.classList.toggle('dark-mode');
    if(document.body.classList.contains('dark-mode')){
        icon.classList.remove('fa-moon')
        icon.classList.add('fa-sun')
        icon.style.color = '#fff';
    }
    else{
        icon.classList.remove('fa-sun')
        icon.classList.add('fa-moon')
        icon.style.color = '#000';
    }
}
