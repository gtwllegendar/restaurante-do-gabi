#!/usr/bin/env python3
"""Gera uma documentação DOCX simples e um ZIP com o site adaptado."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "sarab"
OUT = ROOT / "entrega"
DOCX = OUT / "Documentacao-do-projeto.docx"
ARCHIVE = OUT / "Projeto-Restaurante-do-Gabi.zip"

TITLE = "Projeto Web — Restaurante do Gabi"
SECTIONS = [
    ("Pesquisa e escolha do tema", [
        "Foram pesquisados temas gratuitos para restaurantes em ThemeWagon, BootstrapMade e Colorlib, considerando responsividade, seções disponíveis e facilidade de personalização.",
        "Tema escolhido: Sarab — Free Fast Food & Restaurant HTML Template. O layout de página única já apresenta seções para introdução, cardápio, galeria e contato, adequadas ao projeto.",
        "Alternativas consultadas: TasteIt (Colorlib), Delicious (BootstrapMade) e Burger Restaurant (Colorlib).",
        "Sarab: https://themewagon.com/themes/sarab/ | Demonstração: https://themewagon.github.io/sarab/ | Origem: https://github.com/themewagon/sarab",
    ]),
    ("Créditos e licença", [
        "O README de origem atribui o template a Bestwpware e equipe, distribuído por ThemeWagon, e informa licença MIT. Confira o arquivo de licença e os termos atuais do pacote antes de redistribuir ou usar comercialmente.",
    ]),
    ("Personalizações realizadas", [
        "Conteúdo e navegação em português do Brasil, com apresentação do Restaurante do Gabi, proposta da casa, cardápio demonstrativo, galeria e contato.",
        "CSS próprio para cores quentes, legibilidade e telas móveis; JavaScript implementa filtros de categorias e retorno visual do formulário.",
        "Fotos do tema são ilustrativas. Valores, endereço, telefone, horário, avaliações e dados de operação não foram inventados: devem ser confirmados com o cliente.",
        "O formulário é demonstrativo, não envia nem armazena dados. É necessário integrar um canal de atendimento para receber mensagens.",
    ]),
    ("Arquivos e execução", [
        "Site: sarab/index.html. Estilo: sarab/css/custom.css. Interações: sarab/js/custom.js. Abra index.html no navegador para visualizar.",
        "O pacote ZIP inclui o site e os documentos de apoio. Execute python \"restaurante do gabi/gerar_entrega.py\" na raiz do repositório para gerar esta documentação DOCX e o ZIP.",
    ]),
    ("Pendências antes da publicação", [
        "Confirmar informações reais do restaurante; trocar as fotos por imagens autorizadas; validar cardápio, preços e disponibilidade; configurar pedidos e formulário e testar em celular e computador.",
        "O projeto não foi publicado nem enviado ao Google Drive. O ZIP pode ser gerado localmente pelo script.",
    ]),
]


def paragraph(text, style=None):
    style_xml = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f'<w:p>{style_xml}<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def create_docx():
    OUT.mkdir(parents=True, exist_ok=True)
    body = paragraph(TITLE, "Title") + paragraph("Pesquisa de template, escolha e adaptações", "Subtitle")
    for heading, items in SECTIONS:
        body += paragraph(heading, "Heading1")
        for item in items:
            body += paragraph(item, "ListBullet")
    body += '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>'
    document = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>{body}</w:body></w:document>'
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:color w:val="8E3422"/><w:sz w:val="36"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:rPr><w:color w:val="766E68"/><w:sz w:val="24"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:keepNext/></w:pPr><w:rPr><w:b/><w:color w:val="8E3422"/><w:sz w:val="28"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="ListBullet"><w:name w:val="List Bullet"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="420" w:hanging="220"/></w:pPr></w:style></w:styles>'''
    with ZipFile(DOCX, "w", ZIP_DEFLATED) as doc:
        doc.writestr("[Content_Types].xml", '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>')
        doc.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
        doc.writestr("word/_rels/document.xml.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
        doc.writestr("word/document.xml", document)
        doc.writestr("word/styles.xml", styles)


def create_zip():
    files = [p for p in ROOT.rglob("*") if p.is_file() and OUT not in p.parents and p != ARCHIVE]
    with ZipFile(ARCHIVE, "w", ZIP_DEFLATED) as archive:
        for path in sorted(files):
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            archive.write(path, path.relative_to(ROOT.parent))
        archive.write(DOCX, DOCX.relative_to(ROOT.parent))
    return len(files)


if __name__ == "__main__":
    create_docx()
    count = create_zip()
    print(f"Documentação criada: {DOCX}")
    print(f"ZIP criado: {ARCHIVE} ({count} arquivos do projeto)")
