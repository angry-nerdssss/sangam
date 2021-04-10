window.addEventListener("scroll", function (event) {
    var scroll_y = this.scrollY;

    // console.log(scroll_y);
    bar = document.getElementsByClassName('navbar')[0];

    if (scroll_y > 100) {
        document.getElementsByClassName('navbar-brand')[0].style.fontSize = "2rem"
        bar.classList.add("sticky-top");
        bar.classList.add("shadow-lg")
    } else {
        document.getElementsByClassName('navbar-brand')[0].style.fontSize = "2.5rem"
        bar.classList.remove("shadow-lg")
        bar.classList.remove("sticky-top");
    }
});