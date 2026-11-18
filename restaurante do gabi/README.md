# Restaurante do Gabi — projeto web

Site institucional responsivo, em português, adaptado do template gratuito **Sarab**. Abra `sarab/index.html` no navegador. A página usa os arquivos locais de CSS, JavaScript e imagens da pasta `sarab/`.

## Pesquisa e escolha do tema

Foi considerado o encaixe do layout ao segmento, responsividade, facilidade de personalização e disponibilidade gratuita. Foram consultadas opções de restaurantes no ThemeWagon, BootstrapMade e Colorlib: Sarab (ThemeWagon), TasteIt (ThemeWagon/Colorlib), Delicious (BootstrapMade) e Burger Restaurant (Colorlib). Entre as opções, Sarab foi escolhido porque já traz seções de apresentação, cardápio, imagens de pratos e contato adequadas à proposta do Restaurante do Gabi, reduzindo adaptações estruturais.

- **Tema escolhido:** Sarab — Free Fast Food & Restaurant HTML Template.
- **Download e informações:** https://themewagon.com/themes/sarab/
- **Demonstração:** https://themewagon.github.io/sarab/
- **Repositório de origem do template:** https://github.com/themewagon/sarab
- **Criação:** Bestwpware e equipe; distribuição ThemeWagon. O README de origem identifica a licença como MIT. Consulte os termos e arquivos de licença junto ao download antes de redistribuir.
- **Outras opções consultadas:** [TasteIt](https://colorlib.com/wp/template/tasteit/), [Delicious](https://bootstrapmade.com/delicious-free-restaurant-bootstrap-theme/) e [Burger Restaurant](https://colorlib.com/wp/template/burger-restaurant/).

## Personalizações

- Conteúdo reescrito em português do Brasil para o Restaurante do Gabi, com navegação, apresentação, história/proposta, cardápio, galeria e contato.
- Texto e rótulos adequados ao público local; preços, endereço, telefone, horários, avaliações, estatísticas e pedidos não foram inventados. Informações comerciais pendentes aparecem como itens a confirmar.
- Cardápio de demonstração com filtros funcionais e fotos locais herdadas do template. As descrições e fotos são ilustrativas; confirmar catálogo, ingredientes e preços com o cliente.
- Formulário demonstrativo com retorno visual, sem transmissão ou armazenamento de dados. É necessário integrar e testar um serviço de atendimento antes do uso real.
- CSS próprio em `sarab/css/custom.css` e JavaScript simples em `sarab/js/custom.js`; estrutura responsiva com Bootstrap incluído no projeto.

## Gerar os arquivos de entrega

Com Python 3 instalado, execute na raiz do repositório:

```bash
python "restaurante do gabi/gerar_entrega.py"
```

O script gera `restaurante do gabi/entrega/Documentacao-do-projeto.docx` e `restaurante do gabi/entrega/Projeto-Restaurante-do-Gabi.zip`. O ZIP reúne os arquivos do site, este README, os créditos/licença e a documentação. Os dados fictícios ou pendentes devem ser revisados pelo cliente antes de publicar.

## Publicação

É um site estático; pode ser hospedado em GitHub Pages ou outro serviço de hospedagem estática. Não foi publicado nem enviado ao Google Drive por esta entrega. Endereço, telefone, horários, canais de pedido e integração de formulário precisam ser fornecidos pelo responsável pelo restaurante.
