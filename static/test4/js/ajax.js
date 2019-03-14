$(document).ready(function(){
    document.getElementById('btn').onclick =
    function(){
        $.ajax({
            type:"get",
            url: '/test4/studentsinfo/',
            dataType: 'json',
            success: function (data, status){
                console.log(data)
            }
        })
     }
})
