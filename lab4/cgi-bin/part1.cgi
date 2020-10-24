#!/usr/bin/perl
use CGI':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;
print "Content-type: text/html\n\n";
print <<"HTML CONTENT";
<html>
<head>
<title>CPS 530 | Lab 4</title>
<link href="https://fonts.googleapis.com/css2?family=Interdisplay=swap" rel="stylesheet">
</head>
<body>
<h1 style="text-align: center; font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 700; color: #16a085;">This is my first Perl program</h1>
</body>
</html>
HTML CONTENT
