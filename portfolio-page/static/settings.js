$(document).ready(function(){
  $('div.content').load("/static/about.html");
  $('#navbutton-ABOUT').css('background-color','tomato');
  $(document).prop("title","about");

  /* load in json of the form {"TABNAME":["background-color","background-color"]}*/
  $.getJSON('/testroute', function(result){
    $("h3[name='navbutton-group']").click(function(){
        var selected = $(this).attr("id");
        var button_name = $(this).attr("id").split('-')[1];
        $(this).css("background-color",result[button_name][1]);
        $(document).prop("title",button_name.toLowerCase());
        $(this).parents("#button-group").siblings().children().children("h3").css('background-color','white');

        console.log($("div#about").offset());

      });
      $(window).scroll(function(){
        var section_offset = [$("div#about").offset().top, $("div#skills").offset().top, $("div#projects").offset().top];
        var current_screen = $(document).scrollTop();
        if (current_screen < section_offset[1] - 50){
          $("h3#navbutton-ABOUT").css("background-color",result["ABOUT"][1]);
          $("h3#navbutton-SKILLS").css("background-color","white");
          $("h3#navbutton-PROJECTS").css('background-color','white');
        } else if (current_screen >= section_offset[1] - 150 && current_screen < section_offset[2] - 50){
          $("h3#navbutton-SKILLS").css("background-color",result["SKILLS"][1]);
          $("h3#navbutton-PROJECTS").css('background-color','white');
          $("h3#navbutton-ABOUT").css('background-color','white');
        }else{
          $("h3#navbutton-PROJECTS").css("background-color",result["PROJECTS"][1]);
          $("h3#navbutton-SKILLS").css('background-color','white');
          $("h3#navbutton-ABOUT").css('background-color','white');
        }
      });
  });
});
