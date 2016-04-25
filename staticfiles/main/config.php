<?php
$db_connect = mysql_connect('localhost', 'root', '1221');
if (!$db_connect) {
    exit("Не удалось подключиться к бд".mysql_error());
}
if (!mysql_select_db('local_resource', $db_connect)) {
    exit("Нет такой бд".mysql_error());
}
mysql_query("SET NAMES 'UTF8'");
?>