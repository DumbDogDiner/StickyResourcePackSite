window.addEventListener('load', (event) => {
    onLoad();
});

function onLoad() {
    var something = document.getElementById('something');
    var x = false;
    var check = document.getElementById("test1");
    something.onmouseover = function () {
        if(check.checked) {
            this.style.backgroundColor = 'red';
        } else {
            this.style.backgroundColor = '#ff00ff'
        }
    };
    something.onmouseout = function () {
        //this.style.backgroundColor = '';
    };


    test1.onchange = function () {
        x = !x;
        console.log(x);
        something.onmouseover();
    }

    console.log("hello");
}