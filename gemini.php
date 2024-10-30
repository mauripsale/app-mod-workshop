<?php
    include 'header.php';
?>
<h1>Gemini</h1>

This is currently broken and requires installing stuff..
<?php

// This is broken
// https://php-amarcord-dev-839850161816.europe-west8.run.app/gemini.php
// TODO(ricc):
//  1. require login, so not everyone uses it.
//  2. add composer to Dockerfile. Looks like composer 2.2. supports it: https://getcomposer.org/doc/00-intro.md
    // use GeminiAPI\Client;
    // use GeminiAPI\Resources\Parts\TextPart;

    // $api_key = getenv('GEMINI_API_KEY')  ?: 'DONT HARD CODE IT HERE!';

    // $client = new Client($api_key);
    // $response = $client->geminiPro()->generateContent(
    //     new TextPart('PHP in less than 100 chars'),
    // );

    // print "[REMOVEME!!] api_key=$api_key";
    // print $response->text();

?>
<?php
    include 'footer.php';
?>
