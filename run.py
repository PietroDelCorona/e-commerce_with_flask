from market import app, db
from market.models import Item
import os

def initialize_database():
    if not os.path.exists('market.db'):
        with app.app_context():
            db.create_all()
            insert_test_data()

def insert_test_data():
    with app.app_context():
        # Verifica se há dados na tabela para evitar inserção de dados duplicados
        if Item.query.count() == 0:
            items = [
                Item(name='Smartphone XYZ', price=799, barcode='123456789013', description='Smartphone com tela de 6.5" e 128GB de armazenamento.'),
                Item(name='Laptop ABC', price=1200, barcode='234567890124', description='Laptop com 16GB de RAM, 512GB SSD e processador Intel i7.'),
                Item(name='Fone de Ouvido Bluetooth', price=150, barcode='345678901235', description='Fone de ouvido sem fio com cancelamento de ruído.'),
                Item(name='Tablet 10.1"', price=350, barcode='456789012346', description='Tablet com tela de 10.1" e 64GB de armazenamento.'),
                Item(name='Smartwatch Fitness', price=250, barcode='567890123457', description='Smartwatch com monitoramento de saúde e GPS.'),
                Item(name='Câmera Digital HD', price=650, barcode='678901234568', description='Câmera digital com resolução de 20MP e zoom óptico de 10x.'),
                Item(name='Teclado Mecânico RGB', price=100, barcode='789012345679', description='Teclado mecânico com retroiluminação RGB e switches mecânicos.'),
                Item(name='Mouse Gamer', price=75, barcode='890123456790', description='Mouse gamer com alta precisão e botões programáveis.'),
                Item(name='Carregador Portátil 20000mAh', price=80, barcode='901234567891', description='Carregador portátil com capacidade de 20000mAh e duas portas USB.'),
                Item(name='HD Externo 2TB', price=120, barcode='012345678902', description='Disco rígido externo com capacidade de 2TB e conexão USB 3.0.'),
            ]
            db.session.add_all(items)
            db.session.commit()

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)