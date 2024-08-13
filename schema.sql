CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email_address TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    budget INTEGER NOT NULL DEFAULT 5000
);

CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price INTEGER NOT NULL,
    barcode TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    owner INTEGER,
    FOREIGN KEY (owner) REFERENCES user (id)
);

INSERT INTO item (name, price, barcode, description)
VALUES
    ('Smartphone XYZ', 799, '123456789012', 'Smartphone com tela de 6.5" e 128GB de armazenamento.'),
    ('Laptop ABC', 1200, '234567890123', 'Laptop com 16GB de RAM, 512GB SSD e processador Intel i7.'),
    ('Fone de Ouvido Bluetooth', 150, '345678901234', 'Fone de ouvido sem fio com cancelamento de ruído.'),
    ('Tablet 10.1"', 350, '456789012345', 'Tablet com tela de 10.1" e 64GB de armazenamento.'),
    ('Smartwatch Fitness', 250, '567890123456', 'Smartwatch com monitoramento de saúde e GPS.'),
    ('Câmera Digital HD', 650, '678901234567', 'Câmera digital com resolução de 20MP e zoom óptico de 10x.'),
    ('Teclado Mecânico RGB', 100, '789012345678', 'Teclado mecânico com retroiluminação RGB e switches mecânicos.'),
    ('Mouse Gamer', 75, '890123456789', 'Mouse gamer com alta precisão e botões programáveis.'),
    ('Carregador Portátil 20000mAh', 80, '901234567890', 'Carregador portátil com capacidade de 20000mAh e duas portas USB.'),
    ('HD Externo 2TB', 120, '012345678901', 'Disco rígido externo com capacidade de 2TB e conexão USB 3.0.');