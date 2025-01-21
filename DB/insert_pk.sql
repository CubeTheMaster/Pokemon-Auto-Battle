
-- Inserimenti nella tabella pokemon
INSERT INTO pokemon (id, name, type_1, type_2, hp, attack, defense, sp_attack, sp_defense, speed)
VALUES
(25, 'Pikachu', 'Electric', NULL, 35, 55, 40, 50, 50, 90),
(6, 'Charizard', 'Fire', 'Flying', 78, 84, 78, 109, 85, 100),
(9, 'Blastoise', 'Water', NULL, 79, 83, 100, 85, 105, 78),
(94, 'Gengar', 'Ghost', 'Poison', 60, 65, 60, 130, 75, 110),
(248, 'Tyranitar', 'Rock', 'Dark', 100, 134, 110, 95, 100, 61),
(373, 'Salamence', 'Dragon', 'Flying', 95, 135, 80, 110, 80, 100),
(530, 'Excadrill', 'Steel', 'Ground', 110, 135, 60, 50, 65, 88),
(149, 'Dragonite', 'Dragon', 'Flying', 91, 134, 95, 100, 100, 80),
(392, 'Infernape', 'Fire', 'Fighting', 76, 104, 71, 104, 71, 108),
(448, 'Lucario', 'Fighting', 'steel', 70, 110, 70, 115, 70, 90),
(384, 'Rayquaza', 'Dragon', 'Flying', 105, 150, 90, 150, 90, 95),
(1006, 'Iron_Valiant', 'Fairy', 'Fighting', 74, 130, 90, 120, 60, 116),
(497, 'Serperior', 'Grass', NULL, 75, 75, 95, 75, 95, 113),
(282, 'Gardevoir', 'Psychic', 'Fairy', 68, 65, 65, 125, 115, 80);

INSERT INTO pozione (nome, quatità)
VALUES
('pozione', 3),
('superpozione', 2),
('iperpozione', 1);

-- Inserimenti nella tabella mossa
INSERT INTO mossa (id, nome, type_1, damage, accuracy, categoria)
VALUES
(1, 'Tackle', 'Normal', 20, 100, 'fisica'),
(2, 'Flamethrower', 'Fire', 45, 100, 'speciale'),
(3, 'Thunderbolt', 'Electric', 45, 100, 'speciale'),
(4, 'Earthquake', 'Ground', 50, 100, 'fisica'),
(5, 'Ice Beam', 'Ice', 45, 100, 'speciale'),
(6, 'Crunch', 'Dark', 40, 100, 'fisica'),
(7, 'Shadow Ball', 'Ghost', 40, 100, 'speciale'),
(8, 'Stone Edge', 'Rock', 50, 80, 'fisica'),
(9, 'Hyper Beam', 'Normal', 75, 90, 'speciale'),
(10, 'Flare Blitz', 'Fire', 60, 100, 'fisica'),
(11, 'Quick Attack', 'Normal', 20, 100, 'fisica'),
(12, 'Iron Tail', 'Steel', 50, 75, 'fisica'),
(13, 'Dragon Claw', 'Dragon', 40, 100, 'fisica'),
(14, 'Air Slash', 'Flying', 37, 95, 'speciale'),
(15, 'Hydro Pump', 'Water', 55, 80, 'speciale'),
(16, 'Protect', 'Normal', 0, 100, 'speciale'),
(17, 'Will-O-Wisp', 'Fire', 0, 75, 'speciale'),
(18, 'Sludge Bomb', 'Poison', 90, 100, 'speciale'),
(19, 'Pursuit', 'Dark', 40, 100, 'fisica'),
(20, 'Fly', 'Flying', 45, 95, 'fisica'),
(21, 'Iron Head', 'Steel', 40, 100, 'fisica'),
(22, 'X-Scissor', 'Bug', 40, 100, 'fisica'),
(23, 'Fire Punch', 'Fire', 37, 100, 'fisica'),
(24, 'Close Combat', 'Fighting', 60, 100, 'fisica'),
(25, 'U-turn', 'Bug', 35, 100, 'fisica'),
(26, 'Extreme Speed', 'Normal', 40, 100, 'fisica'),
(27, 'Aura Sphere', 'Fighting', 40, 100, 'speciale'),
(28, 'Moonblast', 'Fairy', 47, 100, 'speciale'),
(29, 'Leaf Storm', 'Grass', 65, 90, 'speciale'),
(30, 'Draco Meteor', 'Dragon', 65, 90, 'speciale'),
(31, 'Psychic', 'Psychic', 45, 100, 'speciale'),
(32, 'Focus Blast', 'Fighting', 60, 70, 'speciale'),
(33, 'Flash Cannon', 'Steel', 40, 100, 'speciale'),
(34, 'Energy Ball', 'Grass', 45, 100, 'speciale'),
(35, 'Dragon Pulse', 'Dragon', 42, 100, 'speciale'),
(36, 'Brick Break', 'Fighting', 37, 100, 'fisica'),
(37, 'Spirit Break', 'Fairy', 37, 100, 'fisica');

-- Inserimenti nella tabella conosce (associando i Pokémon alle mosse)
INSERT INTO conosce (id_pk, id_mossa)
VALUES
(25, 1),  -- Pikachu conosce Tackle
(25, 3),  -- Pikachu conosce Thunderbolt
(25, 11), -- Pikachu conosce Quick Attack
(25, 12), -- Pikachu conosce Iron Tail

(6, 2),   -- Charizard conosce Flamethrower
(6, 4),   -- Charizard conosce Earthquake
(6, 13),  -- Charizard conosce Dragon Claw
(6, 14),  -- Charizard conosce Air Slash

(9, 4),   -- Blastoise conosce Earthquake
(9, 5),   -- Blastoise conosce Ice Beam
(9, 15),  -- Blastoise conosce Hydro Pump
(9, 16),  -- Blastoise conosce Protect

(94, 7),  -- Gengar conosce Shadow Ball
(94, 6),  -- Gengar conosce Crunch
(94, 17), -- Gengar conosce Will-O-Wisp
(94, 18), -- Gengar conosce Sludge Bomb

(248, 8), -- Tyranitar conosce Stone Edge
(248, 6), -- Tyranitar conosce Crunch
(248, 19),-- Tyranitar conosce Pursuit
(248, 5), -- Tyranitar conosce Ice Beam

(373, 2), -- Salamence conosce Flamethrower
(373, 4), -- Salamence conosce Earthquake
(373, 13),-- Salamence conosce Dragon Claw
(373, 20),-- Salamence conosce Fly

(530, 4), -- Excadrill conosce Earthquake
(530, 8), -- Excadrill conosce Stone Edge
(530, 21),-- Excadrill conosce Iron Head
(530, 22),-- Excadrill conosce X-Scissor

(149, 3), -- Dragonite conosce Thunderbolt
(149, 4), -- Dragonite conosce Earthquake
(149, 13),-- Dragonite conosce Dragon Claw
(149, 23),-- Dragonite conosce Fire Punch

(392, 2), -- Infernape conosce Flamethrower
(392, 6), -- Infernape conosce Crunch
(392, 24),-- Infernape conosce Close Combat
(392, 25);-- Infernape conosce U-turn

(448, 26), -- Lucario conosce Extreme Speed
(448, 27), -- Lucario conosce Aura Sphere
(448, 33), -- Lucario conosce Flash Cannon
(448, 36), -- Lucario conosce Brick Break

(282, 28), -- Gardevoir conosce Moonblast
(282, 31), -- Gardevoir conosce Psychic
(282, 34), -- Gardevoir conosce Energy Ball
(282, 3),  -- Gardevoir conosce Thunderbolt

(497, 29), -- Serperior conosce Leaf Storm
(497, 34), -- Serperior conosce Energy Ball
(497, 32), -- Serperior conosce Focus Blast
(497, 1),  -- Serperior conosce Tackle

(384, 30), -- Rayquaza conosce Draco Meteor
(384, 35), -- Rayquaza conosce Dragon Pulse
(384, 2),  -- Rayquaza conosce Flamethrower
(384, 3),  -- Rayquaza conosce Thunderbolt

(1006, 30); -- Iron Valiant conosce Draco Meteor
(1006, 35), -- Iron Valiant conosce Dragon Pulse
(1006, 32); -- Iron Valiant conosce Focus Blast
(1006, 37); -- Iron Valiant conosce Spirit Break