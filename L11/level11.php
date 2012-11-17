#!/usr/bin/php5

<?php

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        //echo "$text[$i]", "\n";
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
echo "default data json encoded: ", json_encode($defaultdata), "\n";
echo "len: ", strlen(json_encode($defaultdata)), "\n";
echo "defaultdata json encoded, encrypted: ", xor_encrypt(json_encode($defaultdata)), "\n";
echo "defaultdata json encoded, encrypted, base64 encoded: ", base64_encode(xor_encrypt(json_encode($defaultdata))), "\n";

//founr key: qw8J
$sol_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
echo "desired cookie data: ", base64_encode(xor_encrypt(json_encode($sol_data))), "\n";
?>
