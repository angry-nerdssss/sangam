document.querySelector(".navbar").classList.remove("navbar-light");
document.querySelector(".navbar").classList.add("navbar-dark");

function collapse2() {
    var scroll_y = this.scrollY;

    if (scroll_y < 100) {
        var bar = document.getElementsByClassName("navbar")[0];
        console.log("collapse2 called");
        bar.classList.toggle("transparent");
        bar.classList.toggle("bg-dark");
    }
}

window.addEventListener("scroll", function (event) {
    var scroll_y = this.scrollY;

    // console.log(scroll_y);
    bar = document.getElementsByClassName('navbar')[0];

    if (scroll_y > 100) {
        bar.classList.add('navbar-light');
        bar.classList.add('bg-light')
        bar.classList.remove('navbar-dark');
    } else {
        bar.classList.remove('navbar-light');
        bar.classList.remove('bg-light')
        bar.classList.add('navbar-dark');
    }
});