// если нажата кнопка "Поиск"
search.addEventListener('click', () => {
    // Формируем ссылку для поиска в яндекс
    let url = 'https://yandex.ru/search/?text=' + textSearch.value
    // Открываем ссылку в новой вкладке
    // _blank - открытие в новой вкладке
    window.open(url, '_blank');
})