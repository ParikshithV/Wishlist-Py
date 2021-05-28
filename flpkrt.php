<?php
  include('simple_html_dom.php');
  $opts = array('http'=>array('header' => "User-Agent:MyAgent/1.0\r\n"));
  $context = stream_context_create($opts);
  $header = file_get_contents('https://www.flipkart.com/wildcraft-men-black-sandals/p/itm39dc14955bca3?pid=SNDFUG399ZHGGNSW&lid=LSTSNDFUG399ZHGGNSWT9QRKW&marketplace=FLIPKART&store=osp&srno=b_1_6&otracker=hp_omu_Today%2527s%2BFashion%2BDeals_2_7.dealCard.OMU_85A9UAX0MDG6_6&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Today%2527s%2BFashion%2BDeals_NA_dealCard_cc_2_NA_view-all_6&fm=neo%2Fmerchandising&iid=2220506e-f7a4-4e92-86ff-b6d9f79e9bf4.SNDFUG399ZHGGNSW.SEARCH&ppt=browse&ppn=browse&ssid=o107okx6ls0000001622237980596',false,$context);
  $html = str_get_html($header);
  echo $html->find('h1',0)->plaintext;
  echo "<br>";
  echo $html->find('div[class=_30jeq3 _16Jk6d]',0)->plaintext;
  echo "<br>";
  echo "<img src='";
  echo "https://seeklogo.com/images/F/flipkart-logo-3F33927DAA-seeklogo.com.png";
  echo "'>";
  // foreach($html->find('img') as $element)
  //      echo $element->src . '<br>';
?>
