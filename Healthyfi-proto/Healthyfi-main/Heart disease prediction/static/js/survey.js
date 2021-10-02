$(window).on("load", function() {
    $("#loader").delay(2000).slideUp(1000);
});
$(document).ready(function() {
    var disease = $("#holder").children("h1").text();
    $("#disease-name").val(disease);
    if (disease === "HEART ATTACK") {
        $("#img-disease").attr("src", "/static/css/images/heartattack.png");
        var intro = `A blockage of blood flow to the heart muscle.
        A heart attack is a medical emergency. A heart attack usually occurs when a blood clot blocks blood flow to the heart. Without blood, tissue loses oxygen and dies.
        Symptoms include tightness or pain in the chest, neck, back or arms, as well as fatigue, lightheadedness, abnormal heartbeat and anxiety. Women are more likely to have atypical symptoms than men.
        Treatment ranges from lifestyle changes and cardiac rehabilitation to medication, stents and bypass surgery.`
        $("#intro").text(intro);
    } else if (disease === "KIDNEY DISEASE") {
        $("#img-disease").attr("src", "/static/css/images/kidney2.png");
        var intro = `Longstanding disease of the kidneys leading to renal failure.
        The kidneys filter waste and excess fluid from the blood. As kidneys fail, waste builds up.
        Symptoms develop slowly and aren't specific to the disease. Some people have no symptoms at all and are diagnosed by a lab test.
        Medication helps manage symptoms. In later stages, filtering the blood with a machine (dialysis) or a transplant may be required.`
        $("#intro").text(intro);
    } else if (disease === "LIVER DISEASE") {
        $("#img-disease").attr("src", "/static/css/images/liver.png");
        var intro = `Liver disease is any disturbance of liver function that causes illness. The liver is responsible for many critical functions within the body and should it become diseased or injured, the loss of those functions can cause significant damage to the body. Liver disease is also referred to as hepatic disease.`
        $("#intro").text(intro);
    } else if (disease === "BREAST CANCER") {
        $("#img-disease").attr("src", "/static/css/images/breast.png");
        var intro = `A cancer that forms in the cells of the breasts.
        Breast cancer can occur in women and rarely in men.
        Symptoms of breast cancer include a lump in the breast, bloody discharge from the nipple and changes in the shape or texture of the nipple or breast.
        Its treatment depends on the stage of cancer. It may consist of chemotherapy, radiation, hormone therapy and surgery.`
        $("#intro").text(intro);

    } else if (disease === "DIABETES") {
        $("#img-disease").attr("src", "/static/css/images/diabetes.png");
        var intro = `Diabetes mellitus, commonly known as diabetes, is a metabolic disease that causes high blood sugar. The hormone insulin moves sugar from the blood into your cells to be stored or used for energy. With diabetes, your body either doesn’t make enough insulin or can’t effectively use the insulin it does make.

        Untreated high blood sugar from diabetes can damage your nerves, eyes, kidneys, and other organs.`
        $("#intro").text(intro);
    }

});