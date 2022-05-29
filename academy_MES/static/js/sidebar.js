// определяем как будет расположен сайдербар в зависимости от ширины экрана
positionSidebarDependingOnTheWidth()

// если ширина окна изменилась
window.addEventListener('resize', function (event) {
    positionSidebarDependingOnTheWidth()
}, true)

function positionSidebarDependingOnTheWidth() {
    if (document.documentElement.clientWidth < 960) {
        wrapper.insertBefore(aside, main)
    } else {
        main.insertBefore(aside, content)
    }
}
