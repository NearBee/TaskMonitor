document.addEventListener('DOMContentLoaded', function () {

    var inputBoxes = document.querySelectorAll('.mb-3 input.forminputBox');
    var mb3Username = document.querySelector('.mb-3.username');

    if (inputBoxes) {
        inputBoxes.forEach(function (inputBox) {

            // adding the activeBox class to (currently) the username box when the box is active
            inputBox.addEventListener('click', function () {
                var parentBox = inputBox.closest('.mb-3');
                if (parentBox) {
                    parentBox.classList.add('activeBox');
                }
            });

            // removing the activeBox class to (currently) the username box when the box is inactive
            inputBox.addEventListener('blur', function () {
                var parentBox = inputBox.closest('.mb-3');
                if (parentBox) {
                    parentBox.classList.remove('activeBox');
                }
            });
        });
    }

});