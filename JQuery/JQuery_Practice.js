$(function() {
    $("#show").hide();
    $("#secret").hide();
    $("#hold").hide();
    $("#fade").hide();
    $("#hiddenMessage").hide();
    
    // 1
    $("#hide").click(function() {
        $(".clickHide").hide();
        $("#hide").hide();
        $("#show").show();
    });

    $("#show").click(function() {
        $(".clickHide").show();
        $("#hide").show();
        $("#show").hide();
    });

    // 2
    $(".doubleClickHide").click(function() {
        $(this).hide();
    });

    $("#doubleClick").dblclick(function() {
        $(".doubleClickHide").show();
    });

    // 3
    $("#hover").mouseenter(function() {
        $("#secret").show();
    });

    $("#hover").mouseleave(function() {
        $("#secret").hide();
    });

    // or you can use hover()
    /*
    $("#hover").hover(function() {
        $("#secret").show();
    }, function() {
        $("#secret").hide();
    });
    */

    // 4
    $("#click").mousedown(function() {
        $("#hold").show();
    });

    $("#click").mouseup(function() {
        $("#hold").hide();
    });

    // 5
    $(".highlight").focus(function() {
        $(this).css("background-color", "yellow")
    });

    $(".highlight").blur(function() {
        $(this).css("background-color", "white")
    });

    // you can attach multiple event handlers to an element
    /*
    $("p").on({
        click: function() {

        }, dblclick: function() {

        }, hover: function() {

        }
    });
    */

    // 6
    $("#block").click(function() {
        $("#fade").fadeToggle();
    });

    // fadeIn and fadeOut (self explanatory), fadeTo (specify an opacity between 0 and 1)
    /*
    $("p").fadeTo("slow", 0.15);
    */
    // or instead of fade, there's slide (slideDown, slideUp, slideToggle)

    // 7
    // to 'animate' an element, it must have css to define its original state
    $("#square").click(function() {
        $("#square").animate({
            opacity: "0.5",
            height: "150px",
            width: "150px"
        });
    });

    $("#resetSquare").click(function() {
        $("#square").animate({
            opacity: "1",
            height: "100px",
            width: "100px"
        })
    })

    $("#grow").click(function() {
        $("#circle").animate({
            height: "+=50px",
            width: "+=50px"
        });
    });

    $("#shrink").click(function() {
        $("#circle").animate({
            height: "-=50px",
            width: "-=50px"
        });
    });

    // animations can be stacked
    /*
    $("#shrink").click(function() {
        var triangle = $("triangle");
        triangle.animate({
            
        });
        triangle.animate({
            
        });
        triangle.animate({
            
        });
    });
    */
    // animations can also be stopped before they've finished using stop()

    // 8
    $("#hideSquare").click(function () {
        $("#squareHide").hide(function () {
            $("#hiddenMessage").show();
        });
    });

    // chaining
    // chaining allows you to run multiple JQuery commands one after another
    /*
    $("p").slideUp().slideDown().css("color", "blue");
    */

    // 9
    $("#getText").click(function() {
        $("#showInformation").text($("#richParagraph").text());
    });

    $("#getHtml").click(function() {
        $("#showInformation").text($("#richParagraph").html());
    });

    $("#getAttributes").click(function() {
        $("#showAttributes").text("Value: '" + $("#richInput").val() + "', another value: '" + $("#richInput").attr("anothervalue") + "'");
    });

    // 10
    $("#append").click(function() {
        $("#showInput").append(" " + $("#inputAdd").val());
    });

    $("#prepend").click(function() {
        $("#showInput").prepend($("#inputAdd").val() + " ");
    });

    // after() and before() are used to append and prepend elements

    // 11
    $("#emptySelect").click(function() {
        $("#select").empty();
    });

    $("#deleteSelect").click(function() {
        $("#select").remove();
    });

    // you can filter which elements to remove
    /*
    $("#removeCountry").click(function() {
        $("#countries").remove(".Europe");
    });
    */

    // continue from https://www.w3schools.com/jquERy/jquery_css_classes.asp
});