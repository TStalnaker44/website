function toggleNavigation() {
    const nav = document.querySelector('nav');
    const top = document.querySelector(".top-bar");
    if (nav.style.display === 'block') {
        nav.style.display = 'none';
        top.style.display = 'block';
    } else {
        nav.style.display = 'block';
        top.style.display = 'none';
    }
}