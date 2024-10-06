USE image_catalog;

-- Popolamento tabella users con un amministratore e alcuni utenti normali
INSERT INTO users (username, password, role) VALUES
('admin', '$2y$10$Ew1S/oBgOzddwzD2hLT0t.8Oofh1E.H9RuQ4YjGb6lgT0Gh5G2ftK', 'admin'),  -- Password: admin123
('user1', '$2y$10$e1zUV7EvFQb/VqjUS1U15O04kDXdzboF4AGU.yPvgHSvmzgV6hg16', 'user'),   -- Password: user123
('user2', '$2y$10$yfU8F5v/OAVYoZz2EB6gNOozF.SAqA.VduOASCN5UuMJPmq41E7be', 'user');   -- Password: user123


-- added 2 lines.
-- * Riccardo does NOT work
-- * rasmuslerdorf DOES work.
INSERT INTO users (username, password, role) VALUES
    ('riccardo', '$2y$10$yfU8F5v/OAVYoZz2EB6gNOozF.SAqA.VduOASCN5UuMJPmq41E7be', 'user');   -- Password: user123
-- https://www.php.net/manual/en/function.password-verify.php
-- This hash works
INSERT INTO users (username, password, role) VALUES
    ('rasmuslerdorf','$2y$10$.vGA1O9wmRjrwAVXD98HNOgsNpDczlqm3Jq7KnEd1rVAGv3Fykk1a', 'admin');   -- Password: rasmuslerdorf


-- Popolamento tabella images con alcune immagini iniziali
INSERT INTO images (user_id, filename, inappropriate) VALUES
(2, 'uploads/image1.png', 0),
(2, 'uploads/image2.png', 0),
(3, 'uploads/image3.png', 1),  -- Immagine segnalata come inappropriata
(3, 'uploads/image4.png', 0);
