function cityIdOnChange() {
    var cityId = document.getElementById("cityid").value;
    var cityLink = document.getElementById("cityLink");
    cityLink.href = "/dashboard/city/" + cityId;
}