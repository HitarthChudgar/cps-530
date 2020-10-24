#!/usr/bin/perl
use CGI':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

print "Content-type: text/html\n";

my $firstName = param('firstName');
my $lastName = param('lastName');
my $email = param('email');
my $gender = param('gender');
my $country = param('country');
my $stars = param('stars');
my $comments = param('comments');

print <<"HTML CONTENT";

<html>
<head>
<title>Feedback Submission</title>
<link href="https://fonts.googleapis.com/css2?family=Interdisplay=swap" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    html,
    body {
        font-family: Inter, sans-serif;
        font-size: 16px;
        background: #232526;
        /* fallback for old browsers */
        background: -webkit-linear-gradient(to right, #414345, #232526);
        /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to right, #414345, #232526);
        /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        text-align: center;
        background-attachment: fixed;
    }

    #main {
        height: auto;
        width: 600px;
        margin: 10px auto;
        background: white;
        padding: 1px;
        -webkit-box-shadow: 10px 10px 49px -13px rgba(0, 0, 0, 0.39);
        -moz-box-shadow: 10px 10px 49px -13px rgba(0, 0, 0, 0.39);
        box-shadow: 10px 10px 49px -13px rgba(0, 0, 0, 0.39);
        border-radius: 15px;
        transition: ease all 0.3s;
    }

    img {
        width: 200px;
        height: 200px;
    }

    input,
    select,
    textarea {
        margin: 3px;
        border-radius: 5px;
        border: 1px solid grey;
    }

    .btn {
        border-radius: 8px;
        border: none;
        color: #232526;
        border-radius: 4px;
        font-size: 14px;
        text-align: center;
        padding: 10px 15px;
        cursor: pointer;
    }

    .btn:hover {
        box-shadow: 0px 14px 18px 0px rgba(0, 0, 0, 0.10), 0px 17px 50px 0px rgba(0, 0, 0, 0.10);
        color: white;
        background-color: #00ff90;
        border-radius: 4px;
        font-size: 18px;
        font-weight: 600;
    }

    /* responsive width */
    @media screen and (max-width: 768px) {
        #main {
            width: 350px;
        }
    }
</style>
</head>
<body>
<div id="main">
<h2>Thanks for your feedback $firstName!</h2>
<img src="./img/teamwork.png" alt="people">
<h3>Submitted information:</h3>
<div id="info">
First Name:&emsp;&nbsp;$firstName<br>
Last Name:&emsp;&nbsp;$lastName<br>
Email:&emsp;&emsp;&emsp;&nbsp;&nbsp;<a href="mailto:$email">$email</a><br>
Gender:&emsp;&emsp;&ensp;&nbsp;$gender<br>
Country:&emsp;&emsp;&ensp;$country<br>
Rating:&emsp;&emsp;&emsp;$stars&#9733<br><br>
</div>
<div id="comments">
Comments:<br><br>$comments
<br><br>
</div>
<button class="btn" onclick="window.location.href = '../../cps530/lab4.html';">Return To Form</button>
<br><br>
</div>
</body>
</html>
HTML CONTENT
