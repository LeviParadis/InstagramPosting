<?php
require_once 'user_info.php';

// Set the username and password of the account that you wish to post a photo to
$username = $_GET["username"];
$password = $_GET["password"];
$filename = $_GET["filename"];
$caption = $_GET["caption"];

/*
// $username = 'leviparadis123';
// $password = 'leviiscool1';
*/
// Set the path to the file that you wish to post.
// This must be jpeg format and it must be a perfect square
$filename = 'square.jpg';

// Set the caption for the photo
$caption = 'Test';
ProcessPost($username,$password,$filename,$caption);


?>