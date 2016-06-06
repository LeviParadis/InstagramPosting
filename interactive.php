<?php
require_once 'user_info.php';
?>
<html>

<?php

// Set the username and password of the account that you wish to post a photo to
$username = 'jimmyjohnson3674';
$password = 'leviiscool1';

// Set the path to the file that you wish to post.
// This must be jpeg format and it must be a perfect square
$filename = 'square.jpg';

// Set the caption for the photo
$caption = 'Test';
ProcessPost($username,$password,$filename,$caption);


?>