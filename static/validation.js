var form = $("#login")
var email = form[0]
var username = form[1]
var password = form[2]

var values = [];


jQuery.validator.addMethod("uniqueFields", function(value, element, params) {
  var values = params.map(function (selector) { return $(selector).val(); });
  return !_.includes(values, value);
},
"email, username, password must not match");


form.validate({
rules:{
  email:{
  required: true,
  email: true,
  uniqueFields: ["#password", "#username"]
},
username:{
  required: true,
  minlength: 3,
  uniqueFields: ["#password", "#email"]

},
password:{
  required: true,
  minlength: 5,
  uniqueFields: ["#email", "#username"]

},
password_confirm:{
  required: true,
  minlength: 5,
  equalTo: "#password"

}

},
messages:{
  email:{
    required: "Please provide a valid email"
  },
  username:{
    required: "Please provide a username",
    minlength: "Username must be greater than 3 chars"
  },
  password:{
    required: "Please provide a password",
    minlength: "Password must by 5 chars or greater"
  },
  password_confirm:{
    required: "You must confirm your password",
    equalTo: "Passwords must match"
  }
}}
);
