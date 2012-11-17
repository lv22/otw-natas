#!/usr/bin/php5

<?php
$filename = $argv[1];
$image_type = exif_imagetype($filename);

echo "Image type of ", $filename ," is: ", $image_type, "\n"

?>
