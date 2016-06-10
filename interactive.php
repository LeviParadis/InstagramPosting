<?php
require_once 'user_info.php';

// Set the username and password of the account that you wish to post a photo to
$username = $_GET["username"];
$password = $_GET["password"];
$filename = $_GET["filename"];
$caption = $_GET["caption"];

ProcessPost($username,$password,$filename,$caption);


?>