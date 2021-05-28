<?php
  include('simple_html_dom.php');
  $opts = array('http'=>array('header' => "User-Agent:MyAgent/1.0\r\n"));
  $context = stream_context_create($opts);
  $header = file_get_contents('https://inkmesilly.com/product/i-need-my-space-for-oneplus-5/',false,$context);
  $html = str_get_html($header);
  echo $html->find('h1',0)->plaintext;
  echo "<br>";
  echo $html->find('span[class=woocommerce-Price-currencySymbol]',0)->plaintext;
  echo "99";
  echo "<br>";
  echo "<img src='";
  echo $html->find('img',12)->src;
  echo "'>";
  // foreach($html->find('img') as $element)
  //      echo $element->src . '<br>';
?>
