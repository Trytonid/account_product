#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Account Product',
    'name_bg_BG': 'Сметка за продукт',
    'name_de_DE': 'Buchhaltung Artikel',
    'name_es_CO': 'Contabilidad de Inventarios',
    'name_es_ES': 'Contabilidad de productos',
    'name_fr_FR': 'Compte produit',
    'name_nl_NL': 'Boekhouding voor producten',
    'version': '2.1.0',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': '''Add accounting properties on product and category like:
    - account for expense / revenue
    - taxes for customer / supplier
''',
    'description_bg_BG': '''Добавя счетоводни свойства на продукт и категория като:
    - сметка за разходи / приходу
    - данъци за клиент / доставчик
''',
    'description_de_DE': '''Fügt Eigenschaften für die Buchhaltung zu Artikeln und Artikelkategorien hinzu:
    - Aufwands- und Ertragskonto
    - Steuern für Kunden und Lieferanten
''',
    'description_es_CO': '''Adiciona propiedades contables en productos y categorías:
    - contabilidad para gastos / ganancias
    - impuestos para cliente / proveedor
''',
    'description_es_ES': '''Añade propiedades de contabilidad productos y categorías como:
    - Cuenta para gastos / ingresos
    - impuestos para cliente / proveedor
''',
    'description_fr_FR': '''Ajoute des propriétés comptables sur les produits et leurs caétgories:
    - comptes de charge et revenu
    - taxes client et fournisseur
''',
    'description_nl_NL': '''Voegt boekhouding eigenschappen toe aan product en categorie als:
    - rekening voor kosten / opbrengsten
    - belastingregels voor klanten en leveranciers
''',
    'depends': [
        'ir',
        'account',
        'company',
        'product',
    ],
    'xml': [
        'product.xml',
    ],
    'translation': [
        'locale/bg_BG.po',
        'locale/de_DE.po',
        'locale/es_CO.po',
        'locale/es_ES.po',
        'locale/fr_FR.po',
        'locale/nl_NL.po',
    ]
}
