<?php
include 'config.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

include 'header.php';

// Se l'utente è amministratore, può vedere tutte le immagini
$is_admin = ($_SESSION['role'] == 'admin');

if ($is_admin) {
    $stmt = $pdo->query("SELECT * FROM images");
} else {
    $stmt = $pdo->query("SELECT * FROM images WHERE inappropriate = 0");
}

$images = $stmt->fetchAll();
?>

<h1>Catalogo Immagini</h1>

<?php foreach ($images as $image): ?>
    <div>
        <img src="<?php echo $image['filename']; ?>" alt="Immagine" width="200" />
        <p>Caption: <i><?php echo $image['description']; ?></i></p>
        <?php if ($is_admin): ?>
            <form method="post" action="inappropriate.php">
                <input type="hidden" name="image_id" value="<?php echo $image['id']; ?>" />
                <button type="submit">Segnala come Inappropriata</button>
            </form>
        <?php endif; ?>
    </div>
<?php endforeach; ?>


<?php
include 'footer.php';
?>
