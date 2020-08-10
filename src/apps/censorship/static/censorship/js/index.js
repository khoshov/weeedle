$(document).ready(function () {
    const countrySelect = $('#id_country');
    const adultCheckbox = $('#id_adult');
    const submitButton = $('#submit-id-submit');

    const toggleSubmitButton = function(countrySelect, adultCheckbox) {
        const countryValue = countrySelect.val();
        const isAdult = adultCheckbox.is(":checked");
        const isRussia = countryValue === 'RU';
        const countrySelected = countryValue !== '';

        console.log(countryValue);
        console.log(isAdult);
        console.log(isRussia);
        console.log(countrySelected);

        if (isAdult && countrySelected && !isRussia) {
            submitButton.css({opacity: 1});
        } else {
            submitButton.css({opacity: 0});
        }
    }

    countrySelect.selectize({
        placeholder: 'Введите название вашей страны',
    });

    countrySelect.on('change', function () {
        toggleSubmitButton(countrySelect, adultCheckbox);
    });

    adultCheckbox.on('change', function () {
        toggleSubmitButton(countrySelect, adultCheckbox);
    });
});
