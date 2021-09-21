$(window).on("load", function() {
    $("#loader").delay(2000).slideUp(1000);
});
$(document).ready(function() {

    $("#search-bar").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        var disease = ["heart attack", "liver disease", "breast cancer", "kidney disease", "diabetes", "hiv", "lungs cancer", "dengu", "herpes"];
        var temp = "";
        var len = value.length;
        if (len != 0) {
            $("#search-result").css({ "display": "table" });

            $("#results").empty();

            for (var i = 0; i < disease.length; i++) {

                temp = disease[i].substr(0, len);
                if (value === temp) {
                    $("#results").append("<tr><td><a style = 'text-decoration:none; color:white;' href='#'>" + disease[i] + "</a></tr></td>");
                }

            }
        } else {
            $("#search-result").css({ "display": "none" });
        }



        $("#results").on("click", "td", function() {
            var a = $(this).text();
            $("#search-bar").val(a);
        });

    });
    $("#btn").on("click", function() {
        $("#inner-block").load("index.html")
    })


});