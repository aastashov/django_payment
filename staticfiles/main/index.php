<?php
header("Content-Type:text/html;charset=utf-8");
require_once("staticfiles/config.php");

$query = "SELECT title, url, logo FROM resource";
$result = mysql_query($query);
if (!$result) {
    exit(mysql_error());
}
        echo'
<!DOCTYPE html>
<html lang="ru">
  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Репозиторий</title>
  <link href="staticfiles/styles/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <div class="container" style="padding-top:60px;">
      <h3>Локальные ресурсы компании</h3>
      <hr>
      <div class="row">';

        for ($i=0; $i < mysql_num_rows($result); $i++) { 
            $row = mysql_fetch_array($result, MYSQL_ASSOC);
            printf("
        <div class='col-lg-3 col-md-4 col-sm-12'>
          <a href='%s'>
            <div class='thumbnail'>
                <img src='%s'>
              <div class='caption' align='center'>
                <h3>%s</h3>
              </div>
            </div>
          </a>
        </div>
            ", $row['url'], $row['logo'], $row['title']);
        }

        echo '
      </div>
    </div>
    <script src="staticfiles/jquery.min.js"></script>
    <script src="staticfiles/javascript/bootstrap.min.js"></script>
  </body>
</html>';
?>