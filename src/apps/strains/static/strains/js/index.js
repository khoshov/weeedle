$(function () {
    const sliderRange = $("#slider-range");
    const amount = $("#amount");
    const thcMinInput = $("#thc-min");
    const thcMaxInput = $("#thc-max");
    const thcMinValue = thcMinInput.data('thc');
    const thcMaxValue = thcMaxInput.data('thc');
    sliderRange.slider({
        range: true,
        min: thcMinValue,
        max: thcMaxValue,
        values: [thcMinInput.val() || thcMinValue, thcMaxInput.val() || thcMaxValue],
        slide: function (event, ui) {
            amount.val(ui.values[0] + "% - " + ui.values[1] + "%");
            thcMinInput.val(ui.values[0]);
            thcMaxInput.val(ui.values[1]);
        }
    });
    amount.val(sliderRange.slider("values", 0) + "% - " + sliderRange.slider("values", 1) + "%");
    thcMinInput.val(sliderRange.slider("values", 0));
    thcMaxInput.val(sliderRange.slider("values", 1));
});