<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Kühlschrankkamera</title>
<link rel="stylesheet" type="text/css" href="lightbox/css/jquery.lightbox-0.5.css" />
<link rel="stylesheet" type="text/css" href="css/demo.css" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<script type="text/javascript" src="lightbox/js/jquery.lightbox-0.5.pack.js"></script>
<script type="text/javascript" src="script.js"></script>

<div id="container">

  <div id="heading">
    <h1>Das Leben durch die Augen eines Kühlschranks</h1>
  </div>

<div id="gallery">

  <?php

  $config = json_decode(file_get_contents("config.json"));
  $directory    = $config['directory'];
  $brThreshold  = $config['brightnessThreshold'];
  $sleepTimer   = $config['adjustmentTimer'];
  $capPin       = $config['capacitorPing'];

  $handle = opendir($directory);

  while (false !== ($entry = readdir($handle))) {
    if ($entry != "." && $entry != "..") {
      $exploded = explode('.', $entry);
      
      $extention = strtolower(array_pop($exploded));
      $title = htmlspecialchars(implode('.', $entry));

      if($extention == 'jpg')
      {
        ;
        echo '<div class="pic '. ($pos + 1) % 4 == 0 ? 'nomargin' : '' . '" style="background:url(' . $directory . '/' . $entry . ') no-repeat 50% 50%;">
        <a href="' . $directory . '/' . $entry . '" title="' . $title . '" target="_blank">' . $title . '</a>
        </div>';

        $pos++;
      }
    }
  }
  closedir($handle);


  ?>

  <div class="clear"></div>
  </div>

  <div id="footer"> 
    <h2><?php echo 'Kondensator an pin: ' . $capPin . ', Lichtgrenzwert bei: ' . $brThreshold . ', Auslöseverzögerung: ' . $sleepTimer ?></h2>
  </div>

</div>