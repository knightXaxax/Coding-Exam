$(document).ready(function(){
    $('a.modal-btns').on({
        'click' : function() {
            color = $(this).attr('value').substring(2, $(this).attr('value').indexOf("id="));
            color_url = color.substring(color.indexOf("-") != -1 ? 1 : 0);
            url = String($('#img-focus').attr('src')+"static/images/"+color_url+".png")
            $('#img-focus').attr('src', url);
            $('#car-name').text($(this).attr('value').substring(0, 1));
            $('#hidden_box').attr('value', $(this).attr('value').substring($(this).attr('value').indexOf("id=") + 3));
            if (color_url == "red") {
                $('option.red').attr('selected', 'true');
            } else {
                $('option.blue').attr('selected', 'true');
            }
        },
    });

    $('#update_delete_modal').on('hidden.bs.modal', function (e) {
        $('#img-focus').attr('src', '/');
    });
});