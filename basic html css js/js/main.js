const categoryTimeframeContainer = document.getElementById('cat-tim-container');
const categoryContainer = document.getElementById('category-container');
const categoryTitleContainer = document.getElementById('category-title-container');
const timeframeContainer = document.getElementById('timeframe-container');
const timeframeTitleContainer = document.getElementById('timeframe-title-container');

categoryTitleContainer.addEventListener('click', function() {
    // If cat-tim-container is hidden -> show
    if (categoryTimeframeContainer.className === 'hide-container') {
        categoryTimeframeContainer.className = 'show-container';
        // Make the z-index of categoryContainer high and timeframe normal
        categoryContainer.className = 'inner-container top';
        timeframeContainer.className = 'inner-container';
    } else {
        categoryTimeframeContainer.className = 'hide-container';
    }
});

timeframeTitleContainer.addEventListener('click', function() {
    // If cat-tim-container is hidden -> show
    if (categoryTimeframeContainer.className === 'hide-container') {
        categoryTimeframeContainer.className = 'show-container';
        // Make the z-index of categoryContainer high and category normal
        categoryContainer.className = 'inner-container';
        timeframeContainer.className = 'inner-container top';
    } else {
        categoryTimeframeContainer.className = 'hide-container';
    }
});