/**
 * Created by linhebin on 2015/11/12.
 */
$(function(){
    var view = $("#jquery_value").text();
    if(view == 1) {
        $('#addModalOne').modal({'backdrop':false});
        $('[name="inputType"]').append('<option value="MIOSD">MIOSD</option><option value="MIOSD_TS">MIOSD_TS</option>');
    }
    //添加页面关闭按钮
    $("button[data-dismiss=modal]").click(function(){window.location.href="index.php";});
    //音频Track
    var audioTrack = $('#addForm').find('select[name=audioTrack]');
    //节目编号
    var tsdemuxProgram = $('#addForm').find('select[name=tsdemuxProgram]');
    tsdemuxProgram.click(function(){
        var val = $(this).val();
        var str_audio = $(this).find("option[value='"+val+"']").attr("audiotrack");
        var arr_audio = str_audio.split("_");
        if(str_audio)
        {
            var tmp= programToAudio(arr_audio,0,arr_audio.length-1);
            audioTrack.html(tmp);
        }

    });

    //输入类型BL4K/BLHD的特殊情况
    var inputType_BL = $('#addForm').find('select[name=inputType]');
    inputType_BL.click(function(){
        var val = $(this).val();
        if(val == 'BL4K' || val == 'BLHD'){
            $('#addForm').find('div.inputSrc_text').addClass('hide');
            $('#addForm').find('div.inputSrc_select').removeClass('hide');
            $('#addForm').find('input[name=inputSrc]').attr("value","1_1");
        }else{
            $('#addForm').find('div.inputSrc_text').removeClass('hide');
            $('#addForm').find('div.inputSrc_select').addClass('hide');
            $('#addForm').find('input[name=inputSrc]').attr("value","238.1.1.1:10001");
        }
    });
    $('#addForm').find('div.inputSrc_select').find('select').click(function(){
        var inputSrc_videoindex = $('#addForm').find('select[name=inputSrc_videoindex]').val();
        var inputSrc_audioindex = $('#addForm').find('select[name=inputSrc_audioindex]').val();
        $('#addForm').find('input[name=inputSrc]').attr("value",inputSrc_videoindex+"_"+inputSrc_audioindex);
    });
    //编码器类型nvh264的特殊情况
    encodeVtypeNvh264();

    //检测流内容
    $('#detect-stream').click(function(){
        $(this).text('请稍等...');

        $('select[name=tsdemuxProgram]').removeAttr("disabled");
        $('select[name=audioTrack]').removeAttr("disabled");
        //输出流1
        var channelName = $('#addForm').find('input.outputSrc').val();
        //输入流
        var groupBroadCast = $('#addForm').find('input[name=inputSrc]').val();
        //输入类型
        var protocolType=$('select[name=inputType]').val();


        var temp = channelName.split('/');
        channelName = temp[temp.length-1];
        if(!channelName){
            alert('频道名称不能为空');
            return false;
        }
        $.post('server.php',{target:'splitStream',channel_name:channelName,gIp:groupBroadCast,pt:protocolType},function(data){
            $('#detect-stream').text('检测流内容');
            console.log(data);
            if(data != '' && data != null )
            {
                var tsdemuxProgramList = [];
                var audioTrackList = [];
                var audio_str = '';
                var temp = '';
                var flag = false;
                data=  $.parseJSON(data);
                for(var i in data)
                {
                    if(data[1] != "_"){
                        temp = data[i].split('_');
                    }else{
                        temp = data.split('_');
                        flag = true;
                    }
                    console.info(temp);
                    var len = temp.length-1;
                    audio_str = temp[2];
                    for(var k =3;k<=len;k++) {
                        if(temp[k]){
                            audio_str += '_'+temp[k];
                        }
                    }
                    tsdemuxProgramList[temp[1]] = temp[0]+'|'+audio_str;
                    audio_str = '';
                    //把第一个节目编号的音频回填到音频Track
                    if(i == 0){
                        var html = programToAudio(temp,2,len);
                        audioTrack.html(html);
                    }
                    if(flag){
                        break;
                    }
                }
                console.info(tsdemuxProgramList);
                //把节目编号回填
                var programList_html = '';
                for(var name in tsdemuxProgramList)
                {
                    var tmp = tsdemuxProgramList[name].split('|');
                    programList_html += '<option value="'+tmp[0]+'" audioTrack="'+tmp[1]+'">'+name+'</option>';
                }

                if(programList_html=='')
                {
                    programList_html += '<option value="0" audioTrack="">0</option>';
                }

                tsdemuxProgram.html(programList_html);
            }else{
                alert("channel文件错误:"+data);
            }
        });
    });
    //添加页面
    $('#add').click(function(){
        // 拆分流默认值
        audioTrack.html('<option value="0">0</option>');
        tsdemuxProgram.html('<option value="0">0</option>');
        if($('.add-title').text() == '修改操作'){
            alert('载入数据失败,请再次点击添加按钮')
            window.location.href="index.php";
        }else{
            $('#addModal').modal({'backdrop':false})
        }
    });
    //添加页面提交
    $('#addSubmit').click(function(){
        var tsdemuxProgramText = $("select[name=tsdemuxProgram] option:selected").text();
        $('#addForm').append('<input type="hidden" name="tsdemuxProgramText" value="'+tsdemuxProgramText+'" />');
        if(!validation()){
            return false;
        }
        var $data = $('#addForm').serialize();

        $.post('server.php',$data,function(data){
            var status = data.status;
            if(status !='success'){
                //if(window.confirm(status)){
                //    $.post('server.php?confirm=1',$data,function(data){
                //        window.location.href="index.php"
                //    });
                //}else{
                //    return false;
                //}
                alert(status);
            }else{
                alert('恭喜你，添加成功');
                window.location.href="index.php"
            }
        },'json')
    });
    //基本信息页面的刷新
    $('.refresh').click(function(){
        var channel_name = $('#baseInfo').text();
        $('#showModal').modal('hide')
        show(channel_name);
    });
    //全部预览
    $('.seeAll').click(function(){
        var output = {};
        var num =0;
        $('.main-table').find('.runbutton').each(function(i,event){
            //console.log($(this));
            if($(this).text() == '正在编码'){
                var src = $(this).attr('data');
                var one_srcs = src.split('<br />');
                $.each(one_srcs,function(key,item){
                    var type = item.substr(0,4);
                    if(type == 'rtmp'){
                        output[num] = item;
                        num++;
                    }
                });
            }
        });
        if(!output[0]){
            alert("输出流中没有rtmp类型！！");
        }
        seeAll(output);
    });
    //新增输出流
    $('#add-div-output').click(function(){
        //关闭所有的展开
        var items = $('#addForm').find(".opne-and-close");
        $.each(items,function(key,item){
            var name = $(item).text();
            if( name == "收缩"){
                openAndClose(item);
            }
        });
        addOutputDiv();
        //所有的checkbox下的区域要隐藏
        var checks = $('.add-one-div-output').find("input[type=checkbox]");
        $.each(checks,function(key,item){
            checkboxOpen(item);
        });
    });
    //全部启动
    $('#runAll').click(function(){
        if( confirm('确定要全部启动？')){
            var run_data = '',need_run = true;
            $('input[name=checkbox]').each(function (){
                if( $(this).prop('checked') ){
                    var channel_name = $(this).attr('data');
                    var status = $('.run-button-'+channel_name).text();
                    if(status == '正在编码'){
                        alert(channel_name+'正在编码，不能启动');
                        need_run = false;
                        return false;
                    }
                    run_data += channel_name+';';
                }

            });
            if(!need_run){
                return false;
            }
            if(!run_data.length){
                alert('没有选中任何频道!');
                return false;
            }else{
                runAll(run_data);
            }
        }
    });


});

//将节目编号的音频回填到音频Track
function programToAudio(temp,start,lenght){
    var audio_track_html = '';
    for(var j=start;j<=lenght;j++)
    {
        var option = "";
        if(isNaN(temp[j+1])){
            if(temp[j+1]){
                option = temp[j]+"_"+temp[j+1];
                j = j+1;
            }else{
                if(!isNaN(temp[j])){
                    option = temp[j];
                }
            }
            audio_track_html += '<option value="'+temp[j]+'">'+option+'</option>';
        }else{
            if(!isNaN(temp[j])){
                audio_track_html += '<option value="'+temp[j]+'">'+temp[j]+'</option>';
            }
        }
    }
    return audio_track_html;
}


//新增输出流区
function addOutputDiv(){
    var num = $('#addForm').find('input.outputSrc').length+1;
    var html_str = '';
    html_str += '<div class="add-one-div-output">';
    html_str += '<div style="padding-bottom: 20px"><button type="button" class="close add-one-colse">×</button></div>';
    html_str += '<div id="output-hand" style="background-color: #cccccc">';
    html_str += '<div class="form-group width36">';
    html_str += '<label class="col-sm-4 control-label">输出类型'+num+'<i class="red">*</i></label>';
    html_str += '<div class="col-sm-5">';
    html_str += '<select class="form-control" name="outputType[]">';
    html_str += '<option value="rtmp">rtmp</option>';
    html_str += '<option value="udp">udp</option>';
    html_str += '<option value="record">record</option>';
    html_str += '<option value="http">http</option>';
    html_str += '</select>';
    html_str += '</div>';
    html_str += '</div>';
    html_str += '<div class="form-group width60">';
    html_str += '<label class="col-sm-3 control-label">输出流'+num+'<i class="red">*</i></label>';
    html_str += '<div class="col-sm-8">';
    html_str += '<input type="text" name="outputSrc[]" class="outputSrc form-control" value="rtmp://10.121.33.36/live/test" />';
    html_str += '</div>';
    html_str += '<div class="col-sm-1">';
    html_str += '<button type="button" id="btn-open" class="btn btn-primary opne-and-close" onclick="openAndClose(this)">收缩</button>';
    html_str += '</div>';
    html_str += '</div>';
    html_str += '</div>';
    var more_output = $("#div-output").html();
    html_str += '<div id="div-output">';
    html_str += more_output;
    html_str += '</div>';
    html_str += '</div>';
    $('#addForm').find("#more-div-output").append(html_str);
    //新增输出流区域的删除
    $('#addForm').find(".add-one-colse").click(function(){
        $(this).parents('.add-one-div-output').remove();
    });
    //编码器类型nvh264的特殊情况
    encodeVtypeNvh264();
}

//编码器类型nvh264的特殊情况
function encodeVtypeNvh264(){
    $('#addForm').find('select[name=encodeVtype\\[\\]]').click(function(){
        if( $(this).val() == 'nvh264'){
            $(this).parents(".form-group").next('div').removeClass('hide');
        }else{
            $(this).parents(".form-group").next('div').addClass('hide');
        }
    });
}

//输出流区域的展开收缩
function openAndClose(obj){
    var str = $(obj).text();
    $(obj).parents("#output-hand").next("#div-output").slideToggle();
    if( str == "展开"){
        $(obj).text("收缩");
        $(obj).removeClass("active");
    }else{
        $(obj).text("展开");
        $(obj).addClass("active");
    }
}

//输出流区域checkbox的展开收缩
function checkboxOpen(obj){
    var name = $(obj).attr("name");
    var num = name.length-2;
    name = name.substring(0,num);
    if( $(obj).prop('checked') ){
        $(obj).parents(".form-group").next('#'+name).removeClass('hide');
        $(obj).parents(".form-group").find("input[type=hidden]").attr("value",1);
    }else{
        $(obj).parents(".form-group").next('#'+name).addClass('hide');
        $(obj).parents(".form-group").find("input[type=hidden]").attr("value",0);
    }
}

//验证
function validation(){
    var res = true;
    var meg = '';
    if(!$('#addForm').find('input[name=name]').val()){
        alert('频道名称不能为空');
        return false;
    }
    if(!$('#addForm').find('input[name=inputSrc]').val()){
        alert('输入流不能为空');
        return false;
    }
    var outputSrc = $('#addForm').find('input[name=outputSrc\\[\\]]');
    $.each(outputSrc, function(i,item){
        if(!$(item).val()){
            meg ='输出流不能为空';
            res = false;
        }
    });
    if(!res){
        alert(meg);
        return res;
    }
    var ranges = [
        ['audioAmplify','0','300','音频增益'],
        ['image_denoisefactor','0','100','降噪'],
        ['image_detailfactor','0','100','增强'],
        ['image_contrast','0.0','10.0','对比度'],
        ['image_brightness','-100.0','100.0','亮度'],
        ['image_saturation','0.0','10.0','饱和度'],
        ['image_hue','-180.0','180.0','色度']
    ];
    $.each(ranges,function(k,arr){
        res = validation_range(arr[0],arr[1],arr[2],arr[3]);
        if(!res){
            return res;
        }
    });
    return res;
}

//多验证范围
function validation_range(name,min,max,meg){
    var res = true;
    var megs = '';
    var names = $('#addForm').find('input[name='+name+'\\[\\]]');
    $.each(names, function(i,item){
        if($(item).val()){
            var val = Number($(item).val());
            if(val<min || val>max ){
                megs = meg+'不在范围';
                res = false;
            }
        }
    });
    if(!res){
        alert(megs);
    }
    return res;
}

function stopAll(data){
    $.post('server.php',{'data':data,'target':'stopAll'},function(data){
        var status = data.status;
        if(status !='success'){
            alert(status);
        }else{
            alert('操作成功!');
            window.location.href="index.php";
        }
    },'json')
}
function runAll(data){
    $.post('server.php',{'data':data,'target':'runAll'},function(data){
        var status = data.status;
        if(status !='success'){
            alert(status);
        }else{
            alert('恭喜你，操作成功！');
            window.location.href="index.php";
        }
    },'json')
}
function seeAll(output){
    $('.seeAllModalBody').empty();
    for (index in output){
        var src = output[index],
            pos = src.lastIndexOf('/')+1,
            url = src.substring(0,pos),
            param = src.substring(pos),
            vars = 'address=' + url + '&stream='+param,
            html = '<embed style="margin-left:10px;margin-right:10px;width:31%;height:350px;vertical-align:top;margin-bottom:20px;" src="liveplayer.swf" quality="high" align="middle" allowscriptaccess="always" allowfullscreen="true" mode="transparent" flashvars="'+vars+'" type="application/x-shockwave-flash" name="xl_player" id="xl_player" autostart="true"></embed>';
        $('.seeAllModalBody').append(html);
    }
    $('#seeAllModal').modal({'backdrop':false});
}
function see(src){
    /*$.getScript( "http://jwpsrv.com/library/eo+GsmlQEeOwDyIACi0I_Q.js",function(){
     jwplayer('playerQwmndhnInhDB').setup({
     file: src,
     image: '/tool/logo.jpg',
     title: '点击观看',
     width: '100%',
     aspectratio: '16:9',
     fallback: 'false',
     autostart: 'true',
     primary: 'flash'
     });*/
    var outputs = src.split('<br />');
    var has_see = false;
    $.each(outputs,function(i,item){
        var type = item.substr(0,4);
        if(type == 'rtmp'){
            var pos = item.lastIndexOf('/')+1,
                url = item.substring(0,pos),
                param = item.substring(pos),
                vars = 'address=' + url + '&stream='+param;
            $('#xl_player').attr('flashvars',vars);
            $('#seeModal').modal({'backdrop':false});
            has_see = true;
            return false;
        }
    });
    if(!has_see){
        alert("输出流中没有rtmp类型！！");
    }
}
function run(channel_name){
    $('.run-button-'+channel_name).prop("onclick",null);
    $.post('server.php',{'channel_name':channel_name,'target':'run'},function(data){
        var status = data.status;
        if(status !='success'){
            alert(status);
        }else{
            alert('恭喜你，启动成功！');
            setTimeout(function(){
                window.location.href="index.php"
            },3000);
        }
    },'json')
}
function stop(channel_name){
    if( confirm('确认要停止'+channel_name+"吗?")){
        $('.stop-button-'+channel_name).prop("onclick",null);
        $.post('server.php',{'channel_name':channel_name,'target':'stop'},function(data){
            var status = data.status;
            if(status !='success'){
                alert(status);
            }else{
                alert('恭喜你，停止成功！');
                window.location.href="index.php"
            }
        },'json')
    }
}
function show(channel_name){
    $.post('server.php',{'channel_name':channel_name,'target':'show'},function(data){
        var status = data.status;
        if(status !='success'){
            alert(status);
        }else{
            var input = data.input,output = data.output,stat = data.stat;
            $('#inPutTable').html(input);
            $('#outPutTable').html(output);
            $('#statTable').html(stat)
            var baseInfo = $('#baseInfo').text();
            if(baseInfo.indexOf(channel_name)<0){
                $('#baseInfo').text(channel_name)
            }
            $('#showModal').modal();
        }
    },'json')
}
function showDetail(channel_name){
    $.post('server.php',{'channel_name':channel_name,'target':'showDetail'},function(data){
        var status = data.status;
        if(status != 'success'){
            alert(status);
        }else{
            var input = data.input,output = data.output,video = data.video,audio=data.audio;
            var encode = data.encode,
                ts = data.ts,logo = data.logo,delogo = data.delogo;
            $('#showInPutTable').html(input);
            $('#showOutPutTable').html(output);
            $('#showVideoTable').html(video);
            $('#showAudioTable').html(audio);
            $('#showEncodeTable').html(encode);
            $('#showTsTable').html(ts);
            $('#showLogoTable').html(logo);
            $('#showDelogoTable').html(delogo);
            var baseInfo = $('#showBaseInfo').text();
            if(baseInfo.indexOf(channel_name)<0){
                $('#showBaseInfo').text(channel_name)
            }
            $('#showDetailModal').modal();
        }
    },'json')
}
function edit(channel_name,number){

    if($(".run-button-"+channel_name).text()=='正在编码')
    {
        $('#detect-stream').addClass("disabled");
    }
    else
    {
        $('#detect-stream').removeClass("disabled");
    }
    for($i=1;$i<number;$i++){
        addOutputDiv();
    }
    //回填text数据
    $('#addForm').find('input[type=text]').each(function(event){
        var $class = $(this).attr('name');
        if($class.lastIndexOf('[') > 0){
            var num = $class.length-2;
            $class = $class.substring(0,num);
        }
        var items = $('i.'+channel_name+'-'+$class);
        var $value = new Array();
        if(items.length >1){
            $.each(items,function(key,item){
                $value[key] = $(item).text();
            });
            var inputs = $('#addForm').find('input[name='+$class+'\\[\\]]');
            $.each(inputs,function(i,input){
                if(this == input){
                    $(this).attr('value',$value[i]);
                }
            });
        }else{
            $(this).attr('value',items.text());
        }
    });
    //回填select数据
    $('#addForm').find('select').each(function(event){
        var $class = $(this).attr('name');
        if($class.lastIndexOf('[') > 0){
            var num = $class.length-2;
            $class = $class.substring(0,num);
        }
        var items = $('i.'+channel_name+'-'+$class);
        var $value = new Array();

        if(items.length >1){
            $.each(items,function(key,item){
                $value[key] = $(item).text();
            });
            if($class=='audioTrack')
            {
                $('#addForm').find('select[name=audioTrack]').html('<option value="'+$value[0]+'">'+$value[0]+'</option>');
            }
            if($class == 'encodeVtype') {
                var encodeGPU = $('#addForm').find('.encodeGPU');
                $.each(encodeGPU, function (i, val) {
                    if ($value[i] == 'nvh264') {
                        $(this).removeClass("hide");
                    }
                });
            }
            var selects = $('#addForm').find('select[name='+$class+'\\[\\]]');
            $.each(selects,function(i,select){
                if(this == select){
                    $(this).find("option[value='"+$value[i]+"']").attr("selected","selected");
                }
            });
        }else{
            if($class=='tsdemuxProgram')
            {
                var tpt = $('i.'+channel_name+'-tsdemuxProgramText').text();
                $('#addForm').find('select[name=tsdemuxProgram]').html('<option value="'+items.text()+'">'+tpt+'</option>');
            }
            if($class=='audioTrack')
            {
                $('#addForm').find('select[name=audioTrack]').html('<option value="'+items.text()+'">'+items.text()+'</option>');
            }
            if($class == 'encodeVtype' && items.text() == 'nvh264' ) {
                $('#addForm').find('.encodeGPU').removeClass("hide");
            }
            $(this).find("option[value='"+items.text()+"']").attr("selected","selected");
        }
    });
    //回填checkbox数据
    $('#addForm').find('input[type=checkbox]').each(function(event){
        var $class = $(this).attr('name');
        if($class.lastIndexOf('[') > 0){
            var num = $class.length-2;
            $class = $class.substring(0,num);
        }
        var items = $('i.'+channel_name+'-'+$class);
        var $value = new Array();
        if(items.length >1){
            $.each(items,function(key,item){
                $value[key] = $(item).text();
            });
            var checkboxs = $('#addForm').find('input[name='+$class+'\\[\\]]');
            $.each(checkboxs,function(i,checkbox){
                if(this == checkbox){
                    if($value[i]==1){
                        $(this).attr('checked',true);
                        $(this).parents(".form-group").next('#'+$class).removeClass('hide');
                        $(this).parents(".form-group").find("input[type=hidden]").attr("value",1);
                    }
                }
            });
        }else{
            if(items.text()==1){
                if( $class == 'rateEnable'){
                    $(this).attr('value',1).attr('checked',true);
                }else{
                    $(this).attr('checked',true);
                    $('#'+$class+'W\\[\\]').attr('value',1);
                    $('#'+$class).removeClass('hide');
                }
            }
        }
    });
    //输入类型BL4K/BLHD的特殊情况
    if($('i.'+channel_name+'-inputType').text() == 'BL4K' || $('i.'+channel_name+'-inputType').text() == 'BLHD'){
        $('#addForm').find('div.inputSrc_text').addClass('hide');
        $('#addForm').find('div.inputSrc_select').removeClass('hide');
    }else{
        $('#addForm').find('div.inputSrc_text').removeClass('hide');
        $('#addForm').find('div.inputSrc_select').addClass('hide');
    }
    $('.add-title').html('修改操作');
    $('input[name=target]').attr('value','update');
    $('#addForm').append('<input type="hidden" name="channel_name" value="'+channel_name+'">');
    //var updateOutPut = $('input[name=outputSrc]').val();
    //$('#addForm').append('<input type="hidden" name="validOut" value="'+updateOutPut+'" />');
    if($(".run-button-"+channel_name).text()=='正在编码')
    {
        $('.footer_submit').html('<button type="button" class="btn btn-default" data-dismiss="modal">关闭</button><button type="button" onclick="update();" class="btn btn-primary disabled">提交</button>')

    }
    else
    {
        $('.footer_submit').html('<button type="button" class="btn btn-default" data-dismiss="modal">关闭</button><button type="button" onclick="update();" class="btn btn-primary">提交</button>')
    }
    //添加页面关闭按钮
    $("button[data-dismiss=modal]").click(function(){window.location.href="index.php";});
    $('#addModal').modal({'backdrop':false});
}
function delet(channel_name,name){
    var status = $('.run-button-'+channel_name).text();
    if(status == '正在编码'){
        alert('频道 '+name+' 正在编码，不能删除数据！');
        return ;
    }
    if( confirm('确认要删除 '+name+" 吗?")){
        $.post('server.php?confirm=1',{'channel_name':channel_name,'target':'delete'},function(data){
            var status = data.status;
            if(status !='success'){
                alert(status);
            }else{
                alert('恭喜你，删除成功！');
                window.location.href="index.php"
            }
        },'json')
    }
}
function update(){

    if( $('input[name=outputSrc]').val() == $('input[name=validOut]').val() ){
        $('#addForm').append('<input type="hidden" name="isValidOut" value="1" />');
    }
    var tsdemuxProgramText = $("select[name=tsdemuxProgram] option:selected").text();
    $('#addForm').append('<input type="hidden" name="tsdemuxProgramText" value="'+tsdemuxProgramText+'" />');

    if(!validation()){
        return false;
    }
    var $data = $('#addForm').serialize();
    $.post('server.php',$data,function(data){
        var status = data.status;
        if(status !='success'){
            //if(window.confirm(status)){
            //    $.post('server.php?confirm=1',$data,function(data){
            //
            //    });
            //    window.location.href="index.php"
            //}else{
            //    return false;
            //}
            alert(status);
        }else{

            alert('恭喜你，更新成功');
            //setTimeout(function(){
            window.location.href="index.php";
            //},3000);
        }
    },'json')
}