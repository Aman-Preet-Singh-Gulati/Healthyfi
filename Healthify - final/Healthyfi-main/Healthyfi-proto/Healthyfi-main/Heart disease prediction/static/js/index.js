$(window).on("load", function() {
    $("#loader").delay(2000).slideUp(1000);
});
$(document).ready(function() {
    $("#heartattack").click(function() {

        $("#search-bar").val("HEART ATTACK");

    })
    $("#breast-cancer").click(function() {

        $("#search-bar").val("BREAST CANCER");

    })
    $("#liver-disease").click(function() {

        $("#search-bar").val("LIVER DISEASE");

    })
    $("#kidney-disease").click(function() {

        $("#search-bar").val("KIDNEY DISEASE");

    })
    $("#diabetes").click(function() {

        $("#search-bar").val("DIABETES");

    })

    $("#search-bar").on("keyup", function() {
        var value = $(this).val();
        var disease = ["HEART ATTACK", "LIVER DISEASE", "BREAST CANCER", "KIDNEY DISEASE", "DIABETES", "HIV", "LUNGS CANCER", "DENGUE", "HERPES"];
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