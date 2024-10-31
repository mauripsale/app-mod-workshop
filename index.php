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

<h1 class="text-3xl font-bold mb-4">Catalogo Immagini</h1>

<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
<?php foreach ($images as $image): ?>
    <!-- no troppo bislunghe le immagine scusami Gemini anche no.
    <div class="bg-white shadow-md rounded-lg overflow-hidden <?php echo empty($image['description']) ? 'flex flex-col' : ''; ?>">
        <img src="<?php echo $image['filename']; ?>" alt="Immagine" class="<?php echo empty($image['description']) ? 'flex-grow' : 'w-full h-48 object-cover'; ?>" />
    -->
    <div class="bg-white shadow-md rounded-lg overflow-hidden">
        <img src="<?php echo $image['filename']; ?>" alt="Immagine" class="w-full h-48 object-cover" />

        <div class="p-4">
            <?php if (!empty($image['description'])): ?>
                <p class="font-bold">Gemini Caption:</p>
                <p class="italic"><?php echo $image['description']; ?></p>
            <?php endif; ?>
            <?php if ($is_admin): ?>
                <form method="post" action="inappropriate.php" class="mt-2">
                    <input type="hidden" name="image_id" value="<?php echo $image['id']; ?>" />
                    <button type="submit" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                        Flag as Inappropriate
                    </button>
                </form>
            <?php endif; ?>
        </div>
    </div>
<?php endforeach; ?>
</div>


<?php
include 'footer.php';
?>
