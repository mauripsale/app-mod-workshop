<?php

    use GeminiAPI\Client;
    use GeminiAPI\Resources\Parts\TextPart;

    $api_key = getenv('GEMINI_API_KEY')  ?: 'DONT HARD CODE IT HERE!';

    $client = new Client($api_key);
    $response = $client->geminiPro()->generateContent(
        new TextPart('PHP in less than 100 chars'),
    );

    print "[REMOVEME!!] api_key=$api_key";
    print $response->text();

?>
