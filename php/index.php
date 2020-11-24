<?php

$msg = "Hello World";
echo $msg;
var_dump($msg);

define("PI",3.141592);
echo PI;

$colors = ["red","blue","yellow"];
echo $colors[0];

$members = [
    "one" => "first",
    "two" => "second"
  ];
echo $members["one"]

function hello($var){
  echo "Hello $var";
}  
hello("world");

?>

<ul>
<?php for($1=0;$1<10;$i++): ?>
<li><?php echo $i ?></li>
<?php endfor; ?>
</ul>