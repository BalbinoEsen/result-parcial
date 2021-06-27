function cityIdOnChange() {
    var cityId = document.getElementById("cityid").value;
    var cityLink = document.getElementById("cityLink");
    cityLink.href = "/dashboard/city/" + cityId;
}

function countryCityIdOnChange() {
    var countryCityId = document.getElementById("countrycityid").value;
    var countryLink = document.getElementById("countryLink");
    countryLink.href = "/dashboard/country/" + countryCityId;

}
