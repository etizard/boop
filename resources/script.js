var userid = "0";

$(".mainBtn").click(
  function(e){
    var mainBtn = e.currentTarget;
    var whichBtn = $(mainBtn).data("button");
    $.ajax({
      method: "get",
      url: "/send",
      data: { }
    }).done(function(){
      $(".mainBtns").hide();
      $(".boopMessages").show();
    })
  }
)

$(".boopMessage").click(
  function(e){
    var boopMessage = e.currentTarget;
    messageid = $(boopMessage).data("boop");
    $.ajax({
      method: "get",
      url: "/",
      data: { }
    }).done(function(){
      $(".boopMessages").hide();
      $(".boopRecipients").show();
    })
  }
)

$(".boopRecipient").click(
  function(e){
    var boopRecipient = e.currentTarget;
    var recipientUserid = $(boopRecipient).data("recipient-userid");
    $.ajax({
      method: "get",
      url: "/send",
      data: {userid: userid,
             recipient: recipientUserid,
             message: messageid }
    }).done(function(){
      $(".boopRecipients").hide();
      $(".mainBtns").show();
      console.log(userid +  " " + messageid + " " + recipientUserid )
    })
  }
)
