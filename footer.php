<hr/>
<div class='footer'>
    <?php
    # PHP 5.3 syntax. In 7 its more elegant: $name = $_GET['name'] ?? 'john doe';
    $appname = getenv('APP_NAME')  ?: '_APP_NAME_SCONOSCIUTA_'; # https://stackoverflow.com/questions/5972516/best-way-to-give-a-variable-a-default-value-simulate-perl
    #$app_version = getenv('APP_VERSION')  ?: '0.0.?';
    $app_version = file_get_contents('VERSION');
    echo "Welcome to <b>$appname</b> v<b>$app_version</b>!";
    # 'version' => env('APP_VERSION', '1.0.0'),
    ?>
</div>
