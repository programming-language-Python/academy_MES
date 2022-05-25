window.addEventListener('resize', function (event) {
    if (document.documentElement.clientWidth < 960) {
        wrapper.insertBefore(aside, main)
    } else {
        main.insertBefore(aside, content)
    }
}, true)