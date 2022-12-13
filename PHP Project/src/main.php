<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="veiwport" content="width=device-width, initial-scale-1.0"> 
	<title>PHP Practice</title>
	<link rel="stylesheet" href="../src/style.css" />
</head>
<body>
	<div class="flex-container">
		<div class="header">
			<?php include 'logo.inc.php' ?>
			<?php include 'menu.inc.php' ?>
		</div>
		<div class="about_me">
		<?php include 'index.php' ?>
			<h1> <?php echo $p ?> </h1>
			
			<div class="data">
				<div class="myImg">
					<?php echo '<img src="../img/php-elephant.jpg">'; ?>
				</div>
				
				<div class="fullname">
					<p> Моё имя
						<?php echo $name, ' ', $surname . '<br>';
						      echo 'город', ' ', $city; ?>
					</p>
					<p> Мой возраст
						<?php echo $age; ?>
					лет</p>
					<p> Мы научились создавать переменные </p>
					<p> Изучили простые операции с ними</p>
				</div>
			</div>
			
			<div class="Knowledge">
				<?php include 'knowledge.inc.php'; ?>
				<?php echo $a, ' ', $b, ' ', $c;?>
				<br>
			    <?php
				    $str = 'Здесь проведем простое вычисление: ';
				    $a = '50 + 80 = ';
				    $b = 50;
				    $c = 80;
				    $sum = $b + $c;
				    echo $str, $a, $sum;
				    ?>
				    <br>
				    <?php echo $d ?>
			</div>
			
			<div class="article">
			<p class="text">
			Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero amet sequi iure. Ex, modi doloremque nihil laudantium veniam rerum maiores suscipit architecto magnam aliquid eius quas tempore alias, quidem at earum tempora beatae est quisquam minus, veritatis placeat consectetur. Blanditiis a enim, quos, culpa iure ut assumenda distinctio minima tempora.
			</p>
				
			</div>
		</div>
		    <?php include 'footer.inc.php' ?>
		</div>
	
</body>